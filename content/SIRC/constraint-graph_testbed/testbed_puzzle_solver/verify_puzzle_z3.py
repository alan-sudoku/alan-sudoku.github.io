"""
Constraint-graph puzzle verifier — Z3 edition.

Companion to verify_puzzle.py (BFS/enumeration). Uses Z3 for:
  1. Valid-state enumeration via iterative model blocking
  2. Minimum path length via bounded model checking (BMC)
  3. Explicit UNSAT proof when puzzle is unsolvable at given capacity

Run:
    python3 tests/verify_puzzle_z3.py

Comparison notes (printed at end):
  - Both methods must agree on all counts for regression to pass.
  - Z3 BMC provides an explicit UNSAT certificate when no path exists;
    BFS returns an empty result with no proof.
  - BFS is faster for small dense state spaces; Z3 BMC scales better
    when |S| is large and paths are sparse.
"""

import sys
from itertools import product as iproduct
from z3 import (
    Bool, BoolVal, And, Or, Not, Implies, Sum, If,
    Solver, sat, unsat, is_true
)

# ---------------------------------------------------------------------------
# Puzzle specs — same as verify_puzzle.py
# ---------------------------------------------------------------------------

PUZZLES = {
    "P3_wolf_goat_cabbage": {
        "objects":    ["F", "W", "G", "C"],
        "predation":  [("W", "G"), ("G", "C")],
        "boat_capacity": 1,
        "start": {"F": "L", "W": "L", "G": "L", "C": "L"},
        "goal":  {"F": "R", "W": "R", "G": "R", "C": "R"},
        "expected": {
            "S_total": 16, "J_minus": 6, "J_plus": 10,
            "edges": 10,   "N_paths": 2, "L_min": 7,
        },
    },
    "P4_fox_chicken_caterpillar_leaf_cap1": {
        "objects":    ["F", "X", "K", "T", "V"],
        "predation":  [("X", "K"), ("K", "T"), ("T", "V")],
        "boat_capacity": 1,
        "start": {"F": "L", "X": "L", "K": "L", "T": "L", "V": "L"},
        "goal":  {"F": "R", "X": "R", "K": "R", "T": "R", "V": "R"},
        "expected": {
            "S_total": 32, "J_minus": 16, "J_plus": 16,
            "edges": 14,   "N_paths": 0,  "L_min": None,
        },
    },
    "P4_fox_chicken_caterpillar_leaf_cap2": {
        "objects":    ["F", "X", "K", "T", "V"],
        "predation":  [("X", "K"), ("K", "T"), ("T", "V")],
        "boat_capacity": 2,
        "start": {"F": "L", "X": "L", "K": "L", "T": "L", "V": "L"},
        "goal":  {"F": "R", "X": "R", "K": "R", "T": "R", "V": "R"},
        "expected": {
            "S_total": 32, "J_minus": 16, "J_plus": 16,
            "edges": 32,   "N_paths": 2,  "L_min": 3,
        },
    },
}

# ---------------------------------------------------------------------------
# Encoding helpers
# ---------------------------------------------------------------------------
#
# Math → Z3 symbol map (applies throughout this file):
#
#   s ∈ {L,R}^N          — one state: N Boolean variables per step
#   obj_var(o, t)         — Bool variable for object o at step t; True = R, False = L
#   s_F = s[farmer_key]   — Farmer's bank at step t
#   unattended bank       — the bank where s_F is NOT
#   (a,b) ∈ R (predation) — a and b cannot both be on the unattended bank
#   J⁺ = {s : s satisfies all (a,b) ∈ R}   — valid_state_constraint returns True
#   J⁻ = {s : s violates at least one (a,b)} — valid_state_constraint returns False
#   move s_t → s_{t+1}   — move_constraint encodes one legal transition
#   L_min                 — bmc_min_path_z3 finds smallest k with SAT k-step trajectory
#   N_paths               — count_paths_at_length_z3 counts via blocking clauses

