---
title: Constraint-Graph Testbed Series — Retraction Log
description: Every retracted claim, overclaimed scope, and removed research pointer for constraint-graph_testbed puzzle exploration.
---

# Constraint-Graph Testbed Series — Retraction Log

Every retracted claim, overclaimed scope, and corrected assessment across the Constraint-Graph Testbed series. The log is the negative boundary ( $C_- $) of the series — what was probed and found absent or misformulated. It carries boundary information: what the experiment series cannot claim constrains what it can claim.

**Structural role (SIRC vocabulary):** The three (and planned four) Constraint-Graph Testbed documents are the positive boundary ( $C_+ $) — the enumerated findings, conjectures, and structural comparisons that survived audit. This log is $C_-$ — the designed mutation record. Each entry is a claim that appeared to belong in the series but was shown to be non-invariant surface: a misidentification, a formulation that applied to the wrong encoding, or a conclusion downstream of a false premise. Shedding these is P2-governed behaviour, not failure. The series documents and this log together form a complete exploration record.

**Scope:** This log covers all Constraint-Graph Testbed documents in `constraint-graph_testbed/`. It does not cover retractions to or `SIRC_principles.md` — those have their own retraction logs.

**Entry format:** ID · Source · Date · Trigger · Why retracted · Exact retracted content · What replaces it · Exploration value

---

## Index

