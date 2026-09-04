"""
Constraint-graph puzzle verifier.

Generates the formal record (§1-5) for river crossing puzzles from a pure
declarative spec: state variables, predation rules, move rule, start/goal.

No external dependencies. Run:
    python3 tests/verify_puzzle.py
"""

from itertools import product
from collections import deque, defaultdict


# ---------------------------------------------------------------------------
# Puzzle specification
# ---------------------------------------------------------------------------

PUZZLES = {
    "P3_wolf_goat_cabbage": {
        "objects": ["F", "W", "G", "C"],
        # Predation rules: each tuple (a, b) means a eats b (both on unattended bank = invalid)
        "predation": [("W", "G"), ("G", "C")],
        "boat_capacity": 1,  # max objects Farmer may carry (excluding Farmer)
        "start": {"F": "L", "W": "L", "G": "L", "C": "L"},
        "goal":  {"F": "R", "W": "R", "G": "R", "C": "R"},
        # Expected values for regression assertions
        "expected": {
            "S_total": 16,
            "J_minus": 6,
            "J_plus": 10,
            "edges": 10,
            "N_paths": 2,
            "L_min": 7,
        },
    },
    "P4_fox_chicken_caterpillar_leaf_cap1": {
        "objects": ["F", "X", "K", "T", "V"],
        "predation": [("X", "K"), ("K", "T"), ("T", "V")],
        "boat_capacity": 1,  # unsolvable — tau(P4)=2 requires capacity >= 2
        "start": {"F": "L", "X": "L", "K": "L", "T": "L", "V": "L"},
        "goal":  {"F": "R", "X": "R", "K": "R", "T": "R", "V": "R"},
        "expected": {
            "S_total": 32,
            "J_minus": 16,
            "J_plus": 16,
            "edges": 14,
            "N_paths": 0,
            "L_min": None,
        },
    },
    "P4_fox_chicken_caterpillar_leaf_cap2": {
        "objects": ["F", "X", "K", "T", "V"],
        "predation": [("X", "K"), ("K", "T"), ("T", "V")],
        "boat_capacity": 2,  # tau(P4)=2; minimum required capacity
        "start": {"F": "L", "X": "L", "K": "L", "T": "L", "V": "L"},
        "goal":  {"F": "R", "X": "R", "K": "R", "T": "R", "V": "R"},
        "expected": {
            "S_total": 32,
            "J_minus": 16,
            "J_plus": 16,
            "edges": 32,
            "N_paths": 2,
            "L_min": 3,
        },
        "ablation": [
            {"label": "Remove {Fx,Ch} (endpoint)", "remove": [("X","K")], "add": [],
             "expected": {"J_minus": 12, "J_plus": 20, "edges": 42, "N_paths": 2, "L_min": 3}},
            {"label": "Remove {Ch,Ca} (middle)", "remove": [("K","T")], "add": [],
             "expected": {"J_minus": 14, "J_plus": 18, "edges": 40, "N_paths": 4, "L_min": 3}},
            {"label": "Remove {Ca,Lf} (endpoint)", "remove": [("T","V")], "add": [],
             "expected": {"J_minus": 12, "J_plus": 20, "edges": 42, "N_paths": 2, "L_min": 3}},
            {"label": "Remove all 3 rules", "remove": [("X","K"),("K","T"),("T","V")], "add": [],
             "expected": {"J_minus": 0, "J_plus": 32, "edges": 72, "N_paths": 6, "L_min": 3}},
            {"label": "Add {Fx,Lf} (4th rule — endpoints)", "remove": [], "add": [("X","V")],
             "expected": {"J_minus": 18, "J_plus": 14, "edges": 26, "N_paths": 2, "L_min": 3}},
        ],
    },
}


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def enumerate_states(objects):
    """Return all 2^n states as tuples of ('L'|'R',) in object order."""
    return list(product(("L", "R"), repeat=len(objects)))


def state_to_dict(state, objects):
    return dict(zip(objects, state))


def is_valid(state_dict, farmer_key, predation):
    """True iff no predation rule is violated on the unattended bank."""
    farmer_bank = state_dict[farmer_key]
    unattended = {o for o, b in state_dict.items() if o != farmer_key and b != farmer_bank}
    for (a, b) in predation:
        if a in unattended and b in unattended:
            return False
    return True


def get_valid_states(objects, farmer_key, predation):
    """Return (J_minus, J_plus) as sets of state tuples."""
    all_states = enumerate_states(objects)
    J_minus, J_plus = set(), set()
    for s in all_states:
        d = state_to_dict(s, objects)
        if is_valid(d, farmer_key, predation):
            J_plus.add(s)
        else:
            J_minus.add(s)
    return J_minus, J_plus