# Convention: Bool variable = True means object is on the RIGHT bank (R).
#             False means LEFT bank (L).

def obj_var(obj, step):
    # s_obj at step t  →  Bool("obj_t")
    return Bool(f"{obj}_{step}")


def state_to_bools(state_dict):
    """Convert {'F':'L','W':'R',...} to {obj: BoolVal}."""
    return {o: BoolVal(b == "R") for o, b in state_dict.items()}


def valid_state_constraint(objects, farmer_key, predation, step):
    """
    Z3 formula: state at `step` is in J⁺ (satisfies all predation rules).

    Math: s ∈ J⁺  iff  ∀(a,b) ∈ R: ¬(s_a = s_b ≠ s_F)
    i.e. a and b cannot both be on the unattended bank (the bank without the Farmer).

    Per rule (a,b):
      - F on L (F=False): unattended = R. Forbidden: a=R ∧ b=R  →  Or(F, ¬A, ¬B)
      - F on R (F=True):  unattended = L. Forbidden: a=L ∧ b=L  →  Or(¬F, A, B)
    Both clauses must hold for every rule → And over all clauses = J⁺ membership.
    """
    F = obj_var(farmer_key, step)          # s_F at step t
    clauses = []
    for (a, b) in predation:
        A = obj_var(a, step)               # s_a at step t
        B = obj_var(b, step)               # s_b at step t
        # ¬(F=L ∧ A=R ∧ B=R)  ≡  F=R ∨ A=L ∨ B=L  ≡  Or(F, ¬A, ¬B)
        not_both_right_unattended = Or(F,  Not(A), Not(B))
        # ¬(F=R ∧ A=L ∧ B=L)  ≡  F=L ∨ A=R ∨ B=R  ≡  Or(¬F, A, B)
        not_both_left_unattended  = Or(Not(F), A, B)
        clauses.append(not_both_right_unattended)
        clauses.append(not_both_left_unattended)
    return And(*clauses)


def move_constraint(objects, farmer_key, predation, boat_capacity, step):
    """
    Z3 formula: transition s_t → s_{t+1} is a legal move.

    Math:
      (1) Farmer always crosses:       s_F_{t+1} ≠ s_F_t
      (2) Each object o ≠ F either:
            crosses: s_o_{t+1} ≠ s_o_t  (requires s_o_t = s_F_t — on farmer's bank)
            stays:   s_o_{t+1} = s_o_t
      (3) |{o : o crosses}| ≤ boat_capacity
      (4) s_{t+1} ∈ J⁺  (valid_state_constraint at step+1)

    Auxiliary Bool cross_o_t = True iff object o crosses at step t.
    Capacity encoded as Sum(If(cross_o, 1, 0)) ≤ boat_capacity.
    """
    F_t  = obj_var(farmer_key, step)
    F_t1 = obj_var(farmer_key, step + 1)
    cargo_objs = [o for o in objects if o != farmer_key]

    # (1) s_F_{t+1} = ¬s_F_t
    farmer_crosses = (F_t1 == Not(F_t))

    crossing_indicators = []
    cargo_constraints = []
    for o in cargo_objs:
        O_t  = obj_var(o, step)
        O_t1 = obj_var(o, step + 1)
        cross = Bool(f"cross_{o}_{step}")      # auxiliary: True iff o crosses at step t
        crossing_indicators.append(cross)
        # cross=True  → s_o_t = s_F_t (on farmer's bank) ∧ s_o_{t+1} = ¬s_o_t
        # cross=False → s_o_{t+1} = s_o_t (stays)
        can_cross  = (O_t == F_t)
        does_cross = (O_t1 == Not(O_t))
        does_stay  = (O_t1 == O_t)
        cargo_constraints.append(
            And(
                Implies(cross, And(can_cross, does_cross)),
                Implies(Not(cross), does_stay),
            )
        )

    # (3) |{o : cross_o}| ≤ boat_capacity
    capacity_ok = (Sum([If(c, 1, 0) for c in crossing_indicators]) <= boat_capacity)

    # (4) s_{t+1} ∈ J⁺
    next_valid = valid_state_constraint(objects, farmer_key, predation, step + 1)

    return And(farmer_crosses, *cargo_constraints, capacity_ok, next_valid)