| ID | Description | Source | Date | Trigger |
|---|---|---|---|---|
| [§R1](#r1) |  Missionaries and Cannibals (M&C) identified as gap-filler with cultural universality | Working notes (archived) — Series gap section | 2026-04-09 | Verification research — Wikipedia river crossing and M&C articles |
| [§R2](#r2) | M&C constraint structure is a hypergraph, framework extension required | Research assessment following R1 retraction | 2026-04-09 | Wikipedia graph-theoretic formulation; Alcuin number; conflict graph definition |
| [§R3](#r3) | "No valid gap-filler found" conclusion | Derived from R1 + R2 | 2026-04-09 | Retraction of R2 — named encoding produces $C_6$, directly applicable |
| [§R4](#r4) | "P1 work operates on the constraint graph" — constraint graph misidentified as P1 object | `P_3_river_crossing.md` — notation note | 2026-04-12 | Gemini audit rejoinder — "eats" edges are predation relations, not entailment relations |

---

## §R1

**Description:** M&C identified as gap-filler with cultural universality
**Source:** Working notes (archived) — Series gap section (first draft)
**Date:** 2026-04-09
**Retraction trigger:** Verification research — Wikipedia articles on river crossing puzzles and Missionaries and Cannibals

### Why retracted

The initial identification of Missionaries and Cannibals as the fourth document candidate assumed (a) that it has documented independent cross-cultural origins, and (b) that its constraint structure is a non-path graph suitable for the path-graph necessity test. Assumption (a) is false. Research confirmed that all variants — Alcuin's brothers-and-sisters (~800 AD), the jealous husbands framing (13th–15th century European transmission), and the missionaries-and-cannibals labelling (19th century) — trace to a single source: the Alcuin manuscript *Propositiones ad Acuendos Juvenes*. There are no documented independent cross-cultural origins. The cultural universality claim was imported from the river crossing puzzle family generally; it applies to Wolf-Goat-Cabbage (4+ independent origins) but not to this variant specifically.

Assumption (b) was correct — M&C does have a non-path constraint structure — but it was not sufficient to qualify M&C as a gap-filler under the stated criteria, which included cultural universality.

### Retracted content

> `Identified gap-filler: Missionaries and Cannibals (3 missionaries, 3 cannibals, 2-person boat). This is a transportation puzzle with cultural universality but a non-path constraint graph — the safety condition is an inequality (cannibals must never outnumber missionaries on either bank) rather than pair exclusion or total ordering. Its constraint graph is not a path; it is a counting constraint over group composition.`

### What replaces it

The jealous husbands puzzle (named-individual encoding of the same puzzle family) as the fourth document candidate. Under the named encoding, the constraint IS a set of pairwise unsafe pairs forming a $C_6$ cycle. Cultural universality evidence is absent — this is recorded as a scope limitation in both the memory file and the Hanoi document, not as a disqualifier for structural exploration.

### Exploration value

The retraction correctly separated two independent claims that R1 conflated: (1) the topological claim (M&C / jealous husbands has a non-path constraint graph — confirmed true) and (2) the empirical claim (cultural universality — confirmed absent). These are now held separately. The fourth document can test the topological claim without making the empirical claim. Knowing that cultural universality evidence is absent is itself informative — it is consistent with the hypothesis that $C_6$ topology does not produce a fitness peak (which would explain its absence in independent cultural transmission), or with the hypothesis that cognitive load exceeds a threshold for puzzles without a bottleneck node.

---

## §R2

**Description:** M&C constraint structure is a hypergraph; framework extension required
**Source:** Research assessment produced after R1 retraction — recorded in working notes (archived), following R1
**Date:** 2026-04-09
**Retraction trigger:** Wikipedia graph-theoretic formulation of river crossing puzzles; Alcuin number definition; named conflict graph

### Why retracted

The intermediate assessment — produced while correcting R1 — identified M&C's constraint structure as an irreducible group cardinality constraint (a hypergraph) that cannot be decomposed into named pairwise unsafe pairs. This applied to the **anonymous M&C counting formulation** (state encoded as ⟨m, c, b⟩ — missionary count, cannibal count, boat position). Under that formulation, the constraint is indeed a counting inequality over group composition, not expressible as pairwise edges between named individuals.

The error was applying this conclusion to the puzzle family as a whole, without recognising that the **jealous husbands formulation** uses named individuals: three couples (α,a), (β,b), (γ,c), with the constraint that no wife can be in the presence of a man other than her husband. Under this encoding, the unsafe pairs are explicitly named: (a,β), (a,γ), (b,α), (b,γ), (c,α), (c,β) — six pairwise edges between named individuals. These form a simple graph. The constraint is NOT a hypergraph under this encoding.

The graph-theoretic formulation of river crossing puzzles (Schwartz 1961, Csorba-Hurkens-Woeginger 2008) treats the conflict graph G = (V,E) as an undirected graph with named-object vertices and conflict edges. The jealous husbands puzzle maps directly onto this formulation. The resulting conflict graph is $C_6$ — a 6-node cycle. The SIRC DAG methodology (named objects, C⁻ as named unsafe pairs forming a simple graph) applies directly under this encoding without any extension.

### Retracted content

> `Verified non-path topology: the safety condition (cannibals must never outnumber missionaries on any bank with missionaries present) is an irreducible group cardinality constraint — a hypergraph — not decomposable into named pairwise unsafe pairs. The SIRC DAG methodology (C⁻ as named pairs forming a simple graph) requires a framework extension before it applies.`

Also retracted from `Pn_tower_of_hanoi.md`:

> `It has a confirmed non-path constraint structure (the safety condition is an irreducible group cardinality constraint — a hypergraph — not decomposable into named pairwise unsafe pairs). [...] The SIRC DAG methodology (C⁻ as named pairs) requires a framework extension before it applies to cardinality constraints.`

### What replaces it

> Under the jealous husbands named-individual encoding, the conflict graph is $C_6$ — a 6-node cycle with named unsafe pairs (a,β), (a,γ), (b,α), (b,γ), (c,α), (c,β). This is directly encodable under the existing SIRC DAG methodology. One model difference remains: in WGC-type puzzles the farmer is an exempt agent not subject to conflict constraints; in jealous husbands all agents including rowers are subject to constraints. The formal encoding section of the fourth document must handle the non-exempt-agent model explicitly — this is a methodology note, not a framework extension.

**Correct scope of the hypergraph claim:** The counting formulation (M&C with anonymous interchangeable missionaries and cannibals) is irreducibly a group constraint and cannot be encoded as named pairwise unsafe pairs. The hypergraph description is correct for that formulation. It is incorrect as a characterisation of the puzzle family, which also admits the named-individual jealous husbands encoding.

### Exploration value

The R2 retraction identified a formulation-sensitivity that is worth preserving as a finding: the same puzzle can have multiple valid encodings with different constraint graph structures depending on whether individuals are named or anonymous. The anonymous formulation (counting) produces an unanalysable constraint under the current methodology; the named formulation (jealous husbands) produces an analysable $C_6$ graph. This is a methodological observation about the SIRC DAG framework itself: the framework is formulation-dependent. A puzzle must be encoded with named individuals and pairwise relations for the methodology to apply. Whether the named encoding or the anonymous encoding is the "correct" representation of a puzzle's constraint structure is a question the series does not yet address.

---

## §R3

**Description:** "No valid gap-filler found" — gap remains open
**Source:** Derived conclusion in working notes (archived), following R1 and R2
**Date:** 2026-04-09
**Retraction trigger:** Retraction of R2 — once the jealous husbands encoding produces $C_6$ via existing methodology, the conclusion is false

### Why retracted

This conclusion was downstream of R2. The stated criteria for a valid gap-filler were: (a) documented independent cross-cultural origins, (b) non-path constraint structure encodable as named-object pairwise pairs, (c) direct applicability of the existing methodology without extension. R2's retraction established that criterion (b) and (c) are satisfied by the jealous husbands encoding. Criterion (a) was subsequently revised: cultural universality absence is recorded as a scope limitation on the fourth document, not as a disqualifier. A document that contributes to the topological claim without contributing to the cultural universality evidence base is still a valid contribution to the series. The "no valid gap-filler" conclusion was therefore false.

### Retracted content

> `What a valid gap-filler must satisfy: (a) documented independent cross-cultural origins, (b) non-path constraint structure still encodable as named-object pairwise unsafe pairs, (c) direct applicability of the existing methodology without extension. No such puzzle has been identified. The gap remains open.`

> `Status: Gap identified, no valid gap-filler found. Do not schedule M&C.`

### What replaces it

> Jealous husbands ( $C_6$ conflict graph, named-individual encoding) is the fourth document in the planned series. Status: planned, do not begin until Hanoi is complete. Cultural universality scope is limited — the fourth document contributes to the structural/topological claim only.

### Exploration value

R3's retraction clarified what "valid gap-filler" actually requires. The revised criterion — direct methodological applicability is necessary; cultural universality evidence is a scope qualifier, not a prerequisite — is more precise and reusable. A future candidate for a fifth or sixth document should be evaluated against the same criterion: can it be encoded under the existing named-object pairwise methodology? If yes, it can contribute to structural claims regardless of its cultural universality status. Cultural universality is evidence for fitness peaks; its absence is a finding about scope, not a disqualifier.

---

## §R4

**Description:** "P1 work operates on the constraint graph" — constraint graph misidentified as P1 object
**Source:** `P_3_river_crossing.md` — notation note (added 2026-04-12 during two-graph separation edit)
**Date:** 2026-04-12
**Retraction trigger:** Gemini audit rejoinder (2026-04-12) — Point 2: the constraint graph's edges are predation relations ("eats"), not entailment relations ( $\vdash$). P1's invariant is the entailment map $\Gamma \vdash C$; a graph with semantic edges does not instantiate this.

### Why retracted

The notation note was added to resolve the original Gemini audit finding: that the state-transition graph ( $\mathcal{G}_T$) was being conflated with the constraint graph. The separation was correct. But the note went further and asserted: "The $\mathsf{P1}$ work operates on the constraint graph, not $\mathcal{G}_T$."

This overclaimed. The constraint graph ( $P_3$ path: Wolf–Goat–Cabbage) is $\mathcal{R}$ — the constraint packet. It is P3's object: its nodes are transported objects, its edges are predation relations. The edges mean "eats," not "entails." P1's invariant requires the entailment map ( $\Gamma \vdash C$) — a graph whose edges represent logical consequence. The constraint graph does not qualify. Routing P1 work through the constraint graph imports the wrong edge semantics into P1's domain.

The error was produced by correctly identifying that $\mathcal{G}_T$ is not the P1-relevant object, then incorrectly concluding that the constraint graph must therefore be. A third object was needed: the entailment map. That object is not directly instantiated in these puzzles.

### Retracted content

> "The $\mathsf{P1}$ work operates on the constraint graph, not $\mathcal{G}_T$."

### What replaces it

> "The constraint graph is $\mathcal{R}$ — P3's object, the constraint packet. Its edges are predation relations ('eats'), not entailment relations ( $\vdash$). P1 contact in this document comes through inferential role identification (§12.3), not through the constraint graph's edges."

P1 contact in the series is indirect and comes through two channels:
1. **§9 — $\mathcal{R}$ logically forces certain conclusions ("Goat first and last," 7 moves minimum) regardless of which solution path a receiver finds. Both paths are witnesses to the same $\mathcal{R}$-entailed conclusions. The paths are not the entailment chain; $\mathcal{R}$ is.
2. §12.3** — the constraint-packet role (degree-2 node in $P_3$) is invariant across cultural substrates. The mechanism is P3 (same slot in the constraint packet); the question it raises is P1 (same node identity across transmissions).

### Exploration value

The retraction produced a three-way separation that was absent before:

| Object | Symbol | Belongs to | Edge type |
|---|---|---|---|
| State-transition graph | $\mathcal{G}_T$ | P3/P4 operational (enumeration) | Bidirectional physical moves |
| Constraint graph | $P_3$ path ( $\mathcal{R}$) | P3 (constraint packet) | Predation relations ("eats") |
| Entailment map | — | P1 | Logical consequence ( $\vdash$) |

The series was operating as if separating two graphs resolved the P1 question. The retraction reveals that P1 requires a third object — the entailment map — which is not directly instantiated in these puzzles. P1 contact is therefore indirect in this series: accessible through $\mathcal{R}$-forced conclusions (§9) and constraint-packet role invariance (§12.3), but not through any graph whose edges are directly present in the documents. This is a more precise description of the P1 gap and defines what a true P1 testbed would need to provide: a puzzle whose solution structure is a branching logical deduction graph, not a state-transition search.

---

## Rejected assessments

Research findings and intermediate conclusions assessed and rejected during the R1–R3 arc. Recorded here as the $C_-$ of the verification process — what was probed, found invalid, and closed.

| Assessment | Source | Why rejected |
|---|---|---|
| M&C constraint graph is K_{3,3} (complete bipartite) | Initial graph-structure inference | K_{3,3} would imply static pairwise conflict between every missionary and every cannibal. The actual constraint is group-size relative — not every pair conflicts independently. The correct named-encoding graph is $C_6$, not K_{3,3}. |
| Framework extension required for all M&C-family puzzles | R2 (retracted) | Applied only to the anonymous counting formulation. The jealous husbands named encoding requires only a methodology note (non-exempt agent), not a framework extension. |
| Cultural universality absence disqualifies M&C as gap-filler | R1 correction | Cultural universality is evidence for fitness peaks (the SIRC empirical claim). Its absence limits what the fourth document can prove, but does not prevent structural exploration. Scope limitation ≠ disqualification. |