def get_transitions(J_plus, objects, farmer_key, boat_capacity=1):
    """
    Return edge list as frozenset pairs {s1, s2} and adjacency dict.

    Move rule: Farmer always crosses. Farmer may carry up to boat_capacity
    objects that are on his bank. All other objects stay.
    """
    from itertools import combinations

    farmer_idx = objects.index(farmer_key)
    cargo_indices = [i for i, o in enumerate(objects) if o != farmer_key]

    edges = set()
    adj = defaultdict(set)

    for s in J_plus:
        s_dict = state_to_dict(s, objects)
        farmer_bank = s_dict[farmer_key]
        opposite = "R" if farmer_bank == "L" else "L"

        # Objects the Farmer could carry (on his bank)
        available = [objects[i] for i in cargo_indices if s[i] == farmer_bank]

        # Candidate cargo sets: empty (alone), or 1..boat_capacity objects
        cargo_sets = [()]
        for size in range(1, boat_capacity + 1):
            cargo_sets.extend(combinations(available, size))

        for cargo in cargo_sets:
            next_s = list(s)
            next_s[farmer_idx] = opposite
            for item in cargo:
                next_s[objects.index(item)] = opposite
            next_s = tuple(next_s)

            if next_s in J_plus:
                edge = frozenset([s, next_s])
                if edge not in edges:
                    edges.add(edge)
                    adj[s].add(next_s)
                    adj[next_s].add(s)

    return edges, adj


def find_all_paths(adj, start, goal):
    """BFS-based enumeration of all simple paths from start to goal."""
    # Returns list of paths (each path is a list of states)
    all_paths = []
    # queue: (current_state, path_so_far, visited_set)
    queue = deque([(start, [start], {start})])

    while queue:
        node, path, visited = queue.popleft()
        if node == goal:
            all_paths.append(path)
            continue
        # Prune: if already found paths and this path is longer, skip
        if all_paths and len(path) > len(all_paths[0]):
            continue
        for neighbor in adj[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], visited | {neighbor}))

    return all_paths


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def fmt_state(state, objects):
    """Format as (L,L,L,L) tuple string."""
    return "(" + ",".join(state) + ")"


def fmt_invalid_reason(state_dict, farmer_key, predation, objects):
    """Describe why a state is invalid."""
    farmer_bank = state_dict[farmer_key]
    unattended = {o for o, b in state_dict.items() if o != farmer_key and b != farmer_bank}
    reasons = []
    for (a, b) in predation:
        if a in unattended and b in unattended:
            reasons.append(f"{{{a},{b}}} present")
    return "; ".join(reasons)


def fmt_unattended(state_dict, farmer_key, objects):
    farmer_bank = state_dict[farmer_key]
    unattended = [o for o in objects if o != farmer_key and state_dict[o] != farmer_bank]
    return "{" + ",".join(unattended) + "}" if unattended else "∅"


def carry_label(s1, s2, objects, farmer_key):
    """What did the Farmer carry between two states? Returns all carried objects."""
    carried = [
        objects[i] for i in range(len(objects))
        if objects[i] != farmer_key and s1[i] != s2[i]
    ]
    return "+".join(carried) if carried else "Nothing"


def ablate(spec, remove=None, add=None, expected=None):
    """Return metrics dict for spec with predation rules modified.

    remove: list of rule tuples to drop from spec["predation"]
    add:    list of rule tuples to add to spec["predation"]
    expected: optional dict of {metric: value} assertions; raises AssertionError on failure
    Returns: {"J_minus", "J_plus", "edges", "N_paths", "L_min"}
    """
    remove = remove or []
    add = add or []
    objects = spec["objects"]
    farmer_key = objects[0]
    predation = [r for r in spec["predation"] if r not in remove] + list(add)
    start = tuple(spec["start"][o] for o in objects)
    goal  = tuple(spec["goal"][o]  for o in objects)
    boat_capacity = spec.get("boat_capacity", 1)

    J_minus, J_plus = get_valid_states(objects, farmer_key, predation)
    edges, adj = get_transitions(J_plus, objects, farmer_key, boat_capacity)
    paths = find_all_paths(adj, start, goal)
    L_min   = min(len(p) - 1 for p in paths) if paths else None
    N_paths = sum(1 for p in paths if len(p) - 1 == L_min) if paths else 0

    results = {
        "J_minus": len(J_minus),
        "J_plus":  len(J_plus),
        "edges":   len(edges),
        "N_paths": N_paths,
        "L_min":   L_min,
    }
    if expected:
        failures = []
        for key, exp_val in expected.items():
            actual = results[key]
            status = "PASS" if actual == exp_val else "FAIL"
            if status == "FAIL":
                failures.append(f"{key}: expected {exp_val}, got {actual}")
            print(f"    {status}  {key}: expected {exp_val}, got {actual}")
        if failures:
            raise AssertionError(f"ablate() failure (remove={remove}, add={add}): {failures}")
    return results