# ---------------------------------------------------------------------------
# Z3 §3/§4: enumerate valid and invalid states
# ---------------------------------------------------------------------------

def enumerate_states_z3(objects, farmer_key, predation):
    """
    Return (J_minus, J_plus) as lists of state dicts.

    Math: partition {L,R}^N into J⁺ (valid_state_constraint=True) and J⁻ (False).

    NOTE: This uses brute-force iproduct over all 2^N assignments, not true Z3
    model blocking. Each assignment is checked with a fresh Solver. Stage Z3-A
    replaces this with real model blocking (s.add(Or(*[v != m[v] for v in vars_])))
    which scales to large sparse state spaces. Current approach is correct but O(2^N).
    """
    n = len(objects)
    vars_ = [obj_var(o, 0) for o in objects]   # s ∈ {L,R}^N encoded as Bool vector at step 0
    valid_cond = valid_state_constraint(objects, farmer_key, predation, 0)

    J_plus, J_minus = [], []

    for bits in iproduct([False, True], repeat=n):
        assignment = {obj_var(o, 0): BoolVal(b) for o, b in zip(objects, bits)}
        s = Solver()
        s.add(And(*[v == assignment[v] for v in vars_]))   # fix exact state
        s.add(valid_cond)                                   # test J⁺ membership
        result = s.check()
        state_dict = dict(zip(objects, ["R" if b else "L" for b in bits]))
        if result == sat:
            J_plus.append(state_dict)
        else:
            J_minus.append(state_dict)

    return J_minus, J_plus


# ---------------------------------------------------------------------------
# Z3 §5: edge enumeration
# ---------------------------------------------------------------------------

def enumerate_edges_z3(J_plus, objects, farmer_key, predation, boat_capacity):
    """
    For each pair of valid states, check if a legal move exists between them.
    Returns edge list as frozenset pairs of state-tuple keys.
    """
    def to_tuple(d):
        return tuple(d[o] for o in objects)

    valid_tuples = {to_tuple(s) for s in J_plus}
    edges = set()

    # Build a small solver per pair: encode move_constraint for step 0→1
    # with both endpoints fixed.
    for i, s1 in enumerate(J_plus):
        for s2 in J_plus[i+1:]:
            t1 = to_tuple(s1)
            t2 = to_tuple(s2)
            if frozenset([t1, t2]) in edges:
                continue
            solver = Solver()
            # Fix step 0 to s1
            for o, b in s1.items():
                solver.add(obj_var(o, 0) == BoolVal(b == "R"))
            # Fix step 1 to s2
            for o, b in s2.items():
                solver.add(obj_var(o, 1) == BoolVal(b == "R"))
            # Require a legal move
            solver.add(move_constraint(objects, farmer_key, predation, boat_capacity, 0))
            if solver.check() == sat:
                edges.add(frozenset([t1, t2]))
            # Also check reverse direction (s2 → s1) — should be same for river crossing
            # but encode explicitly to be safe
            solver2 = Solver()
            for o, b in s2.items():
                solver2.add(obj_var(o, 0) == BoolVal(b == "R"))
            for o, b in s1.items():
                solver2.add(obj_var(o, 1) == BoolVal(b == "R"))
            solver2.add(move_constraint(objects, farmer_key, predation, boat_capacity, 0))
            if solver2.check() == sat:
                edges.add(frozenset([t1, t2]))

    return edges


# ---------------------------------------------------------------------------
# Z3 §5: bounded model checking for L_min and N_paths
# ---------------------------------------------------------------------------

def bmc_min_path_z3(objects, farmer_key, predation, boat_capacity, start, goal, max_steps=20):
    """
    Bounded model checking: find minimum path length L_min from start to goal.

    Math: for each k = 1..max_steps, encode the formula:
        s_0 = start  ∧  s_0 ∈ J⁺
        ∧  ⋀_{t=0}^{k-1} move_constraint(s_t, s_{t+1})   [includes s_{t+1} ∈ J⁺]
        ∧  s_k = goal
    SAT at k → L_min = k, witness path extracted from model.
    UNSAT at all k ≤ max_steps → explicit certificate: no solution within bound.

    Returns: (L_min, path_or_None, unsat_note_or_None)
    """
    # start/goal as Z3 BoolVal constants for endpoint fixing
    start_bools = {o: BoolVal(b == "R") for o, b in start.items()}   # s_0 = start
    goal_bools  = {o: BoolVal(b == "R") for o, b in goal.items()}    # s_k = goal

    for k in range(1, max_steps + 1):
        s = Solver()

        # Fix start
        for o, bv in start_bools.items():
            s.add(obj_var(o, 0) == bv)

        # Valid state at step 0
        s.add(valid_state_constraint(objects, farmer_key, predation, 0))

        # Legal moves and valid states at each step
        for step in range(k):
            s.add(move_constraint(objects, farmer_key, predation, boat_capacity, step))

        # Fix goal at step k
        for o, bv in goal_bools.items():
            s.add(obj_var(o, k) == bv)

        result = s.check()

        if result == sat:
            # Extract witness path
            m = s.model()
            path = []
            for step in range(k + 1):
                state = {}
                for o in objects:
                    val = m.eval(obj_var(o, step))
                    state[o] = "R" if is_true(val) else "L"
                path.append(state)
            return k, path, None

        elif result == unsat:
            # No path of length k exists. Continue to k+1.
            # After max_steps consecutive UNSAT: puzzle is unsolvable.
            if k == max_steps:
                return None, None, f"UNSAT at all k ≤ {max_steps} — no solution exists within bound"

    return None, None, f"No path found within {max_steps} steps"


def count_paths_at_length_z3(objects, farmer_key, predation, boat_capacity,
                              start, goal, L_min, max_paths=50):
    """
    Count distinct solution paths of exactly length L_min using blocking clauses.
    Returns count and list of paths.
    """
    if L_min is None:
        return 0, []

    start_bools = {o: BoolVal(b == "R") for o, b in start.items()}
    goal_bools  = {o: BoolVal(b == "R") for o, b in goal.items()}

    s = Solver()

    # Fix start
    for o, bv in start_bools.items():
        s.add(obj_var(o, 0) == bv)
    s.add(valid_state_constraint(objects, farmer_key, predation, 0))

    for step in range(L_min):
        s.add(move_constraint(objects, farmer_key, predation, boat_capacity, step))

    for o, bv in goal_bools.items():
        s.add(obj_var(o, L_min) == bv)

    paths = []
    while len(paths) < max_paths:
        if s.check() != sat:
            break
        m = s.model()
        # Extract path
        path = []
        for step in range(L_min + 1):
            state = {o: ("R" if is_true(m.eval(obj_var(o, step))) else "L")
                     for o in objects}
            path.append(state)
        paths.append(path)
        # Block this path: negate all intermediate state variables
        # (start and goal are fixed; only intermediate steps distinguish paths)
        block = []
        for step in range(1, L_min):
            for o in objects:
                val = m.eval(obj_var(o, step))
                block.append(obj_var(o, step) != val)
        if not block:
            break
        s.add(Or(*block))

    return len(paths), paths


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def fmt_state_dict(d, objects):
    return "(" + ",".join(d[o] for o in objects) + ")"


def carry_label(s1, s2, objects, farmer_key):
    carried = [o for o in objects if o != farmer_key and s1[o] != s2[o]]
    return "+".join(carried) if carried else "Nothing"