# ---------------------------------------------------------------------------
# Main verifier
# ---------------------------------------------------------------------------

def verify_puzzle(name, spec):
    objects = spec["objects"]
    farmer_key = objects[0]  # convention: first object is Farmer
    predation = spec["predation"]
    start = tuple(spec["start"][o] for o in objects)
    goal  = tuple(spec["goal"][o]  for o in objects)
    expected = spec.get("expected")

    print(f"\n{'='*70}")
    print(f"PUZZLE: {name}")
    print(f"{'='*70}")
    print(f"Objects: {objects}")
    print(f"Predation rules: {predation}")
    print(f"Start: {fmt_state(start, objects)}")
    print(f"Goal:  {fmt_state(goal, objects)}")

    # §2 — state space
    S_total = 2 ** len(objects)
    print(f"\n§2 — State space: |S| = 2^{len(objects)} = {S_total}")

    # §3 — J_minus
    J_minus, J_plus = get_valid_states(objects, farmer_key, predation)
    print(f"\n§3 — J^- (invalid states): {len(J_minus)}")
    print(f"{'State':<25} {'Unattended bank':<20} {'Why invalid'}")
    print("-" * 65)
    for s in sorted(J_minus):
        d = state_to_dict(s, objects)
        print(f"{fmt_state(s, objects):<25} {fmt_unattended(d, farmer_key, objects):<20} {fmt_invalid_reason(d, farmer_key, predation, objects)}")

    # §4 — J_plus
    print(f"\n§4 — J^+ (valid states): {len(J_plus)}")
    print(f"{'ID':<8} {'State':<25} {'Notes'}")
    print("-" * 50)
    valid_sorted = sorted(J_plus)
    state_ids = {}
    for idx, s in enumerate(valid_sorted, start=1):
        state_ids[s] = idx
    for s in valid_sorted:
        note = ""
        if s == start: note = "Start"
        elif s == goal: note = "Goal"
        print(f"  S{state_ids[s]:<5} {fmt_state(s, objects):<25} {note}")

    # §5 — transition graph
    boat_capacity = spec.get("boat_capacity", 1)
    edges, adj = get_transitions(J_plus, objects, farmer_key, boat_capacity)
    print(f"\n§5 — Transition graph: {len(edges)} edges")
    print(f"{'Edge':<8} {'States':<50} {'Farmer carries'}")
    print("-" * 70)
    for i, e in enumerate(sorted(edges, key=lambda e: sorted(state_ids[s] for s in e))):
        s1, s2 = sorted(e, key=lambda s: state_ids[s])
        print(f"  e{i+1:<5} S{state_ids[s1]} — S{state_ids[s2]}   {fmt_state(s1, objects)} — {fmt_state(s2, objects)}   carries: {carry_label(s1, s2, objects, farmer_key)}")

    # Paths
    paths = find_all_paths(adj, start, goal)
    L_min = min(len(p) - 1 for p in paths) if paths else None
    N_paths = sum(1 for p in paths if len(p) - 1 == L_min)

    print(f"\n§5 — Solution paths:")
    print(f"  N_paths (at L_min) = {N_paths}")
    print(f"  L_min (moves)      = {L_min}")
    for i, p in enumerate(paths):
        if len(p) - 1 == L_min:
            steps = [f"S{state_ids[p[0]]}"]
            for j in range(1, len(p)):
                label = carry_label(p[j-1], p[j], objects, farmer_key)
                steps.append(f"--[{label}]--> S{state_ids[p[j]]}")
            print(f"  Path {i+1}: " + " ".join(steps))

    # Regression assertions
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
            print(f"\n  All assertions passed — formal record verified.")
        else:
            print(f"\n  ASSERTION FAILURE — document inconsistency detected.")
            raise SystemExit(1)
    else:
        print("  No expected values defined — verifier output is the ground truth.")
        for key, val in results.items():
            print(f"    {key} = {val}")

    # Ablation assertions (if defined in spec)
    ablation_specs = spec.get("ablation", [])
    if ablation_specs:
        print(f"\n§ Ablation ({len(ablation_specs)} variants):")
        for row in ablation_specs:
            label = row.get("label", str(row.get("remove", [])))
            print(f"  {label}")
            ablate(spec, remove=row.get("remove", []), add=row.get("add", []),
                   expected=row.get("expected"))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    for name, spec in PUZZLES.items():
        verify_puzzle(name, spec)