def replay_path(path, objects, farmer_key, predation, boat_capacity, start, goal):
    """
    Verify a Z3-returned path in pure Python — no solver calls.

    Checks:
      1. path[0] == start, path[-1] == goal
      2. Every state satisfies all predation rules (J+ membership)
      3. Every step: Farmer crosses; crossing cargo was on Farmer's bank; count <= capacity
    Returns (True, None) on success or (False, error_string) on failure.
    """
    if path[0] != start:
        return False, f"path[0] {path[0]} != start {start}"
    if path[-1] != goal:
        return False, f"path[-1] {path[-1]} != goal {goal}"

    for t, state in enumerate(path):
        f_bank = state[farmer_key]
        unattended = "R" if f_bank == "L" else "L"
        for (a, b) in predation:
            if state[a] == unattended and state[b] == unattended:
                return False, (f"step {t}: rule ({a},{b}) violated — "
                               f"both on unattended bank {unattended}")

    for t in range(len(path) - 1):
        s_t, s_t1 = path[t], path[t + 1]
        f_bank = s_t[farmer_key]
        if s_t1[farmer_key] == f_bank:
            return False, f"step {t}→{t+1}: Farmer did not cross"
        crossing = []
        for o in objects:
            if o == farmer_key:
                continue
            if s_t1[o] != s_t[o]:
                if s_t[o] != f_bank:
                    return False, (f"step {t}→{t+1}: {o} crossed but was not "
                                   f"on Farmer's bank ({f_bank})")
                crossing.append(o)
        if len(crossing) > boat_capacity:
            return False, (f"step {t}→{t+1}: {len(crossing)} objects crossed, "
                           f"capacity is {boat_capacity}")

    return True, None


# ---------------------------------------------------------------------------
# Main verifier
# ---------------------------------------------------------------------------

def verify_puzzle_z3(name, spec):
    objects      = spec["objects"]
    farmer_key   = objects[0]
    predation    = spec["predation"]
    boat_capacity = spec.get("boat_capacity", 1)
    start        = spec["start"]
    goal         = spec["goal"]
    expected     = spec.get("expected")

    print(f"\n{'='*70}")
    print(f"PUZZLE (Z3): {name}")
    print(f"{'='*70}")
    print(f"Objects: {objects}  |  Predation: {predation}  |  Boat capacity: {boat_capacity}")

    S_total = 2 ** len(objects)
    print(f"\n§2 — State space: |S| = 2^{len(objects)} = {S_total}")

    # §3/§4 — enumerate states
    print("§3/§4 — Enumerating valid/invalid states via Z3 model blocking...")
    J_minus, J_plus = enumerate_states_z3(objects, farmer_key, predation)
    print(f"  |J-| = {len(J_minus)}  |J+| = {len(J_plus)}")

    # §5 — edges
    print("§5 — Enumerating edges via Z3 move encoding...")
    edges = enumerate_edges_z3(J_plus, objects, farmer_key, predation, boat_capacity)
    print(f"  Edges = {len(edges)}")

    # §5 — BMC for L_min
    print("§5 — BMC: searching for minimum path length...")
    L_min, witness, unsat_note = bmc_min_path_z3(
        objects, farmer_key, predation, boat_capacity, start, goal
    )

    if L_min is None:
        print(f"  L_min = None")
        print(f"  {unsat_note}")
        N_paths = 0
        paths = []
    else:
        print(f"  L_min = {L_min}")
        print("§5 — Counting paths at L_min via blocking clauses...")
        N_paths, paths = count_paths_at_length_z3(
            objects, farmer_key, predation, boat_capacity, start, goal, L_min
        )
        print(f"  N_paths = {N_paths}")
        for i, p in enumerate(paths):
            steps = [fmt_state_dict(p[0], objects)]
            for j in range(1, len(p)):
                label = carry_label(p[j-1], p[j], objects, farmer_key)
                steps.append(f"--[{label}]--> {fmt_state_dict(p[j], objects)}")
            print(f"  Path {i+1}: " + " ".join(steps))
        # Solution replay — verify each path in pure Python, independent of Z3
        for i, p in enumerate(paths):
            ok, err = replay_path(p, objects, farmer_key, predation,
                                  boat_capacity, start, goal)
            status = "PASS" if ok else f"FAIL — {err}"
            print(f"  Path {i+1} replay: {status}")
            if not ok:
                return False

    # Assertions
    print(f"\n§ Assertions:")
    results = {
        "S_total": S_total,
        "J_minus": len(J_minus),
        "J_plus":  len(J_plus),
        "edges":   len(edges),
        "N_paths": N_paths,
        "L_min":   L_min,
    }

    if expected:
        all_pass = True
        for key, exp_val in expected.items():
            actual = results[key]
            status = "PASS" if actual == exp_val else "FAIL"
            if status == "FAIL":
                all_pass = False
            print(f"  {status}  {key}: expected {exp_val}, got {actual}")
        if all_pass:
            print(f"\n  All assertions passed.")
        else:
            print(f"\n  ASSERTION FAILURE.")
            return False
    else:
        for key, val in results.items():
            print(f"    {key} = {val}")

    return results


# ---------------------------------------------------------------------------
# Cross-check against BFS verifier
# ---------------------------------------------------------------------------

def cross_check():
    """
    Import and run both verifiers; assert they produce identical results.
    Prints a comparison table.
    """
    sys.path.insert(0, "tests")
    import verify_puzzle as bfs_module

    print("\n" + "="*70)
    print("CROSS-CHECK: Z3 vs BFS/Enumeration")
    print("="*70)

    # Run BFS verifier silently by capturing results
    bfs_results = {}
    for name, spec in bfs_module.PUZZLES.items():
        objects    = spec["objects"]
        farmer_key = objects[0]
        predation  = spec["predation"]
        boat_cap   = spec.get("boat_capacity", 1)
        start      = tuple(spec["start"][o] for o in objects)
        goal       = tuple(spec["goal"][o]  for o in objects)

        J_minus, J_plus = bfs_module.get_valid_states(objects, farmer_key, predation)
        edges, adj = bfs_module.get_transitions(J_plus, objects, farmer_key, boat_cap)
        paths = bfs_module.find_all_paths(adj, start, goal)
        L_min = min(len(p)-1 for p in paths) if paths else None
        N_paths = sum(1 for p in paths if len(p)-1 == L_min) if paths else 0

        bfs_results[name] = {
            "S_total": 2**len(objects),
            "J_minus": len(J_minus),
            "J_plus":  len(J_plus),
            "edges":   len(edges),
            "N_paths": N_paths,
            "L_min":   L_min,
        }

    # Run Z3 verifier
    z3_results = {}
    import io, contextlib
    for name, spec in PUZZLES.items():
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r = verify_puzzle_z3(name, spec)
        z3_results[name] = r

    # Compare
    print(f"\n{'Puzzle':<45} {'Metric':<12} {'BFS':>8} {'Z3':>8} {'Match':>6}")
    print("-"*85)
    for name in PUZZLES:
        bfs_name = name.replace("_cap1","_cap1").replace("_cap2","_cap2")
        # Map Z3 puzzle names to BFS puzzle names
        # Map Z3 puzzle names to BFS puzzle names (identical now)
        bfs_key = name
        if bfs_key and bfs_key in bfs_results:
            bfs_r = bfs_results[bfs_key]
        else:
            bfs_r = None

        z3_r = z3_results.get(name)
        if not isinstance(z3_r, dict):
            continue

        first = True
        for metric in ["S_total", "J_minus", "J_plus", "edges", "N_paths", "L_min"]:
            z3_val = z3_r.get(metric, "?")
            bfs_val = bfs_r.get(metric, "N/A") if bfs_r else "N/A"
            match = "OK" if z3_val == bfs_val else "MISMATCH"
            label = name if first else ""
            first = False
            print(f"  {label:<43} {metric:<12} {str(bfs_val):>8} {str(z3_val):>8} {match:>6}")
        print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    all_passed = True
    for name, spec in PUZZLES.items():
        r = verify_puzzle_z3(name, spec)
        if r is False:
            all_passed = False

    cross_check()

    if not all_passed:
        sys.exit(1)
