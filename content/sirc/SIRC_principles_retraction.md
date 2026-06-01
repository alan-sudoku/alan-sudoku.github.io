# SIRC Protocol Constraints — Retraction Log

Every retracted claim, overclaimed scope, and removed research pointer. The log is the negative channel ( $C_-$) of the document — what was probed and found absent. It carries boundary information: what the constraints cannot claim constrains what they can claim.

**Structural role (SIRC vocabulary):** `SIRC_principles.md` is the positive channel ( $C_+$) — the invariant content that survived audit. This log is $C_-$ — the designed mutation record. Each entry is a claim that appeared to belong to $C_+$ (a foundational constraint) but was shown to be non-invariant surface: an overclaimed formalization, a loaded term, or a scope that could not be defended. Shedding these is $\mathsf{P2}$-governed behaviour, not failure. The two documents together form a complete transmission record.

**Entry format:** ID · Source · Date · Audit trigger · Why retracted · Exact retracted content · What replaces it · Exploration value

**Entry types:**
- **§Rxx — retraction:** content removed or replaced because it was wrong. Use when a claim, scope, or pointer is false or indefensible.
- **§Axx — amendment:** underlying direction correct; exposition was imprecise. Use when a precision addition closes an attack or resolves an ambiguity without retracting the direction.

*Note: `§Cxx` is reserved for Closure content-type labels within audited source documents. It is not a retraction log entry type.*

**Name change note:** Entries dated before 2026-04-16 use the original protocol name SISC (Substrate-Independent Semantic Communication). The protocol was renamed SIRC (Substrate-Independent Reasoning Communication) on 2026-04-16; the rename is recorded in §R13. Entries from §A6 onward use SIRC. The earlier entries retain SISC as written — this is a historical record, not an error.

---

## Index

| ID | Description | Source | Date | Audit pass |
|---|---|---|---|---|
| [§R1](#r1) | DAG isomorphism mandated as $\mathsf{P1}$ invariant | § $\mathsf{P1}$ Definition item 2 | 2026-04-08 | Pass 1 — Gemini Rev 0 |
| [§R2](#r2) | DPI scope implied to cover invariant | § $\mathsf{P2}$ Grounding | 2026-04-08 | Pass 1 — Gemini Rev 0 |
| [§R3](#r3) | Braid scope constraint framed as topological only | § $\mathsf{P1}$ OQ1.1 pointer | 2026-04-08 | Pass 1 — Gemini Rev 0 |
| [§R4](#r4) | AIT/MDL implied to ground constraint/content distinction | § $\mathsf{P3}$ Grounding | 2026-04-08 | Pass 1 — Gemini Rev 0 |
| [§R5](#r5) | $\mathsf{P4}$ inverse coupling held unconditionally | § $\mathsf{P4}$ Definition | 2026-04-08 | Pass 1 — Gemini Rev 0 |
| [§R6](#r6) | Braid group pointer retained after algebraic incompatibility named | § $\mathsf{P1}$ OQ1.1 pointer | 2026-04-08 | Pass 2 — Gemini Rev 1 |
| [§R7](#r7) | Rate-Distortion Theory labeled as research pointer | § $\mathsf{P2}$ Grounding pointer | 2026-04-08 | Pass 2 — Gemini Rev 1 |
| [§R8](#r8) | "Mathematically independent" language for $\mathsf{P1}$ / $\mathsf{P2}$ | Preamble pedagogical sequence | 2026-04-08 | Pass 3 — Gemini Rev 2 |
| [§R9](#r9) | "Irreducible (engineering definition)" defense paragraph | Preamble | 2026-04-08 | Pass 3 — superseded by R10 |
| [§R10](#r10) | "Irreducible Principles" title and language throughout | Title, headers, preamble | 2026-04-08 | Pass 4 — defensive restructure |
| [§A1](#a1) | Node Identity ambiguity: "what entails it" read as edge-adjacency | § $\mathsf{P1}$ Node Identity | 2026-04-09 | Pass 5 — Gemini attack on entailment vs. isomorphism |
| [§A2](#a2) | OQ3.1 success criterion framed as uniqueness; cardinality/geometry axes unnamed | § $\mathsf{P3}$ OQ3.1 research pointer | 2026-04-15 | Pass 8 — Infinite Grid attack on OQ3.1 draft |
| [§A3](#a3) | Node Identity: labels readable as prohibited from use as reconstruction scaffolding | § $\mathsf{P1}$ Node Identity | 2026-04-15 | Pass 9 — Identity-Identifier Collapse attack |
| [§A4](#a4) | Node Identity: proof-theoretic tradition not named; model-theoretic reading not closed | § $\mathsf{P1}$ Node Identity | 2026-04-15 | Pressure Point 1 — semantic/syntactic equivocation |
| [§A5](#a5) | OQ1.2: positive and negative result conditions not specified | § $\mathsf{P1}$ OQ1.2 | 2026-04-15 | Pressure Point 3 — epistemic sharpening |
| [§R11](#r11) | Algebraic Topology (Homology) named as formal parent for SET identities | § $\mathsf{P3}$ OQ3.2 research pointer | 2026-04-12 | Pass 6 — Gemini Rubik's/invertibility audit |
| [§R12](#r12) | "Mathematical parent" label overclaims epistemic status — reads as formal SISC grounding in $S_n$ | § $\mathsf{P3}$ OQ3.2 research pointer | 2026-04-12 | Pass 7 — Gemini revision evaluation |
| [§A6](#a6) | §A4 repair reversed — proof-theoretic tradition reference removed from Node Identity | § $\mathsf{P1}$ Node Identity | 2026-04-16 | Author revision — vocabulary R10 pattern applied |
| [§R13](#r13) | "Semantic" removed from protocol name — SISC renamed SIRC | Title; all formal uses throughout document | 2026-04-16 | Author revision — § $\mathsf{P1}$ self-referential violation |
| [§A7](#a7) | OQ3.1 cardinality/geometry framing carried implicit logic-class scope assumption | § $\mathsf{P3}$ OQ3.1 cardinality/geometry pointer | 2026-04-18 | Pass 10 — Gemini re-evaluation + independent analysis |
| [§A8](#a8) | Node Identity: co-premise exception not stated; entailment map definition omits arity preservation | § $\mathsf{P1}$ Node Identity; § $\mathsf{P1}$ Definition item 1 | 2026-04-18 | Pass 11 — Arity Collapse attack on automorphism defence |
| [§A9](#a9) | §A8 justification false: co-premise fix relied on graph topology, not pure entailment map; Node Identity restated as topological identity criterion | § $\mathsf{P1}$ Node Identity (§A8 repair) | 2026-04-18 | Pass 12 — Extensionality Trap + Syntax Smuggling |
| [§A10](#a10) | "Vocabulary" in surface form clause ambiguous — logical operator types not named as invariant structural content; operator void exposes untyped graph cannot encode negation | § $\mathsf{P1}$ Definition item 3 (new); § $\mathsf{P1}$ Node Identity surface form clause | 2026-04-18 | Pass 13 — Operator Void + Tautological Collapse |
| [§A11](#a11) | $\mathsf{P3}$ "boundary conditions of a thought" ambiguous — domain grounding not explicitly excluded; misreading invites Semantic Void attack | § $\mathsf{P3}$ opening definition sentence | 2026-04-18 | Pass 14 — Semantic Void; valid kernel of rejected critique |
| [§A12](#a12) | Defense argument false: "structural role constraints rule out sourdough starter" — formal constraints cannot distinguish domain-isomorphic models; concession made explicit | Rejected critique record (Semantic Void); §A11 exploration value | 2026-04-18 | Pass 15 — Model-Theoretic Isomorphism attack |
| [§A13](#a13) | $\mathsf{P4}$ Definition omits verification-cost dimension — inverse coupling correct for receiver search cost under targeted reconstruction; breaks when verification cost dominates (Pure Formalism / any-valid-instantiation case) | § $\mathsf{P4}$ Definition; § $\mathsf{P4}$ OQ4.1 | 2026-04-18 | Pass 17 — § $\mathsf{P4}$ Inversion Paradox / CSP Collapse; partial hold |
| [§A14](#a14) | §A11 overcorrected — "domain content is not encoded" is false; correct claim is domain content is not *required* (not § $\mathsf{P1}$invariant); sender may include domain guidance as optional Layer 2 content; this resolves the § $\mathsf{P1}$validity vs. communication gap | § $\mathsf{P3}$ opening definition; § $\mathsf{P3}$ Definition; § $\mathsf{P2}$ OQ2.1 | 2026-04-18 | Author self-correction — user-identified gap in §A11 logic |
| [§A15](#a15) | $\mathsf{P4}$ omits cooperativity assumption for Layer 2 (soft guidance, not hard constraint; § $\mathsf{P1}$ permits discard) and phase transition regime restriction (inverse coupling holds over-constrained only; under-constrained coupling is direct) | § $\mathsf{P4}$ Definition; § $\mathsf{P4}$ OQ4.1 | 2026-04-18 | Pass 18 — Layer 2 Epistemic Contradiction / § $\mathsf{P1}$ Loophole; sub-arguments 2–3 partially hold |
| [§A16](#a16) | $\mathsf{P1}$ Node Identity two-level distinction not explicit enough to foreclose distance-metric misreading of "topological position"; operator type equivalence not stated as functional/truth-table criterion | § $\mathsf{P1}$ Node Identity; § $\mathsf{P1}$ Definition item 3 | 2026-04-18 | Pass 20 — Topological Identity Contradiction; precision additions only |

---

## §R1

**Description:** DAG isomorphism mandated as $\mathsf{P1}$ invariant
**Source:** § $\mathsf{P1}$ Definition, item 2
**Date:** 2026-04-08
**Retraction trigger:** Pass 1 — Gemini Revision 0 audit

### Why retracted

$\mathsf{P1}$'s Definition mandated DAG isomorphism as the invariant structural property while OQ1.1 simultaneously admitted the isomorphism question is unresolved. These cannot coexist: you cannot mandate a formalization as the invariant definition while the OQ acknowledges that the correct formalization is unknown. The stronger claim — structural isomorphism required — was retracted in favour of the weaker claim — entailment equivalence required — which the Grounding (consequence relation preservation) actually supports.

### Retracted content

> `2. **Dependency structure** — the isomorphism class of the directed acyclic graph of inferential dependencies: which conclusions depend on which premises.`

### What replaces it

> `2. **Entailment equivalence** — the consequence relation is preserved under structural variation: two dependency structures satisfy $\mathsf{P1}$ if they entail the same conclusions from the same premises, regardless of whether they are isomorphic. DAG isomorphism is a sufficient condition for $\mathsf{P1}$ validity, not the definition of the invariant. OQ1.1 characterises when structural isomorphism is required beyond entailment equivalence.`

**Implication now false:** That a receiver reconstructing `A ⊢ C ⊢ B` when the sender used `A ⊢ B` constitutes a $\mathsf{P1}$ failure. Under the repair this is a $\mathsf{P1}$-valid transmission — same entailment, different dependency path.

**Searchable marker:** Any document citing $\mathsf{P1}$ as requiring DAG isomorphism as the invariant definition is citing the pre-2026-04-08 state. The current standard is entailment equivalence.

### Exploration value

DAG isomorphism is the correct formalization candidate for the dependency structure invariant when structural isomorphism is required. The retraction did not destroy this direction — it correctly opened OQ1.1: under what conditions is entailment equivalence sufficient, and under what conditions is structural isomorphism additionally required? That is a richer and more precise research question than the retracted claim allowed.

---

## §R2

**Description:** DPI scope implied to cover the $\mathsf{P1}$ invariant
**Source:** § $\mathsf{P2}$ Grounding
**Date:** 2026-04-08
**Retraction trigger:** Pass 1 — Gemini Revision 0 audit

### Why retracted

The prior text stated that "a finite encoding cannot be a sufficient statistic for the sender's full activation state" and "strict loss follows from the substrate mismatch, not from the DPI alone." The document correctly noted that DPI alone wasn't sufficient — but the surrounding framing allowed a reading where DPI grounded the claim that the $\mathsf{P1}$ invariant is also at risk during transmission. That reading is incorrect. DPI proves loss of the full continuous activation state. If the invariant is a finite logical structure, DPI says nothing about whether it suffers loss. The implicit overclaim was retracted by making the scope boundary explicit.

### Retracted content

Implicit — no text was removed. The prior framing allowed the reading:

> *DPI establishes that loss exists, including loss of the invariant.*

That reading is false.

### What replaces it

An added sentence making the scope explicit:

> `DPI applies to the full activation state, not the invariant alone. The claim that invariant content is also at risk follows from substrate mismatch (OQ2.1), not from DPI directly.`

### Exploration value

The retraction correctly scoped the two arguments: DPI establishes the floor (full-state loss unavoidable); substrate mismatch is the separate argument for why the invariant is also exposed. These are now independent claims that can be attacked or supported independently. OQ2.1 is the correct location for the empirical question about invariant degradation — DPI cannot settle it.

---

## §R3

**Description:** Braid scope constraint framed as topological observation without naming algebraic source
**Source:** § $\mathsf{P1}$ OQ1.1 research pointer
**Date:** 2026-04-08
**Retraction trigger:** Pass 1 — Gemini Revision 0 audit
**Note:** R3 was an intermediate repair. The pointer was subsequently removed entirely by R6. R3's contribution was naming the algebraic source, which confirmed the pointer was unretainable.

### Why retracted

The braid groups pointer noted that "braid strands cannot topologically merge — unlike DAG vertices, where multiple premises combine into a single conclusion" and used this as a scope constraint limiting braids to linear sub-paths. The constraint was stated as a topological observation without explaining why it exists. A scope constraint stated as observed but not explained is fragile: a future reader can interpret it as contingent (braid diagrams could be extended) rather than principled. Naming the algebraic source makes the constraint unconditional.

### Retracted content

> *Topological scope constraint: braid strands cannot topologically merge — unlike DAG vertices, where multiple premises combine into a single conclusion.*

(Presented as the primary reason for the scope limit, without the algebraic root.)

### What replaces it

An added sentence preceding the topological note:

> `Algebraic constraint: braid groups are groups — every element has an inverse braid. Directed inference is irreversible: A ⊢ B does not imply B ⊢ A. This algebraic incompatibility is the source of the scope constraint below, not a topological coincidence.`

**Subsequent finding (R6):** Naming the algebraic incompatibility revealed that the scope constraint does not salvage the pointer — linear inference chains are equally irreversible, and the pointer was removed entirely in Pass 2.

### Exploration value

R3's repair correctly named why braid groups fail. That naming was the necessary step before R6's removal — without it, the removal could have been read as a topological judgment rather than an algebraic one. The algebraic incompatibility is now a permanent closed direction: no scope constraint on braid groups can overcome the invertibility requirement. Future proposals for representing dependency sub-structures need a mathematical parent that is directed and irreversible from the ground up.

---

## §R4

**Description:** AIT/MDL implied to ground the constraint/content distinction
**Source:** § $\mathsf{P3}$ Grounding
**Date:** 2026-04-08
**Retraction trigger:** Pass 1 — Gemini Revision 0 audit

### Why retracted

The prior Grounding listed AIT and Optimisation Theory together as if jointly supporting $\mathsf{P3}$. The MDL sentence — "the shortest sufficient description of a solution space is a valid representation of it" — implied that MDL supports the constraint/content distinction. It does not. In AIT, a program is a string that generates another string. The concept of "boundary conditions vs. content" is not native to AIT — it belongs to constraint satisfaction and optimisation theory. The joint listing implied a unified grounding that did not exist.

### Retracted content

> `- **Algorithmic information theory** — Kolmogorov complexity: the minimum description length of an object is well-defined. The MDL principle: the shortest sufficient description of a solution space is a valid representation of it.`
>
> `- **Optimisation theory** — boundary conditions on a feasible set are a standard compact representation of a solution space. The set of solutions consistent with a constraint system is fully determined by those constraints.`

(The joint listing implied AIT supported the constraint/content distinction.)

### What replaces it

> `- **Algorithmic information theory** — Kolmogorov complexity: the minimum description length of an object is well-defined. MDL establishes that a minimum sufficient description exists; it does not distinguish boundary conditions from content — in AIT, both are programs that generate strings. AIT grounds $\mathsf{P3}$'s claim that a minimum description exists; it does not ground the constraint/content distinction.`
>
> `- **Optimisation theory** — the constraint/content distinction is grounded here, not in AIT. Boundary conditions on a feasible set are a standard compact representation of a solution space. The set of solutions consistent with a constraint system is fully determined by those constraints. $\mathsf{P3}$ applies AIT (minimum description exists) and Optimisation Theory (boundary conditions are the correct encoding type) as independent supports for different parts of the principle.`

### Exploration value

The separation makes $\mathsf{P3}$'s grounding more robust: each field is only asked to prove what it can actually prove. AIT's claim (a minimum description exists) survives independently of whether the constraint/content distinction holds. Optimisation Theory's claim (boundary conditions are sufficient to define a solution space) survives independently of whether a minimum description is achievable. An attack on either grounding now leaves the other intact.

---

## §R5

**Description:** $\mathsf{P4}$ inverse coupling held unconditionally across all channel configurations
**Source:** § $\mathsf{P4}$ Definition
**Date:** 2026-04-08
**Retraction trigger:** Pass 1 — Gemini Revision 0 audit

### Why retracted

$\mathsf{P4}$ states that sender and receiver work is inversely coupled. This was stated without naming the channel capacity assumption the coupling depends on. In an unconstrained channel where the sender can transmit the full reasoning structure at zero cost, both sender and receiver work scale at $O(N)$ and the inverse coupling does not apply. $\mathsf{P4}$ implicitly assumed constrained channel capacity. A tradeoff curve requires both ends to be constrained — if one cost is zero, the curve collapses. Leaving the assumption implicit allowed $\mathsf{P4}$ to read as a universal complexity principle rather than a constraint that applies under realistic transmission conditions.

### Retracted content

Implicit — no text was removed. The prior framing allowed the reading:

> *The inverse coupling holds in all channel configurations.*

That reading is false.

### What replaces it

An added sentence making the assumption explicit:

> `$\mathsf{P4}$ additionally assumes constrained channel capacity. In an unconstrained channel where the sender can transmit the full reasoning structure at zero cost, both sender and receiver work scale at $O(N)$ and the inverse coupling does not apply. $\mathsf{P4}$ characterises the design space under realistic transmission constraints.`

### Exploration value

Making the assumption explicit makes $\mathsf{P4}$ falsifiable within its scope: if a deployment context provides effectively unconstrained channel capacity, $\mathsf{P4}$'s tradeoff curve collapses and a different design analysis applies. This is not a weakness — it is the condition under which $\mathsf{P4}$ would be overridden. Knowing when a constraint does not apply is as useful as knowing when it does.

---

## §R6

**Description:** Braid group pointer retained after algebraic incompatibility named
**Source:** § $\mathsf{P1}$ OQ1.1 research pointer
**Date:** 2026-04-08
**Retraction trigger:** Pass 2 — Gemini Revision 1 audit

### Why retracted

R3 correctly named the algebraic incompatibility (braid groups require invertibility; directed inference is irreversible) as the source of the scope constraint, then retained the pointer scoped to linear sub-paths. This retention was incoherent: linear inference chains ( $A \vdash B \vdash C$) are equally irreversible. The algebraic incompatibility applies everywhere in the domain, not only where branching occurs. A pointer that names why it cannot work and then proposes a limited scope where it supposedly can is self-contradictory. Removal is the only consistent action once the incompatibility is named as unconditional.

### Retracted content

> *Research pointer: braid groups have a natural source-to-target directionality that maps onto DAG inferential structure more directly than closed topological invariants. Whether braid-theoretic representations of dependency graphs produce better-behaved invariants under this definition is an open direction. Algebraic constraint: braid groups are groups — every element has an inverse braid. Directed inference is irreversible: A ⊢ B does not imply B ⊢ A. This algebraic incompatibility is the source of the scope constraint below, not a topological coincidence. Topological scope constraint: braid strands cannot topologically merge — unlike DAG vertices, where multiple premises combine into a single conclusion. This constraint is a consequence of where braid groups sit in the mathematical hierarchy: Symmetric groups (Sn, OQ3.2) are static with no direction; braid groups add directionality but not merging; DAGs ( $\mathsf{P1}$) add both direction and merging. Braids are therefore the correct tool for the sequential non-branching sub-structures of a reasoning DAG, and out of scope for the full inferential structure. Braid-theoretic representations are strictly limited to analysing these linear sub-paths; any application to OQ1.1 must be scoped accordingly.*

### What replaces it

Nothing. OQ1.1 stands without a research pointer. The question of which formalization captures the dependency structure invariant remains open; braid groups are a permanently closed direction.

**Note on Theory §4.2:** Topological Braiding in the Theory was already marked as a conceptual constraint with no established bridge. That status is correct and unchanged. This retraction is Principles-only.

### Exploration value

The mathematical hierarchy note (Symmetric groups → braid groups → DAGs) was a correct observation about where braid groups sit relative to the target. It showed that braid groups are not useless as mathematics — they occupy a real position in the algebraic hierarchy. The value it generated: any valid candidate for representing dependency structure must support both directionality AND merging, which eliminates braid groups and Symmetric groups as candidates and narrows the search to structures that natively support convergent directed edges. DAGs themselves are the correct mathematical parent; the open question is how to define a stable invariant over them, not how to embed them in a different algebraic structure.

---

## §R7

**Description:** Rate-Distortion Theory labeled as a current research pointer
**Source:** § $\mathsf{P2}$ Grounding — Rate-Distortion pointer
**Date:** 2026-04-08
**Retraction trigger:** Pass 2 — Gemini Revision 1 audit

### Why retracted

Rate-Distortion Theory requires a strictly defined quantitative distortion metric $d(x, \hat{x})$ over a measurable space. The pointer mapped "Distortion" to semantic surface mutation (the Achilles/Susanoo divergence) — which is not a defined distortion metric. The prior label "Research pointer" and the phrase "this mapping creates an explicit mathematical bridge" implied the formal bridge exists. It does not. "Structural analogy pointing toward a formalization target" and "current application of Rate-Distortion Theory" are different epistemic statuses; the pointer used the wrong one.

### Retracted content

> *Research pointer: Rate-Distortion Theory (Shannon, 1959) characterises the tradeoff space above that floor — the minimum transmission rate required to reconstruct a source within a given distortion bound. Mapped to SISC: Rate corresponds to the strictness and size of the $\mathsf{P3}$ Constraint Packet; Distortion corresponds to the $\mathsf{P2}$ designed semantic mutation — the Achilles/Susanoo divergence. This mapping creates an explicit mathematical bridge between $\mathsf{P2}$ and $\mathsf{P3}$: tighter constraint packets (higher Rate) produce lower semantic distortion; looser packets (lower Rate) permit greater surface mutation. Rate-Distortion Theory is an addition to DPI, not a replacement — DPI establishes that loss exists; Rate-Distortion characterises how much loss is acceptable at a given transmission cost.*

### What replaces it

> *Structural analogy (not a current application): Rate-Distortion Theory (Shannon, 1959) characterises the tradeoff space above that floor — the minimum transmission rate required to reconstruct a source within a given distortion bound. The structural mapping to SISC is visible: Rate corresponds to constraint packet strictness; Distortion corresponds to semantic surface mutation. This analogy becomes a formal bridge only if a quantitative distortion metric over semantic content is defined — which SISC does not currently provide. Rate-Distortion Theory is a candidate formal framework for OQ2.1, not a current grounding. DPI establishes that loss exists; Rate-Distortion is where that formalization should eventually land.*

**Condition for promotion back to research pointer:** A quantitative semantic distance metric defined over the surface-content mutation space (OQ2.1). Once that metric exists, Rate-Distortion Theory applies directly.

### Exploration value

The structural analogy is real and identifies the correct formalization target. Rate-Distortion Theory is not a dead end — it is the candidate framework once the missing component (semantic distance metric) is defined. The retraction correctly names what is required for the bridge to exist, which is more useful than either claiming the bridge exists or abandoning the direction entirely.

---

## §R8

**Description:** "Mathematically independent" language for $\mathsf{P1}$ / $\mathsf{P2}$ coupling
**Source:** Preamble — pedagogical sequence paragraph
**Date:** 2026-04-08
**Retraction trigger:** Pass 3 — Gemini Revision 2 audit

### Why retracted

"Mathematically independent (different fields)" is ambiguous. It can be read as "not derivable from each other" (the correct and defensible claim) or "no shared vocabulary or definitional dependency" (a stronger claim the document cannot make, since $\mathsf{P2}$'s application uses the invariant $I$ defined by $\mathsf{P1}$). The functional dependency is real and was already conceded in the same sentence ("they interact functionally"). The surrounding "mathematically independent" language created a tension between the concession and the claim — asserting independence while simultaneously demonstrating coupling. The repair replaces the ambiguous phrase with a statement that names exactly what is and is not independent.

### Retracted content

> `$\mathsf{P1}$ and $\mathsf{P2}$ are mathematically independent (different fields); they interact functionally: $\mathsf{P1}$ defines the invariant that $\mathsf{P2}$'s loss is measured against.`

### What replaces it

> `$\mathsf{P1}$ and $\mathsf{P2}$ are non-derivable from each other: DPI holds without reference to any consequence relation; the logical equivalence criterion holds without reference to any information channel. They interact in application: $\mathsf{P1}$ defines the invariant; $\mathsf{P2}$ characterises why the system must target invariant preservation rather than full fidelity. Application-level coupling is not logical derivation.`

### Exploration value

The repair demonstrates the correct precision for independence claims in protocol specifications: state what is non-derivable (the theorems in their home fields) and separately state how they interact in application. This pattern is reusable: any two constraints in this set that share application vocabulary can be described as non-derivable while functionally coupled, without contradiction.

---

## §R9

**Description:** "Irreducible (engineering definition)" defense paragraph
**Source:** Preamble
**Date:** 2026-04-08
**Retraction trigger:** Pass 3 — Gemini Revision 2 — superseded by R10 in same pass

### Why retracted

R9 added a paragraph defining "irreducible" in engineering terms to defend the word against its axiomatic mathematics reading. R10 removed the word from the document entirely. A paragraph defending a contested term is load the document should not carry — defending the term keeps the fight on the attacker's terrain. R10's approach (remove the term; let the attacker engage the constraints directly) is more effective. R9's content (each constraint is necessary; none derivable from the others) was preserved in the Categorical scope paragraph without the contested label.

### Retracted content

> `**Irreducible (engineering definition):** No principle in this set is derivable from the others, and removing any one loses an independent dimension of the transmission problem — validity, limits, encoding, and cost are each necessary and none subsumes another. This is the engineering usage: a design cannot escape this constraint. It is not the axiomatic mathematics usage, where "irreducible" denotes a non-derivable primitive of a new formal system. The principles apply known mathematics to a novel domain; originality is in the application.`

### What replaces it

Content absorbed into Categorical scope:

> `Each constraint is necessary — removing any one loses an independent dimension of the transmission problem. None is derivable from the others.`

### Exploration value

R9 was the correct intermediate step — it identified what "irreducible" needed to mean to be defensible. That identification made R10 possible: once the engineering meaning was articulated clearly, it became obvious the meaning could be stated without the contested word. The defense paragraph was the probe; R10 was the retraction of the term it was defending.

---

## §R10

**Description:** "Irreducible Principles" title and language throughout
**Source:** Title; "Principles at a Glance" header; "Each principle follows" preamble
**Date:** 2026-04-08
**Retraction trigger:** Pass 4 — author defensive restructure following Gemini Revision 2

### Why retracted

"Irreducible" carries a specific meaning in formal axiomatic systems: a non-derivable primitive of a new mathematical theory. The document's body consistently claimed something accurate and different — novel application of known mathematics — but the title set expectations the content did not match. Rather than defend the term (R9's approach), the term was removed. "Protocol Constraints" is SISC-native vocabulary: a boundary condition the protocol cannot cross, in the same register as Constraint Packet ( $\mathsf{P3}$). A SISC-native term has no prior definition available to import; the attacker must engage the constraints directly.

### Retracted content

> Title: `# Substrate-Independent Semantic Communication (SISC)— Irreducible Principles`

> Header: `## Principles at a Glance`

> Preamble: `Each principle follows the same structure:`

### What replaces it

> Title: `# Substrate-Independent Semantic Communication (SISC) — Protocol Constraints`

> Header: `## Constraints at a Glance`

> Preamble: `Each constraint follows the same structure:`

**What this does not concede:** The four constraints are still necessary and non-redundant. The content is unchanged. The change is purely terminological.

### Exploration value

The retraction demonstrates a general defensive principle: when a contested term is borrowed from another domain, the correct response is removal rather than redefinition. Redefinition keeps the dispute alive by accepting the attacker's frame. Removal forces engagement with the substance. Any SISC document using borrowed terminology that carries external definitional baggage should prefer SISC-native alternatives wherever they exist.

---

## Rejected critiques

Gemini critiques assessed and rejected across all four audit passes. Recorded here as the $C_-$ of the audit process — what was probed, found invalid, and closed.

| Critique | Source | Why rejected |
|---|---|---|
| $\mathsf{P1}$ is a tautology (classical logical equivalence) | Rev 1, Rev 2, Rev 3 | Novelty is in application to cross-substrate neural transmission, explicitly stated from the first line. Applying a known criterion to a domain where it was not previously operationalised is not trivial. |
| $\mathsf{P2}$ is hollow / only an empirical observation | Rev 1, Rev 2, Rev 3 | $\mathsf{P2}$ is a design directive: do not attempt losslessness; target invariant preservation. A system designer ignoring $\mathsf{P2}$ would rationally attempt full-fidelity encoding. $\mathsf{P2}$ closes that path. |
| $\mathsf{P1}$→$\mathsf{P2}$ logical derivation dependency | Rev 2 | Conflates application-level coupling with logical derivation. DPI is provable without any consequence relation. The consequence relation is provable without any information channel. Non-derivability and shared application vocabulary are compatible. |
| Dead end as unified mathematical theory | Rev 0, Rev 1 | Applied only if method-level pointers are read as foundational claims. The document explicitly states originality is in the application, not the mathematics. |
| Motte-and-Bailey fallacy | Rev 2 | Misclassified. Motte-and-Bailey requires strategic shifting between positions under pressure. The document's body stated the same position throughout. The valid kernel — title/body presentation gap — was addressed by R10 (term removal), not by shifting position. |
| $\mathsf{P1}$ / $\mathsf{P2}$ are requirements not mechanics; document is top-heavy | Rev 3 | Fair typological observation about role differentiation; not a structural attack. $\mathsf{P1}$ and $\mathsf{P2}$ are prescriptive constraints that close off design alternatives (full fidelity, structural isomorphism), not merely descriptive requirements. Accepted as a documentation note, not a retraction trigger. |
| Node Identity secretly forces isomorphism ("back door" attack) | Pass 5 | Conflates dependency path with inferential role. If $A \vdash B$ holds in both structures, $B$'s position in the entailment map is unchanged regardless of intermediate step $C$. Attack lands on a genuine ambiguity in exposition (C1); the underlying claim is correct. |
| Inferential role is an unverifiable projection onto neural substrates | Pass 5 | This is OQ1.2, already open. The attack addresses a claim the document does not make. Principles define the invariant mathematically; extractability is deferred as an empirical question. |
| $\mathsf{P3}$ forces the sender to provide intermediate steps (isomorphic structure) to be tractable | Pass 5 | Correct observation about the design space; misfires as a $\mathsf{P1}$ contradiction. This is $\mathsf{P4}$ operating correctly — the sender may choose a higher point on the trade-off curve, approaching fuller specification. That is a design choice, not a collapse of entailment equivalence. |
| OQ1.1 (braid rejection for invertibility) and OQ3.2 (Symmetric Group $S_n$) are contradictory — the system rejects invertibility in one OQ and invokes an invertible structure in another | Pass 6 | Framework import. OQ1.1 and OQ3.2 are separate open questions exploring separate directions — the principles do not commit to a single algebraic parent across all OQs. The auditor imports the assumption that the theory must be globally consistent within one algebraic structure. OQ3.2's Sudoku pointer is an analogy (survival criterion 6: motivation, not mechanism grounding); treating it as a formal algebraic commitment is a misreading of epistemic status. The invertibility objection is valid against a formal commitment; it does not land against a motivating analogy. |
| Repair: replace Symmetric Group $S_n$ with Semigroups or Monoids to model non-invertible directed operations | Pass 6 | Framework import (attack category: over-specification). Prescribes a specific algebraic structure where the principles currently point at an intuition. The correct action at OQ3.2 is to leave the open direction open, not to anchor it to a specific non-invertible algebraic parent. If Semigroups or Monoids are eventually validated as the correct formalization, that is a theory-level research outcome — not a principles-level commitment. |
| $\mathsf{P1}$ and $\mathsf{P3}$ cannot coexist — boundary conditions cannot force unique reconstruction in open domains ("Infinite Grid") | Pass 8 | Imports a uniqueness requirement that neither $\mathsf{P1}$ nor $\mathsf{P3}$ makes. $\mathsf{P1}$ requires reconstruction to preserve the entailment map, not to be unique. $\mathsf{P3}$ requires the encoding type to be boundary conditions, not that those conditions force one solution. The § $\mathsf{P1}$equivalent set may contain multiple valid reconstructions; boundary conditions succeed if they constrain reconstruction to that set. Uniqueness is a special case at the fully over-determined end of the $\mathsf{P4}$ trade-off curve, not a general requirement. |
| Bootstrap Paradox — "positions in the entailment map" presupposes a coordinate system the constraints are supposed to create (circular) | Pass 8 | Imports a Cartesian model (positions exist prior to objects) onto a relational model (positions are constituted by relations). $\mathsf{P1}$'s node identity is explicitly relational: a node's position in the entailment map is the set of entailment relations in which it participates. Transmitting a constraint $\Gamma \vdash C$ simultaneously specifies the required relation and partially identifies the nodes by their required inferential roles. Constraints and their referents are co-constituted. This is holistic, not circular — the same structure as relational definitions throughout graph theory and model theory. |
| Infinite Basis Problem — optimization theory requires a fixed finite basis; open-domain reasoning has no finite variable set, so $\mathsf{P3}$'s feasible-set grounding is incoherent | Pass 8 | False premise. The requirement of a finite basis is specific to linear programming on finite-dimensional vector spaces, not to optimization theory generally. More importantly, $\mathsf{P3}$'s variable space is not "all propositions in the universe" but consequence relations over the sender's specific reasoning structure — a finite object. MDL's existence guarantee applies to this finite target. Optimization over infinite-dimensional spaces is a mature field; the attack mistakes a subfield constraint for a parent-theory requirement. |
| Tautological Shield — OQ3.2 makes the protocol unfalsifiable: it works for receivers who can make it work | Pass 8 | Conflates validity condition with achievability condition. $\mathsf{P1}$ defines what a valid transmission is (entailment-map preservation) — this is the protocol's success criterion, independently defined. OQ3.2 asks what receiver capacity is required for that success to be achievable — a separate and open empirical question. The protocol is falsifiable: a transmission where the receiver's reconstruction does not preserve the entailment map is a $\mathsf{P1}$ failure, regardless of receiver capacity. OQ3.2 failure (insufficient capacity) and $\mathsf{P3}$ failure (wrong encoding type) are distinct failure modes, now explicitly named in the OQ3.1 cardinality-and-geometry research pointer. |
| Identity-Identifier Collapse — "surface form" label designation means the receiver has no invariant identifier to link constraints during reconstruction | Pass 9 | Conflates two distinct functions of labels: (1) identity criterion — inferential role, not label (correct, $\mathsf{P1}$'s definition); (2) provisional coordination handle — labels can and do serve this function during reconstruction. $\mathsf{P1}$ prohibits treating label agreement as sufficient for identity; it does not prohibit using labels as reconstruction scaffolding. Final node identity is established by inferential role once the full entailment map is assembled. Nomenclature mismatch (same label, different inferential roles) is already a $\mathsf{P1}$ failure. Addressed by clarification in Node Identity section. |
| Unknown N — receiver starts blank, so § $\mathsf{P3}$'s optimization has no defined variable space | Pass 9 | Assumes a blank receiver substrate; $\mathsf{P3}$ does not. $\mathsf{P3}$ states reconstruction occurs "from the receiver's own capacity." Constraint packets co-define their variable space through the constraints themselves (standard CSP — variables are introduced by rules, not by a pre-declared schema). The receiver's existing reasoning structure is the background space; transmitted constraints narrow what is produced within it. The blank-receiver premise is the attack's own, not a claim in the document. |
| Ghost Constraint — separating § $\mathsf{P3}$ (encoding type) from OQ3.2 (capacity) makes § $\mathsf{P3}$ vacuous: any data is § $\mathsf{P3}$compliant | Pass 9 | Accurate description of $\mathsf{P3}$'s scope, not a new flaw. $\mathsf{P3}$'s Definition already states packets range from minimum sufficient to fully over-determined, and that below the minimum the receiver's search space is too large for reliable reconstruction. Sufficiency is OQ3.1's domain. $\mathsf{P3}$ defines encoding type; the four constraints together define the complete design space. Presenting the document's own stated scope as a newly exposed failure misreads the architecture. |
| "Operationally Vacuous" meta-verdict — the protocol moved from logically non-feasible to formally vacuous: always correct, never necessarily working | Pass 8 summary | Meta-verdict rests entirely on the uniqueness-requirement premise already rejected in the same pass (Infinite Grid). $\mathsf{P3}$'s Definition explicitly states packets range from minimum sufficient to fully over-determined — the protocol's own text names the "never working" condition as below-minimum encoding, not as a structural feature. The verdict does not survive its own constituent attack rejections. |
| DPI and Kolmogorov Complexity laundered — DPI conflated with prescriptive mechanics; MDL conflated with constraint/content distinction | Gemini re-evaluation 2026-04-18, Point 1 | Defended. § $\mathsf{P2}$ explicitly decouples DPI from what is lost: "DPI establishes the existence of loss — the floor... The claim that invariant content is also at risk follows from substrate mismatch (OQ2.1), not from DPI directly." § $\mathsf{P3}$ explicitly separates AIT's existence proof from the constraint/content distinction, grounding the latter in Optimisation Theory. Both decouplings are stated in the document, not asserted post-attack. |
| Incomputability and intractability — protocol mandates uncomputable operations (MDL, entailment equivalence verification) | Gemini re-evaluation 2026-04-18, Point 2 | Defended. The protocol does not mandate these as solved operational steps. OQ3.1 explicitly concedes MDL uncomputability: "the existence of such a minimum follows from MDL; the procedure for finding it does not." OQ1.3 explicitly leaves verification cost uncharacterised. Both are flagged as open questions, not claimed as solved. |
| Entailment vs. structure equivocation — protocol reduces entailment to uninterpreted syntactic structure and graph isomorphism | Gemini re-evaluation 2026-04-18, Point 3 | Defended by design scope. The protocol explicitly bites the bullet: node identity is protocol-internal and does not invoke any tradition of semantics. The protocol transmits a formal system; whether that counts as "entailment" in a model-theoretic sense is outside $\mathsf{P1}$'s stated scope. Demanding model-theoretic grounding imports a requirement the document structurally disavows. |
| Analogy scope and unfalsifiability — Phistomefel Ring imports finite group theory into general DAGs; $\mathsf{P3}$ vs OQ3.2 separation is a tautological shield; OQ1.2 uses moving goalposts | Gemini re-evaluation 2026-04-18, Point 5 | Defended. The Ring analogy is conditioned: "if reasoning DAGs have identifiable partition boundaries." OQ3.2 separation is standard Information Theory (existence of code vs. decoder complexity). OQ1.2 explicitly states what a negative result would mean — $\mathsf{P1}$ scope revision — which is a falsification condition, not a goalpost. All three sub-attacks misread epistemic-status labels as evasion. |
| Disjunctive Collapse — two symmetric premises $\{A\} \vdash X$, $\{B\} \vdash X$ collapse to $\{N\} \vdash X$, destroying proof-path multiplicity | Pass 12 — Gemini §A8 counter-attack | Does not hold. § $\mathsf{P1}$'s iff is a universal quantifier over individual $(\Gamma,C)$ pairs; nodes with globally identical inferential roles ARE the same node in SIRC's extensional ontology. Valid kernel: proof-path multiplicity for inferential-role-identical nodes is not part of the § $\mathsf{P1}$ invariant. §A9 adds topological position to disambiguate symmetric nodes at transmission level. |
| Tautological Collapse — "consequence relation" is graph reachability; logical vocabulary is superfluous; § $\mathsf{P1}$ reduces to graph isomorphism | Pass 13 — Gemini §A9 counter-attack | Does not hold once operator types are invariant (§A10). The tautology only applies to untyped graphs. A typed DAG has logical derivability as its consequence relation, not reachability — two typed graphs with identical topology but different operator assignments have different consequence relations. |
| Operator Void — operators are "vocabulary" → surface form → stripped; SIRC cannot encode negation | Pass 13 — Gemini §A9 counter-attack | Precision gap; closed by §A10. "Vocabulary" was ambiguous; §A10 distinguishes non-logical vocabulary (surface form) from logical operator types (invariant structural content). → §A10. |
| Semantic Void — stripping non-logical vocabulary produces an uninterpreted proof schema; any domain substitution satisfies § $\mathsf{P1}$; § $\mathsf{P4}$ inverse coupling violated | Pass 14 — Gemini §A10 counter-attack | Does not hold as structural attack; attacks design intent. Domain substitution is designed mutation (OQ2.1). § $\mathsf{P4}$ "violation" correctly describes the tradeoff. Valid kernel: §A11 precision on what § $\mathsf{P3}$ encodes; §A12 concession that structural constraints cannot distinguish domain-isomorphic models. → §A11, §A12. |
| Shannon Entropy Failure / Zero-bit Semantic Payload — $I(\text{domain};\text{packet}) = 0$; the protocol transmits no domain-relevant information | Pass 16 — Gemini §A12 counter-attack | Does not hold; correctly describes scope but misidentifies it as failure. $I(\text{domain};\text{packet}) = 0$ is the designed behaviour — domain is surface form by definition. Imports blank-receiver premise (rejected, Unknown N). Valid kernel: OQ2.1 should name the shared-domain-context assumption explicitly. |
| Topological Ontology Paradox — domain bounding via topology requires transmitting MDL(domain ontology) >> MDL(thought), violating § $\mathsf{P3}$; label-based $O(1)$ mechanism forbidden by §A10 | Pass 17 — Gemini §A12/§A11 counter-attack | Does not hold; forces a concession already made in §A12. The "Pure Formalism Path" demanded is the current protocol position. Valid kernel: $O(1)$ label vs. intractable topology complexity argument precisely explains why §A12's concession holds; added to §A12 exploration value. |
| Teleological Smuggling / CSP Collapse — §A13's "targeted reconstruction" is out-of-band; CSP search space is $O(|V_\text{domain}|^{|V_\text{packet}|})$; § $\mathsf{P4}$ must be fully rewritten | Pass 18 — Gemini §A13 counter-attack | Does not hold as full retraction demand. Teleological attack neutralised by §A14 (Layer 2 brings domain guidance in-band). CSP attack uses naive enumeration, not constraint-propagation-effective cost; VF2-class propagation prunes additional constraints faster than it adds them. § $\mathsf{P4}$ Definition updated to specify constraint-propagation-pruned space. |
| Layer 2 Epistemic Contradiction / § $\mathsf{P1}$ Loophole — Layer 2 is surface form → not a load-bearing boundary condition; § $\mathsf{P1}$ permits discard → Pure Formalism; § $\mathsf{P4}$ only holds above CSP phase transition | Pass 18 — Gemini §A14/§A13 counter-attack | Partially holds on two sub-arguments (§ $\mathsf{P1}$ loophole → cooperativity assumption required; phase transition → regime restriction required). Semantic smuggling sub-argument does not hold. → §A15. |
| § $\mathsf{P4}$ Inversion Paradox / CSP Collapse — over-constrained packets require NP-complete subgraph isomorphism; more sender work increases receiver work; § $\mathsf{P4}$ coupling is backwards | Pass 17 — Gemini §A13 counter-attack | Partial hold. Correctly identifies verification cost as a dimension § $\mathsf{P4}$ omits; overclaims full rewrite. Inverse coupling holds for search cost under targeted reconstruction; verification cost (graph homomorphism) is directly coupled and dominates under Pure Formalism. → §A13. |
| Satisfiability Paradox / Unprotected Boundary — over-constrained SIRC packets must be UNSAT (E[X]→0) by CSP phase transition theory; Layer 2 has no channel reliability requirement | Pass 19 — Gemini §A15 counter-attack | Satisfiability Paradox does not hold — applies random CSP theory to designed instances (category error); SIRC packets are over-constrained AND satisfiable (E[X]≈1); Sudoku 17-clue analogy applies. Unprotected Boundary is a precision extension — channel noise operationally equivalent to non-cooperative receiver; cooperativity assumption extended to cover both. → §A15. |
| Isomorphism Collapse / Node Identity Vacancy / Equivocation — transitive closure trap; propositional set contradiction; symmetry erasure; logical vocabulary masks graph reachability | Pass 20 — Gemini §A10/§A9/§A1 structural teardown | Transitive Closure Trap: false premise — typed DAG consequence relation is logical derivability, not edge-set transitive closure (§A10). Propositional Set Contradiction: precision gap in quantifier domain, closed by explicit domain restriction in § $\mathsf{P1}$ Def item 1. Symmetry Erasure: Disjunctive Collapse redux — §A9 topological position distinguishes symmetric nodes. Equivocation: depends on 1 and 3, both false. → §A16. |
| Topological Identity Contradiction — §A9 topological position and §A1 path-length flexibility are inconsistent; operator parity presupposes shared logical primitives | Pass 20 — Gemini §A9/§A1/§A10 consistency attack | Precision gaps identified; document did not yet explain why the two levels do not contradict. §A9 is intra-graph disambiguation (which transmitted node is which); §A1 is reconstruction validity (entailment-map position preserved by transitivity) — different levels, not in tension. Operator parity: verification hardness ≠ definitional incoherence (OQ1.3); operator labels name truth-table functions. → §A16. |
| Entailment vs. Structure Equivocation — §A9/§A1 inconsistency re-run; transmitted object is uninterpreted proof skeleton; operator parity presupposes shared logic; verification gap requires DAG replication | Pass 21 — Gemini §A16/§A9/§A10 re-attack | Sub-arguments 1 and 4 do not hold (Pass 20 re-runs; §A16 closes both). Sub-argument 2 does not hold — accurately describes the protocol's design; whether logical-form transmission constitutes "thought transmission" is OQ5.1. Sub-argument 3 partially holds: "substrate-independent" requires operator-type-compatible substrates; named as Substrate scope condition in preamble. → OQ1.4, OQ5.1. |

---

## Audit characterization record

Precision additions made in Passes 8–9 are recorded here to prevent misreading of those additions as strategic repositioning in response to attacks. Three characterizations appearing in the Pass 9 final audit summary ("Logically Feasible / Formally Robust") are inaccurate and recorded as closed directions.

| Claim in final audit summary | Actual record | Why the characterization is wrong |
|---|---|---|
| "The document **pivoted** to Proof-Theoretic Semantics" | Pass 9 — precision addition: one sentence naming the philosophical tradition the document already occupied | The document always used inferential role as the identity criterion. The addition named the tradition; it did not change the stance. No attack caused repositioning. A pivot implies the prior state was different — it was not. |
| "The target was **shifted** from Uniqueness to $\mathsf{P1}$-Equivalence" | Pass 8 — rejected critique (Infinite Grid): the uniqueness requirement was never in $\mathsf{P1}$ or $\mathsf{P3}$ | The uniqueness framing appeared in a draft OQ3.1 addition and was corrected before application. The document's core claim was always $\mathsf{P1}$-equivalence. The "shift" was a correction to draft language, not a change to any principle. |
| "Reinventing the Wheel resolved by citing groundings (Shannon, Kolmogorov, Mac Lane, McGuire)" | Pass 1 — rejected critique: citations always present; defense was rejection, not document revision | No document change was made in response to the reinvention charge. Those citations existed before any audit pass. The defense is recorded in the rejected critiques table (Rev 0, Rev 1: "Dead end as unified mathematical theory — applies only if method-level pointers are read as foundational claims"). |

**Implication for future audit:** The $\mathsf{P1}\text{–}\mathsf{P4}$ statements are unchanged from Pass 4 onward. Passes 5–9 produced clarifications, precision additions, and pointer repairs — no structural changes to any principle. An auditor finding the Pass 9 final summary and treating it as the audit history will have a wrong model of the document's provenance. This record is the correction.

---

## §A1

**Description:** Node Identity ambiguity — "what entails it" readable as immediate predecessor in the DAG
**Source:** § $\mathsf{P1}$ Node Identity
**Date:** 2026-04-09
**Trigger:** Pass 5 — Gemini attack on entailment equivalence vs. isomorphism

### Why addressed

The phrase "what entails it" in the Node Identity definition is ambiguous between two readings:
- *Consequence-relation reading* (intended): any premise from which the proposition is derivable in the entailment map.
- *Edge-adjacency reading* (not intended): immediate predecessor nodes in the dependency graph.

Gemini's attack exploited the edge-adjacency reading: if $B$ is an immediate child of $A$ on the sender and an immediate child of $C$ on the receiver, the attack argues $B$'s inferential role differs across substrates, therefore node identity fails, therefore entailment equivalence collapses to structural isomorphism. This reading is incorrect but the text permitted it.

This is a clarification, not a retraction. The underlying claim was correct throughout; the exposition was imprecise.

### What changed

Added to Node Identity:

> `(what it entails; what entails it at the level of the consequence relation — not which immediate predecessors it has in the dependency graph)`

And a closing paragraph making the concrete case explicit and naming the two-class taxonomy:

> `Dependency path is not inferential role: if $A \vdash B$ holds in both the sender's structure and the receiver's reconstruction, $B$'s inferential role is preserved regardless of whether the receiver introduces an intermediate step $C$ such that $A \vdash C \vdash B$. The intermediate step is a dependency-path artifact; it does not alter $B$'s position in the entailment map. A nomenclature mismatch is a node identity failure; a path-length mismatch is a dependency-path variation that remains $\mathsf{P1}$-compliant.`

The global/local framing and abstract "paths differ in length" language from Gemini's proposed repair were rejected — new vocabulary, same effect as the parenthetical. The final taxonomy sentence was incorporated as additive: it names the two-class decision procedure not present in the original text.

### Exploration value

The clarification makes the entailment-equivalence vs. isomorphism distinction load-bearing and explicit. Any future attack claiming node identity forces isomorphism must now engage the consequence-relation definition directly, not the edge-adjacency reading. The text no longer admits that misreading.

---

## §A2

**Description:** OQ3.1 success criterion framed as uniqueness; cardinality/geometry axes unnamed
**Source:** § $\mathsf{P3}$ OQ3.1 first research pointer
**Date:** 2026-04-15
**Trigger:** Pass 8 — Gemini Infinite Grid attack on OQ3.1 draft

### Why addressed

The existing OQ3.1 text mentioned "geometry of constraint distribution (placement across the structure, not only count)" but did not name cardinality and geometry as two distinct axes with different tractability profiles. A draft addition was written to close the Sudoku analogy vulnerability but inherited the analogy's uniqueness criterion ("force a unique reconstruction") — which is not what $\mathsf{P1}$ or $\mathsf{P3}$ requires. Additionally, the distinction between a $\mathsf{P3}$ failure (wrong encoding type) and an OQ3.2 failure (insufficient receiver capacity) was not stated in the OQ3.1 text, leaving the failure modes conflatable.

This is a clarification and precision addition, not a retraction. The document's core claim was always $\mathsf{P1}$-equivalence, not uniqueness. The addition corrects draft language and makes the two axes and two failure modes explicit.

### What changed

New research pointer "(cardinality and geometry)" added to OQ3.1 after the existing Sudoku pointer:

> `OQ3.1 has two axes that are related but not equivalent. (a) Cardinality: the minimum number of constraints required. (b) Geometry: the distribution of those constraints across the entailment map. McGuire et al. establishes (a) for Sudoku, where the target is a unique solution. SISC's target is different: boundary conditions succeed if they constrain reconstruction to the § $\mathsf{P1}$equivalent set... The geometry axis is the harder open direction... The cardinality minimum is geometry-dependent... A packet satisfies § $\mathsf{P3}$ if it encodes constraints on the § $\mathsf{P1}$valid space regardless of whether the receiving substrate has sufficient capacity to exploit those constraints. § $\mathsf{P3}$ failure and OQ3.2 failure are distinct: § $\mathsf{P3}$ concerns encoding type; OQ3.2 concerns the receiver threshold at which that encoding becomes resolvable. The research question for reasoning structures is: how many constraints, of what type, at what positions in the entailment map, such that all reconstructions within the boundaries are § $\mathsf{P1}$equivalent.`

### Exploration value

Naming the two axes opens independently investigable research directions — cardinality may be tractable in restricted domains before geometry is solved. The $\mathsf{P1}$-equivalence target is more tractable than uniqueness for open-domain reasoning, and narrows the research question to the correct class. The $\mathsf{P3}$/OQ3.2 failure-mode distinction clarifies the protocol's architecture for system designers: a packet that is correctly typed but unresolvable is a different problem from one that is incorrectly typed.

---

## §A3

**Description:** Node Identity: labels readable as prohibited from use as reconstruction scaffolding
**Source:** § $\mathsf{P1}$ Node Identity
**Date:** 2026-04-15
**Trigger:** Pass 9 — Identity-Identifier Collapse attack

### Why addressed

The phrases "label is surface form" and "label agreement is not sufficient" could be read as prohibiting labels from serving as coordination handles during reconstruction. The Pass 9 attack exploited this reading: if labels cannot be used to link constraints during assembly, the receiver has no basis for joining $\{Node\_A\} \vdash Node\_B$ with $\{Node\_B\} \vdash Node\_C$, making reconstruction operationally impossible. The underlying claim was correct throughout — labels are not the identity criterion — but the exposition permitted the misreading.

This is a clarification, not a retraction. The prohibition is on treating label agreement as sufficient for identity, not on using labels as scaffolding. These are distinct functions and the text now names them as such.

### What changed

Three sentences added to Node Identity after "label agreement is not sufficient":

> `Labels may serve as provisional coordination handles during reconstruction — the receiver uses transmitted labels to link constraints while assembling the entailment map. Final node identity is established by inferential role once the map is complete, not by label consistency during assembly. The prohibition is on treating label agreement as a sufficient identity criterion, not on using labels as reconstruction scaffolding.`

### Exploration value

Makes the two functions of labels explicit and independently attackable: (1) identity criterion — inferential role; (2) coordination handle during reconstruction — labels permitted. A future attack must now target one function specifically. The clarification also maps directly onto how natural language works during communication: labels serve as provisional handles; semantic role is established relationally.

---

## §A4

**Description:** Node Identity: proof-theoretic tradition not named; model-theoretic reading not closed
**Source:** § $\mathsf{P1}$ Node Identity
**Date:** 2026-04-15
**Trigger:** Pressure Point 1 — semantic/syntactic equivocation attack

### Why addressed

The title "Substrate-Independent *Semantic* Communication" invites a model-theoretic reading of "semantic" — meaning as reference to external objects, independent of inferential structure. $\mathsf{P1}$'s node identity uses inferential role as the identity criterion, which is the proof-theoretic tradition (meaning constituted by inferential role). Without naming this tradition, an attacker can claim the protocol transmits syntax not semantics — that structural isomorphism is a syntactic criterion dressed in semantic language. The document's position was correct throughout; it needed naming to foreclose that reading.

This is a precision addition, not a retraction. No philosophical stance changed. The sentence names the tradition the document already occupied.

### What changed

One sentence added immediately after the first sentence of Node Identity, before "Label is surface form":

> `Node identity as defined here treats inferential role as constitutive of meaning: a proposition's meaning is its position in the entailment structure — what it entails and what entails it — not its reference to objects in the world. This is the proof-theoretic reading of 'semantic'; the model-theoretic reading, where meaning is grounded in reference to external objects independent of inferential structure, is outside the scope of § $\mathsf{P1}$.`

### Exploration value

Permanently closes the semantic/syntactic equivocation attack by naming the philosophical parent. A future attack on whether SISC is "really semantic" must now engage proof-theoretic semantics directly — a well-developed tradition — rather than exploiting ambiguity in the word "semantic." The scope exclusion (model-theoretic reading outside $\mathsf{P1}$) is also a positive boundary: it tells a future researcher that extending SISC to referential semantics would require new machinery beyond $\mathsf{P1}$'s current definition.

---

## §A5

**Description:** OQ1.2: positive and negative result conditions not specified
**Source:** § $\mathsf{P1}$ OQ1.2
**Date:** 2026-04-15
**Trigger:** Pressure Point 3 — epistemic sharpening

### Why addressed

OQ1.2 correctly deferred extractability of invariants from neural substrates as "an empirical question outside the boundary of this principle." This is accurate but underdetermined: it does not specify what evidence would constitute a positive result, what evidence would constitute a negative result, or what a negative result would mean for $\mathsf{P1}$'s scope claim. Without result conditions, OQ1.2 is not actionable as a research frontier — it names a gap without defining what closing it would look like.

This is a precision addition. The deferral is correct and unchanged. The addition specifies the test structure, not the method.

### What changed

Result conditions research pointer added to OQ1.2:

> `A positive result requires a procedure that, given a substrate's internal states, recovers a set of (Γ, C) entailment pairs that are stable under paraphrase and invariant to surface label change — the same pairs must be recoverable regardless of how the proposition is expressed or labelled. A negative result — a proof that no such procedure exists for a given substrate architecture — would bound § $\mathsf{P1}$'s scope to symbolic substrates only and reopen the substrate-independence claim at the principle level. A negative result is therefore not a corner case: it would require revision of § $\mathsf{P1}$'s scope, not only of OQ1.2. The gap between these two outcomes defines the research frontier: methods that recover stable (Γ, C) pairs from activation space without label-decoding are the target class; methods that recover labels and infer roles from them are outside it.`

### Exploration value

Makes OQ1.2 a falsifiable research frontier rather than a deferred question. The negative result condition's stakes — requiring a $\mathsf{P1}$ scope revision — elevate OQ1.2 from an engineering question to a foundational test of SISC's substrate-independence claim. The target class definition (stable $(\Gamma, C)$ pairs without label-decoding) gives researchers a precise criterion that distinguishes qualifying methods from non-qualifying ones, preventing the open question from being closed by weaker results.

---

## §A6

**Description:** §A4 repair reversed — proof-theoretic tradition reference removed from Node Identity
**Source:** § $\mathsf{P1}$ Node Identity
**Date:** 2026-04-16
**Trigger:** Author revision — vocabulary too lossy; naming a tradition imports that tradition's attack surface

### Why addressed

§A4 added a sentence to Node Identity naming the proof-theoretic philosophical tradition as the document's position on the semantic/syntactic distinction:

> `This is the proof-theoretic reading of 'semantic'; the model-theoretic reading, where meaning is grounded in reference to external objects independent of inferential structure, is outside the scope of § $\mathsf{P1}$.`

This repair correctly closed the model-theoretic attack by naming the tradition the document occupied. However, during the SIRC→SIRC rename review, the repair was found to carry its own liability: naming proof-theoretic semantics as the tradition imports that tradition's contested vocabulary into SIRC's formal claims. An attacker familiar with proof-theoretic semantics can now probe whether SIRC correctly applies that tradition, whether inferential role as SIRC uses it is consistent with Dummett, Prawitz, or Brandom, and whether the tradition's full commitments are honoured elsewhere in the document. The fix exchanged one attack surface (semantic/syntactic ambiguity) for a narrower but still exploitable one (tradition fidelity).

The correct move — identified as the R10 pattern — is to remove the contested borrowed vocabulary entirely rather than defining it more precisely. A SIRC-native operative definition of node identity does not require philosophical tradition backing. The document's claim is internal to the protocol: a node is identified by its inferential role in the entailment structure transmitted and received. Whether that constitutes "meaning" in any external tradition is not the protocol's question to answer.

This is a clarification, not a retraction of the §A4 finding. The underlying §A4 problem (model-theoretic attack was exploiting semantic/syntactic ambiguity) was real and correctly diagnosed. The §A4 repair was an intermediate step — it closed one attack by naming a tradition. §A6 reverses that repair in favour of a stronger defensive posture: the protocol does not participate in the semantic/syntactic debate because it does not invoke the vocabulary the debate runs on.

### What changed

§A4's added sentence (proof-theoretic tradition reference + model-theoretic exclusion) was removed from Node Identity.

**Retracted content from §A4 repair:**

> `Node identity as defined here treats inferential role as constitutive of meaning: a proposition's meaning is its position in the entailment structure — what it entails and what entails it — not its reference to objects in the world. This is the proof-theoretic reading of 'semantic'; the model-theoretic reading, where meaning is grounded in reference to external objects independent of inferential structure, is outside the scope of § $\mathsf{P1}$.`

**What replaces it:**

> `In SIRC, this is the operative definition of node identity; it is internal to the protocol and does not invoke or depend on any tradition of semantics from philosophy of language or information theory.`

The replacement does not name a tradition. It states the definition is internal to the protocol and explicitly disclaims dependence on external semantic traditions. An attacker cannot probe tradition fidelity against a claim that asserts no tradition membership.

### What this does not concede

The model-theoretic attack (that SIRC's inferential role criterion is "really syntactic" because it does not invoke reference) is not conceded. The defense shifts ground: SIRC's node identity criterion is not a claim about semantics in any tradition's sense — it is a protocol-internal operative definition. Calling it syntactic requires the attacker to import a semantic/syntactic distinction that the protocol does not recognize. The §A4 defense was active (asserting proof-theoretic membership to deflect the attack). The §A6 defense is passive (the attack's framing does not apply to a protocol that makes no tradition claim). Passive defense is stronger when the contested vocabulary cannot be owned cleanly.

### Exploration value

The §A4→§A6 sequence demonstrates the R10 pattern applied to a repair, not only to an initial claim: a precision addition that names a borrowed tradition can be a correct intermediate step (closing one attack) and still be reversible when a stronger alternative is found. The finding is that tradition membership claims carry the liability of that tradition's full contested vocabulary. For any future SIRC document using vocabulary from philosophy of language, information theory, or formal semantics: the question is not whether to define the term, but whether to use it at all. SIRC-native vocabulary that makes no external claim has no external attack surface.

---

## §R11

**Description:** Algebraic Topology (Homology) named as the formal parent for SET identities
**Source:** § $\mathsf{P3}$ OQ3.2 research pointer
**Date:** 2026-04-12
**Retraction trigger:** Pass 6 — Gemini audit on Rubik's Cube / invertibility (topology vs. combinatorics finding)

### Why retracted

The OQ3.2 pointer correctly identified the Phistomefel Ring's mathematical parent in the sentence immediately before the retracted claim: *"algebraic constraint identity (Symmetric Group Sn acting on permutation structure)."* The final sentence then asserted *"Algebraic Topology (Homology) is the correct formal parent for the conservation-law structure the Ring demonstrates"* — which contradicts the preceding sentence.

The SET identities in Sudoku follow from permutation overlap constraints in a finite combinatorial structure. Homology is the study of holes and cycles in topological spaces via chain complexes; it has no mechanism for reaching a permutation-conservation identity in a finite grid. The word "conservation-law structure" does not invoke topology — it names the algebraic consequence of how the Symmetric Group's permutations must overlap. The correct parent was already stated. The Homology sentence added a false categorical claim.

### Retracted content

> `Algebraic Topology (Homology) is the correct formal parent for the conservation-law structure the Ring demonstrates.`

### What replaces it

Nothing. The preceding sentence already names the correct parent. Removal restores the internal consistency of the pointer.

### Exploration value

The retraction closes a potential confusion between two uses of "conservation": (1) conservation in the algebraic/combinatorial sense — permutation overlap forces multiset conservation across regions — and (2) conservation in the topological sense — homological invariants. These are unrelated mechanisms. The retraction prevents a future researcher from pursuing a topological formalization of SET identities based on this pointer and reaching a dead end. The correct search space is algebraic: Symmetric Group structure, combinatorial identity, constraint satisfaction — not topological invariants.

---

## §R12

**Description:** "Mathematical parent" label overclaims epistemic status in OQ3.2
**Source:** § $\mathsf{P3}$ OQ3.2 research pointer
**Date:** 2026-04-12
**Retraction trigger:** Pass 7 — Gemini revision evaluation audit

### Why retracted

The note in OQ3.2 describing the Phistomefel Ring's mathematical home was labeled "Mathematical parent:" — a grounding label. Within a SIRC research pointer, this reads as: *"the mathematical parent of this SIRC research direction is $S_n$."* That claim would formally import $S_n$'s invertibility into a system explicitly defined as non-invertible (directed logical entailment). The pointer uses the Ring as a motivating analogy for receiver derivability; it does not commit SIRC to $S_n$ as its algebraic framework. Survival criterion 6 requires claim strength to match epistemic status. "Mathematical parent" exceeds the defensible claim.

The underlying note is valid — it correctly describes the Ring's own mathematical home (algebraic, not topological) and closes the braid direction. The error is the label only.

The auditor's proposed replacement language ("mechanism of overlapping constraints forcing global conservation laws transfers as an intuition") was rejected as over-specification — it prescribes what transfers from the analogy, which is researcher homework, not a principles-level commitment.

### Retracted content

> `Mathematical parent: the Phistomefel Ring is grounded in algebraic constraint identity...`

### What replaces it

> `Analogy source: the Phistomefel Ring is grounded in algebraic constraint identity...`

Two words changed. The note's content and function are unchanged — it still describes the Ring's own mathematical home and closes the topological/braid direction. The label now correctly scopes the note as describing where the analogy comes from, not what SISC is formally grounded in.

### Exploration value

The retraction establishes a labeling distinction that applies to all research pointers using analogies: describing the analogy's mathematical home (where the source object lives) is not the same as asserting a formal parent for the SISC claim. Future pointers that need to identify the source of an analogy should use "Analogy source:" rather than any grounding label.

---

## §R13

**Description:** "Semantic" removed from protocol name — SISC renamed SIRC
**Source:** Title (`Substrate-Independent Semantic Communication`); all formal uses of "Semantic" as part of the protocol name throughout
**Date:** 2026-04-16
**Retraction trigger:** Author revision — § $\mathsf{P1}$ self-referential violation; R10 pattern applied

### Why retracted

The protocol name "Substrate-Independent Semantic Communication (SISC)" fails $\mathsf{P1}$ as a self-referential case. The name is itself a constraint packet transmitted to receivers. The word "Semantic" admits non-$\mathsf{P1}$-equivalent reconstructions across receivers:

- **Proof-theoretic:** semantic = inferential role in an entailment structure
- **Model-theoretic:** semantic = reference to external objects in a model
- **Shannon-Weaver:** semantic = meaning relative to the receiver's interpretation, including communicative intent and pragmatics
- **Distributional:** semantic = meaning as captured by co-occurrence patterns in corpora
- **Pragmatic:** semantic = what is communicated in context, including implicature

These are not $\mathsf{P1}$-equivalent reconstructions. A protocol whose name is itself a $\mathsf{P1}$-violating transmission cannot coherently claim $\mathsf{P1}$ as a foundational constraint. This is a self-referential violation: the protocol fails the invariance requirement it defines.

The correct move is R10's pattern: remove the contested borrowed term from formal claims rather than redefining it. Redefining "semantic" within the protocol would require defending that definition against all competing traditions indefinitely. A SISC-native replacement term — "Reasoning" — is less contested, covers the protocol's actual scope (entailment relations, consequence structures, inference patterns), and does not import any tradition's attack surface.

**Why "Reasoning" is defensible where "Semantic" is not:** "Reasoning" is operationally defined by the protocol itself — the constraint packet transmits entailment relations, and entailment relations are the formal structure of reasoning. No tradition claims exclusive ownership of what "reasoning" means in the way that multiple traditions contest what "semantic" means. An attacker who argues SIRC does not transmit "real reasoning" must engage the protocol's concrete definition (consequence-relation preservation under $\mathsf{P1}$), not invoke a tradition the protocol never cited.

### Retracted content

The word "Semantic" in:
- Protocol name: `Substrate-Independent Semantic Communication (SIRC)`
- All formal document headings, titles, and section labels using "SIRC" or "Semantic Communication" as protocol designators
- Any sentence using "semantic" as a protocol-level descriptor (e.g., "semantic surface mutation" → "surface content mutation"; "semantic content" → "surface content" or "invariant content" depending on context)

Retained (not retracted): uses of "semantic" in purely defensive or metalinguistic contexts, specifically: *"does not invoke or depend on any tradition of semantics from philosophy of language or information theory"* — this sentence uses "semantics" to name what the protocol disclaims, not to characterise what it does.

### What replaces it

- Protocol name: `Substrate-Independent Reasoning Communication (SIRC)`
- Specific terminology replacements made in `SIRC_principles.md`:
  - `Semantic Compression Loss` → `Invariant Content Loss` (§ $\mathsf{P2}$)
  - `non-invariant semantic content` → `non-invariant surface content` (OQ2.1)
  - `semantic surface mutation` → `surface content mutation` (Rate-Distortion analogy)
  - `distortion metric over semantic content` → `distortion metric over surface content` (Rate-Distortion analogy)
  - `prose carries semantics` → `prose carries content` (OQ3.1)
  - Preamble: added **Reasoning scope** note defining what SIRC transmits in protocol-native terms
  - §A4 repair sentence: proof-theoretic tradition reference → SIRC-native operative definition (recorded separately as §A6)

### What this does not concede

The protocol's claim — that entailment relations can be transmitted as constraint packets and reconstructed by a receiver preserving $\mathsf{P1}$-equivalence — is unchanged. The rename is terminological, not substantive. The semantic/syntactic attack (that the protocol only transmits syntax) is not conceded; the defense has shifted from active (asserting proof-theoretic tradition membership, §A4) to passive (the protocol does not participate in the semantic/syntactic debate because it does not use the vocabulary that debate runs on, §A6).

### Exploration value

The rename demonstrates the R10 pattern at protocol-name level: the most load-bearing term in a framework's identity is also the most exposed attack surface. "Semantic" was carrying the full weight of the protocol's identity claim while simultaneously admitting five non-equivalent reconstructions. Replacing it with a term that is operationally defined by the protocol's own content (reasoning = entailment-relation structure, as specified in $\mathsf{P1}\text{–}\mathsf{P4}$) removes the attack surface entirely. Future documents extending or applying SIRC should apply the same test to any term borrowed from a contested tradition: if the term's definition is disputed outside the protocol, use SIRC-native vocabulary instead.

---

## §A7

**Description:** OQ3.1 cardinality/geometry framing carried implicit logic-class scope assumption
**Source:** § $\mathsf{P3}$ OQ3.1 cardinality/geometry research pointer
**Date:** 2026-04-18
**Trigger:** Pass 10 — Gemini re-evaluation 2026-04-18 + independent analysis (dilemma declaration and logic-class restriction)

### Why addressed

The cardinality/geometry pointer frames underdetermination as a geometric problem — solvable by distributing constraints correctly across the entailment map. That framing presupposes monotonic, finitely axiomatizable logics. For non-monotonic logics and arithmetic-expressive logics, underdetermination is a class-level impossibility, not a placement problem. The assumption was not stated. This is a clarification, not a retraction; the pointer is correct within its implicit scope.

### What changed

No existing text was modified. A new research pointer — *(logic-class restrictions on § $\mathsf{P3}$ completeness)* — was added to OQ3.1 immediately after the cardinality/geometry pointer. Full detail of the two failure classes and falsifiability conditions F2–F3 is in that pointer; see `SIRC_principles.md` § $\mathsf{P3}$ OQ3.1.

### Exploration value

Separates two previously conflatable failure modes: geometric underdetermination (OQ3.1's geometry question is live here) and class-level impossibility (geometry question does not apply). The logic-class restriction is now a load-bearing scope condition for any future formalisation of $\mathsf{P3}$ completeness.

---

## §A8

**Description:** Node Identity: co-premise exception not stated; entailment map definition omits arity preservation
**Source:** § $\mathsf{P1}$ Node Identity; § $\mathsf{P1}$ Definition item 1
**Date:** 2026-04-18
**Trigger:** Pass 11 — Arity Collapse attack (Gemini counter-attack on automorphism defence)

### Why addressed

The Node Identity criterion stated: *"Two propositions with different labels that participate in identical entailment relations are the same node."* In the globally symmetric case — two nodes $P$ and $Q$ appearing only in $\{P, Q\} \vdash R$ with no other entailment relations — this criterion collapses $P$ and $Q$ to a single node $N$, producing the receiver reconstruction $\{N\} \vdash R$.

The Arity Collapse attack demonstrated that $\{P, Q\} \vdash R \neq \{N\} \vdash R$: the former encodes a binary premise requirement, the latter a unary one. "Having a key AND knowing the code" is not equivalent to "having a key alone." The collapse therefore violates $\mathsf{P1}$'s entailment map preservation requirement — the invariant the Node Identity criterion is designed to serve.

The prior defence ("global symmetry justifies node collapse; the distinction is a surface matter") was incorrect. The globally symmetric case is precisely the case where the defence cannot appeal to distinguishing global context, because by hypothesis no such context exists. Two globally symmetric co-premises are not the same node because they separately contribute to the arity of their shared entailment relation. Arity is structural content, not surface form.

A related gap: $\mathsf{P1}$'s Definition item 1 defined the entailment map in terms of $(\Gamma, C)$ pairs but did not state that $|\Gamma|$ is a structural property that must be preserved. Without this, a reconstruction that reduces $|\Gamma|$ by collapsing co-premises was not explicitly a $\mathsf{P1}$ failure.

This is a clarification and precision addition, not a retraction of $\mathsf{P1}$'s invariance claim. The fix is structural: arity is a property of the entailment map itself (the cardinality of each $\Gamma$ in each $(\Gamma, C)$ pair) and does not require labels or external indices.

### What changed

**In § $\mathsf{P1}$ Definition, item 1 (Entailment map):** three sentences appended to the existing definition sentence:

> `Arity is part of the entailment map: the cardinality $|\Gamma|$ of each premise set is a structural property that must be preserved. $\{P, Q\} \vdash R$ and $\{N\} \vdash R$ are distinct entries in the entailment map; the former requires two distinct premises, the latter one. A reconstruction that reduces $|\Gamma|$ by collapsing co-premises fails $\mathsf{P1}$ regardless of whether the collapsed nodes had identical inferential role descriptions.`

**In § $\mathsf{P1}$ Node Identity:** the sentence "Two propositions with different labels that participate in identical entailment relations are the same node" was qualified with a co-premise exception and a paragraph naming the canonical case:

> `Two propositions with different labels that participate in identical entailment relations are the same node — unless they are co-premises. Co-premises are nodes that appear as distinct elements within the same premise set $\Gamma$ in any entailment relation. Co-premises are structurally distinct regardless of whether their individual inferential role descriptions are identical, because each separately contributes to $|\Gamma|$. Collapsing co-premises converts a $k$-premise entailment into a $(k-1)$-premise entailment — a change in arity that constitutes a $\mathsf{P1}$ violation under the entailment map preservation requirement above. The globally symmetric case — two nodes $P$ and $Q$ appearing only in $\{P, Q\} \vdash R$ with no other entailment relations — is the canonical instance: identical role descriptions do not license collapse when the nodes are co-premises.`

### What this does not concede

Inferential role as the identity criterion is not abandoned. The co-premise exception is not an external label or arbitrary syntactic index. Co-premiership is defined by structural membership in a shared $\Gamma$ — a property internal to the entailment map. Gemini's Option 1 framing ("arbitrary syntactic scaffolding not derived from the entailment map") does not apply: co-premiership IS derived from the entailment map.

The fix does not require premise sets to become multisets in the underlying logic, nor does it import any logic-level assumption about idempotency. It requires only that the reconstruction mapping preserve $|\Gamma|$ for each entailment relation — a natural constraint on any map that claims to preserve an entailment map.

### Exploration value

The co-premise exception separates two previously conflated cases in the Node Identity criterion:

- **Non-co-premise symmetric nodes:** nodes in different parts of the entailment map with identical role descriptions. These are the same node under $\mathsf{P1}$ — the identity criterion applies correctly.
- **Co-premise symmetric nodes:** nodes in the same $\Gamma$ with identical role descriptions. These are structurally distinct; the identity criterion's collapse rule does not apply.

An attack on non-co-premise collapse now targets a different claim from an attack on co-premise collapse. The arity-preservation requirement also has downstream implications for OQ1.1: two entailment structures are now $\mathsf{P1}$-equivalent only if they agree on both the set of $(\Gamma, C)$ pairs AND the cardinality of each $\Gamma$. Structural variations that preserve the entailment relation but change arity (e.g., splitting one premise into two co-premises that are always supplied together) are $\mathsf{P1}$-inequivalent unless OQ1.1 resolves to permit them as a dependent class.

---

## §A9

**Description:** §A8 justification false: co-premise fix relied on graph topology, not pure entailment map; Node Identity restated as topological identity criterion
**Source:** § $\mathsf{P1}$ Node Identity (§A8 repair)
**Date:** 2026-04-18
**Trigger:** Pass 12 — Extensionality Trap + Syntax Smuggling (Gemini counter-attack on §A8)

### Why addressed

§A8's "What this does not concede" contained a false claim: *"Co-premiership IS derived from the entailment map. Gemini's Option 1 framing ('arbitrary syntactic scaffolding not derived from the entailment map') does not apply."*

Pass 12 demonstrated this is wrong on two counts:

**Extensionality Trap:** §A8 retained standard set theory for premise sets. Under the Axiom of Extensionality, $|\{P,Q\}| = 2$ iff $P \neq Q$. Whether $P \neq Q$ is precisely what node identity is trying to determine. The patch therefore presupposed the answer it was trying to establish — a definitional circle. The co-premise exception cannot be evaluated without prior knowledge of whether the nodes are already distinct, which is the question the exception was supposed to answer.

**Syntax Smuggling:** The only way to break the circularity operationally is to count distinct incoming edges to a node in the transmitted DAG — which is graph topology. §A8's claim that co-premiership is "internal to the entailment map" was therefore false: co-premiership was being derived from the *graph representation* of the entailment map, not from the abstract set-theoretic consequence relation. Graph topology was doing the work while the document claimed it was not.

The correct move — which §A8 avoided — is to acknowledge what the protocol actually does: it transmits a DAG, and topological position in that DAG provides the pre-semantic distinctness anchor. Graph topology is not "arbitrary syntax"; it is invariant structural content. What is surface form is labels and vocabulary, not graph topology.

### What changed

**In § $\mathsf{P1}$ Node Identity:** the §A8 co-premise exception paragraph was replaced with a topological identity statement:

> `Node identity in the transmitted representation is topological: two nodes are distinct if and only if they occupy distinct positions in the DAG, regardless of whether their inferential role descriptions are identical. Graph topology — including arity, co-premise structure, and the number of distinct proof paths to each conclusion — is invariant structural content, not surface form. Surface form is labels and vocabulary; it is not graph topology. The inferential role criterion is therefore a reconstruction validity criterion: a reconstruction satisfies $\mathsf{P1}$ when the consequence relation of the reconstructed DAG matches the sender's under the mapping of node positions. Under this framing, two topologically distinct nodes — whether co-premises in a shared $\Gamma$ or occupying separate proof paths — do not collapse regardless of whether their inferential role descriptions are identical, because their distinctness is established by their position in the transmitted structure, not by their role descriptions. Two propositions with different labels that participate in identical entailment relations are the same node when they also occupy the same topological position in the transmitted graph; otherwise they are distinct.`

The §A8 arity-preservation text in § $\mathsf{P1}$ Definition item 1 was not changed — it is correct. Its grounding now flows from topology rather than from "entailment map derivation," but the text does not assert the latter.

### What this does not concede

The outcome of §A8 is preserved: co-premises do not collapse. What changes is the justification. Co-premise distinctness is grounded in topological position, not in a circular appeal to set membership. The protocol is not conceding that it transmits "arbitrary labels" — graph topology (arity, co-premise structure, proof-path count) is not arbitrary. It is the structural content that $\mathsf{P1}$ claims to transmit.

The forced concession is narrower than Gemini framed it: SIRC does transmit a syntactic object (a DAG), but the topology of that object IS the invariant. Surface form is the labeling layer above the topology, not the topology itself. Inferential role equivalence — the criterion stated in the Node Identity section — was always an informal description of what DAG topology encodes. The revision makes this explicit rather than conflating identity criterion with validity criterion.

### Exploration value

The §A8→§A9 sequence clarifies a two-level structure that was implicit throughout but never named:

- **Transmission level:** node identity is topological. The transmitted DAG is a syntactic object. Distinct positions are distinct nodes.
- **Validity level:** a reconstruction is $\mathsf{P1}$-valid when its consequence relation matches the sender's under the node-position mapping. Inferential role equivalence is the name for this match condition.

Separating these two levels closes the automorphism attacks without requiring labels. It also more precisely scopes what $\mathsf{P1}$ claims to preserve: not the abstract consequence relation in isolation, but the consequence relation together with the topological structure that determines node identity. OQ1.1 inherits this precision: the open question is now framed as "when are two DAG structures with the same topological shape but different compositions $\mathsf{P1}$-equivalent?" rather than the prior looser framing.

---

## §A10

**Description:** "Vocabulary" in surface form clause ambiguous — logical operator types not named as invariant structural content; operator void exposes untyped graph cannot encode negation
**Source:** § $\mathsf{P1}$ Definition (new item 3); § $\mathsf{P1}$ Node Identity surface form clause; "Everything else" surface form line
**Date:** 2026-04-18
**Trigger:** Pass 13 — Operator Void + Tautological Collapse (Gemini counter-attack on §A9)

### Why addressed

§A9 stated: *"Surface form is labels and vocabulary; it is not graph topology."* The word "vocabulary" is ambiguous. In formal logic, "vocabulary" can refer to both non-logical vocabulary (proposition/predicate/variable names — genuinely surface form) and logical operators (AND, OR, NOT, modal operators — structural content). The §A9 text did not distinguish these.

The Operator Void attack demonstrated the consequence: an unlabeled, untyped graph cannot represent negation. The path $A \rightarrow B$ and the path $A \rightarrow \neg B$ are topologically identical in an untyped graph. If logical operators are "vocabulary" → "surface form" → stripped, the protocol cannot encode basic propositional logic. If logical operators are not surface form, the transmitted object is a typed graph and the §A9 text needed to say so.

The Tautological Collapse attack is connected: in an untyped graph, the "consequence relation" reduces to graph reachability (transitive closure), making § $\mathsf{P1}$ equivalent to graph isomorphism and the logical vocabulary superfluous. This tautology dissolves once operator types are present — in a typed graph, the consequence relation is logical derivability determined jointly by topology and operator types, not graph reachability alone. Two typed graphs with identical topology but different operator assignments have different consequence relations. The logical vocabulary is not superfluous; it is the operator typing that makes derivability non-trivial.

The Tautological Collapse therefore does not hold once Point 2 (Operator Void) is resolved. Both attacks are closed by the same revision.

This is a precision addition, not a retraction of §A9. The topological identity framing of §A9 is correct and unchanged. Operator types sit alongside topology as a second component of the invariant structure.

### What changed

**In § $\mathsf{P1}$ Definition:** a new item 3 added:

> `3. **Operator types** — the logical function assigned to each node and edge is invariant structural content: AND, OR, NOT, modal operators, and equivalent types in the target logic. Operator types are not proposition labels; they specify what logical operation a node performs. Relabelling a NOT node as "complement" is surface variation; replacing a NOT node with an AND node changes the reasoning structure and violates $\mathsf{P1}$. An untyped graph cannot represent negation or any non-trivial logical operator — the transmitted object is a typed DAG, not a bare topology. The consequence relation $\mathsf{P1}$ preserves is therefore logical derivability determined jointly by topology and operator types, not graph reachability alone.`

**In § $\mathsf{P1}$ Node Identity:** "Label is surface form. Non-logical vocabulary — the names given to propositions, predicates, and variables — is surface form. Logical operator types (AND, OR, NOT, modal operators) are not surface form; they are invariant structural content specified in $\mathsf{P1}$ Definition item 3."

**In the surface form closing line:** "Everything else — vocabulary, order, substrate encoding — is surface form" revised to: "Everything else — non-logical vocabulary, order, substrate encoding — is surface form. Logical operator types are invariant (§ $\mathsf{P1}$ Definition item 3)."

### What this does not concede

The Tautological Collapse attack ("§ $\mathsf{P1}$ is just graph isomorphism; the logical vocabulary is superfluous") does not hold once operator types are invariant. A typed graph with operator types has a consequence relation that is logical derivability, not graph reachability. Two graphs with the same topology but different operator assignments have different consequence relations — § $\mathsf{P1}$ is therefore not graph isomorphism. The logical vocabulary is precisely the operator typing that makes § $\mathsf{P1}$ non-trivial. Gemini's verdict ("killed the logic") is wrong: operator typing restores the logic without requiring any retraction of §A9.

### Exploration value

The surface form / invariant structure distinction now has a three-way partition:

| Category | Status | Examples |
|---|---|---|
| Non-logical vocabulary | Surface form | Proposition names, variable labels, "Achilles," "raining" |
| Graph topology | Invariant | Arity, co-premise structure, proof-path count |
| Operator types | Invariant | AND, OR, NOT, □, ◇, ⊃, and equivalents in the target logic |

This partition is the correct design target for cross-substrate transmission: what varies (labels), what must be preserved (structure and operators). Future work on the OQ3.1 constraint packet minimum must account for all three levels — a packet that encodes topology but under-specifies operator types is not $\mathsf{P3}$-compliant even if its topology is correct.

---

## §A11

**Description:** $\mathsf{P3}$ "boundary conditions of a thought" ambiguous — domain grounding not explicitly excluded; misreading invites Semantic Void attack
**Source:** § $\mathsf{P3}$ opening definition sentence
**Date:** 2026-04-18
**Trigger:** Pass 14 — valid kernel of Semantic Void rejected critique

### Why addressed

$\mathsf{P3}$'s opening sentence stated: *"A packet encodes boundary conditions of a thought, not its content."* The phrase "boundary conditions of a thought" is ambiguous: it could mean (a) boundary conditions on the § $\mathsf{P1}$invariant structure (the logical form, operator types, entailment topology) — the correct reading — or (b) boundary conditions on the fully domain-grounded thought, which would require domain vocabulary in the packet.

The Semantic Void attack exploited reading (b): if "boundary conditions of a thought" requires domain grounding, then stripping non-logical vocabulary makes the packet fail to bound the domain, producing the unconstrained interpretation problem. The attack as a structural attack does not hold (domain substitution is designed mutation, per OQ2.1; see rejected critiques table). But the ambiguity in the phrase is real.

This is a precision addition, not a retraction of § $\mathsf{P3}$'s claim.

### What changed

**In § $\mathsf{P3}$ opening:** one clarifying sentence added after the first sentence:

> `"Boundary conditions of a thought" means boundary conditions on the § $\mathsf{P1}$invariant structure — the logical form, operator types, and entailment topology. Domain content (what fills the variables), cultural surface, and non-logical vocabulary are not encoded; they are reconstructed by the receiver from its own capacity and prior knowledge.`

### What this does not concede

The Semantic Void verdict ("operationally vacuous") is not conceded. The protocol's design intent is to transmit logical form, not domain-grounded propositions. OQ2.1's designed mutation distinction already validates domain variation as correct protocol behaviour, not failure. The precision addition clarifies the protocol's design intent; it does not change or restrict it.

### Exploration value

The addition makes the § $\mathsf{P3}$/OQ2.1 relationship explicit at the § $\mathsf{P3}$ level: the packet bounds the logical structure; domain reconstruction is the receiver's work, governed by the receiver's prior knowledge and the § $\mathsf{P4}$ tradeoff. A sender who wants to transmit a richer constraint packet includes more structural constraints — these narrow the topological reconstruction space, not the domain interpretation space. Within those topological bounds, any domain-isomorphic interpretation is § $\mathsf{P1}$valid by design. A sender who transmits only the logical skeleton accepts that any structurally isomorphic domain reconstruction is a valid transmission. Correction to prior defense language (§A12): "structural role constraints do domain-bounding work" was imprecise — the correct claim is that they narrow topological reconstruction space; they do not rule out domain-isomorphic interpretations.

---

## §A12

**Description:** Defense argument false: "structural role constraints rule out sourdough starter" — formal constraints cannot distinguish domain-isomorphic models; formal concession made explicit
**Source:** Semantic Void rejected critique record; §A11 exploration value
**Date:** 2026-04-18
**Trigger:** Pass 15 — Model-Theoretic Isomorphism attack (Gemini counter-attack on Semantic Void defense)

### Why addressed

The Semantic Void rejected critique (Pass 14) contained a false sub-claim in the defense argument: *"structural role constraints… do domain-bounding work… structural constraints rule [sourdough starter] out even without labeling the domain."* The §A11 exploration value also contained the imprecise phrase "domain-bounding work."

The Model-Theoretic Isomorphism attack demonstrated this is formally false. Under §A10/§A11, the transmitted packet contains only graph topology and logical operator types. All non-logical vocabulary is stripped. The "structural role constraints" are therefore uninterpreted predicates ( $P_1, P_2, P_3$). By the fundamental theorems of formal logic, a purely formal system cannot distinguish between isomorphic models: if a bijective mapping exists from "hero's journey" predicates to "sourdough fermentation" predicates that preserves all logical relations, the sourdough model is a valid model of the formal system. The structural constraints cannot rule it out.

The defense argument was wrong. The correction: structural constraints narrow the set of valid topological reconstructions, not the set of valid domain interpretations. Within the topological bounds, any domain-isomorphic interpretation is § $\mathsf{P1}$valid.

### The formal concession

SIRC is formally blind to domain isomorphism. If a receiver reconstructs a hero's journey as a sourdough fermentation process, and the logical topology matches, SIRC classifies this as a § $\mathsf{P1}$compliant, zero-loss transmission of the invariant structure. This is not a new concession: it is the existing protocol position. OQ2.1 already states that non-invariant surface content (domain, cultural surface) is expected to vary and is designated designed mutation, not failure. The Achilles/Susanoo example is a special case of the general principle that domain substitution is valid when topology is preserved. The sourdough case is another instance of the same principle.

Making this explicit does not require retracting §A10 or §A11. The protocol's design has always been to transmit logical form, not domain-grounded propositions. "SIRC is blind to domain isomorphism" = "domain is surface form." These are the same claim stated from two directions.

### What changed

**Semantic Void rejected critique entry:** the false sub-claim ("structural constraints rule out sourdough starter") was replaced with the correct description: structural constraints narrow topological reconstruction space; domain-isomorphic interpretations are § $\mathsf{P1}$valid by design; the correction is recorded here.

**§A11 exploration value:** "domain-bounding work" replaced with "narrowing topological reconstruction space"; explicit statement added that domain-isomorphic interpretations are § $\mathsf{P1}$valid within those topological bounds.

No changes to the principles document are required. The OQ2.1 designed mutation principle and § $\mathsf{P3}$'s §A11 clarification already state the protocol's position correctly.

### Exploration value

The model-theoretic isomorphism argument precisely states what SIRC does and does not transmit:

- **What SIRC transmits:** the isomorphism class of the typed DAG (topology + operator types + entailment structure)
- **What SIRC does not transmit:** any information that distinguishes isomorphic domain interpretations of that structure
- **What a valid reconstruction is:** any instantiation that satisfies the logical topology, regardless of domain

This precision is useful for future scope claims about the protocol: any claim that SIRC transmits "domain-specific reasoning" is false. Any claim that SIRC transmits "the logical form of domain-specific reasoning" is true. OQ2.1's designed mutation principle is not an incidental example; it is a direct consequence of this formal property. The designed mutation is exactly model-theoretic isomorphism operating as intended.

**Why topological domain bounding is not available (complexity argument — Pass 17 precision):** The only mechanism for domain bounding available within a §A10-compliant packet is unlabeled topology. Domain bounding via a non-logical vocabulary label (e.g., "Economics") is $O(1)$ sender cost and directly bounds the receiver's search to one domain. Domain bounding via unlabeled topology requires transmitting a topological subgraph that is isomorphic to the target domain but not to any isomorphic competitor domain — effectively the uninterpreted axiomatic ontology of the domain. Since local reasoning structures (Modus Ponens, causal chains, syllogisms) are highly isomorphic across domains, no small topological addition achieves this; the constraint packet size scales with MDL(domain ontology), not MDL(thought). This violates $\mathsf{P3}$'s premise that packet size should scale with the complexity of the transmitted reasoning structure. The formal consequence: within a $\mathsf{P3}$-compliant §A10 packet, domain bounding is not merely high-cost sender work on the $\mathsf{P4}$ curve — it is intractable in principle and $\mathsf{P3}$-violating in the general case. This is the formal reason the §A12 concession holds: domain is surface form not because of a design preference, but because including the mechanism to bound it would violate $\mathsf{P3}$ by making packet size domain-complexity-dependent rather than thought-complexity-dependent.

---

## §A13

**Description:** $\mathsf{P4}$ Definition omits verification-cost dimension — inverse coupling correct for receiver search cost under targeted reconstruction; breaks when verification cost dominates (Pure Formalism / any-valid-instantiation case)
**Source:** § $\mathsf{P4}$ Definition; § $\mathsf{P4}$ OQ4.1
**Date:** 2026-04-18
**Trigger:** Pass 17 — § $\mathsf{P4}$ Inversion Paradox / CSP Collapse (Gemini counter-attack); partial hold

### Why addressed

$\mathsf{P4}$'s Definition states the inverse coupling holds "in the general case" and names two break conditions: unconstrained channel, and low Kolmogorov complexity structures. A third break condition was absent: the Pure Formalism / any-valid-instantiation case, where verification cost dominates and the coupling inverts.

$\mathsf{P4}$ implicitly models receiver work as **search cost** — the cost of finding a § $\mathsf{P1}$equivalent reconstruction in the receiver's prior knowledge. For targeted reconstruction (receiver with domain priors seeking a communicatively useful result), search cost is inversely coupled with constraint density: tighter constraints narrow the space the receiver must search, reducing § $\mathsf{P1}$inequivalent results. This is correct.

What $\mathsf{P4}$ omits is a second dimension: **verification cost** — the cost of confirming that a proposed instantiation satisfies the transmitted typed topology. Verification cost scales directly with constraint density. Checking whether a candidate reconstruction matches a 5-node packet is $O(5)$; checking a 500-node typed DAG requires graph homomorphism verification, which scales with topology size. Under Pure Formalism (§A12), where any domain-isomorphic instantiation is valid and the receiver is solving "find any valid subgraph instantiation," verification is the dominant cost — and it is directly coupled with constraint density.

The CSP framing in the attack is formally correct for the "find any valid solution" problem: under-constrained systems have high solution density so finding any valid solution is trivial ( $O(1)$ in the limit); adding constraints pushes toward the SAT phase transition where finding any valid solution becomes NP-hard. The OQ4.1 phase transition pointer — the protocol's own citation — confirms this: more constraints drives the receiver toward the intractable regime for any-valid-solution search. The attack correctly turns this citation against the principle.

This is a precision addition to $\mathsf{P4}$, not a retraction of its inverse coupling claim. The claim holds for search cost under targeted reconstruction, which is $\mathsf{P4}$'s design use case. The addition names the second dimension and the break condition. **§A14 note:** "targeted reconstruction with domain priors" as written here is underspecified — the protocol-internal mechanism enabling targeted reconstruction is Layer 2 domain guidance (§A14). The receiver does not select a target domain from out-of-band context; the sender includes domain guidance in the packet, and the receiver follows it. §A13's "domain priors" language was correct that the receiver has priors, but the targeting mechanism is Layer 2, not unprompted prior inference. This precision is required to resist the Teleological Smuggling attack (Pass 18, rejected critiques table).

### What changed

**In § $\mathsf{P4}$ Definition:** a third named break condition added after the existing two exceptions:

> `The inverse coupling also assumes the receiver is performing targeted reconstruction — seeking a specific § $\mathsf{P1}$equivalent reconstruction using domain priors, where the bottleneck is search cost (how large a space must be evaluated). Under Pure Formalism's any-valid-instantiation interpretation (§A12), the receiver's bottleneck shifts to verification cost — confirming that a proposed instantiation satisfies the transmitted typed topology. Verification cost scales directly with constraint density: a denser topology requires more work to verify a candidate against it, independent of how many candidates exist. In this regime, more sender work (tighter topology) increases receiver verification cost, and the inverse coupling does not hold. Targeted reconstruction with domain priors is $\mathsf{P4}$'s design use case; the any-valid-instantiation case is a named exception alongside the unconstrained channel and low-Kolmogorov-complexity conditions above.`

**In § $\mathsf{P4}$ OQ4.1:** the research pointer extended to name the Pure Formalism case as a characterised break condition.

### What this does not concede

$\mathsf{P4}$'s inverse coupling is not retracted. It holds for the design use case: targeted reconstruction, where receiver bottleneck is search cost. The "directly coupled in general" rewrite the attack demands is rejected — direct coupling holds only in the any-valid-instantiation formulation, which is not $\mathsf{P4}$'s scope. The attack correctly identifies a dimension $\mathsf{P4}$ omitted; it incorrectly generalises from that dimension to the whole principle.

### Exploration value

The search-cost / verification-cost distinction has downstream implications for OQ4.1. The total receiver work is $W_{receiver} = W_{search} + W_{verify}$. Under targeted reconstruction with domain priors: $W_{search}$ is inversely coupled with constraint density (§ $\mathsf{P4}$ holds); $W_{verify}$ is directly coupled. $\mathsf{P4}$'s inverse coupling holds when $W_{search} \gg W_{verify}$ — i.e., when the receiver has weak domain priors (large search space) and the constraint packet is compact. The coupling inverts when $W_{verify} \gg W_{search}$ — i.e., when the receiver has strong domain priors (search is fast) but the topology is dense (verification is slow). This ratio characterises when the $\mathsf{P4}$ curve is accurate and when it is not. OQ4.1's open direction — "whether total system work is minimised by maximising sender constraint-generation" — now has a more precise framing: total system work is minimised at the constraint density where the marginal sender cost of adding one constraint equals the marginal change in $(W_{search} + W_{verify})$ for the receiver. That minimum is receiver-prior-dependent and topology-dependent; it is not a fixed point on the curve.

---

## §A14

**Description:** §A11 overcorrected — "domain content is not encoded" is false; correct claim is domain content is not *required* (not § $\mathsf{P1}$invariant); sender may include domain guidance as optional Layer 2 content; this resolves the § $\mathsf{P1}$validity vs. communication gap
**Source:** § $\mathsf{P3}$ opening definition (§A11 repair); § $\mathsf{P3}$ Definition; § $\mathsf{P2}$ OQ2.1
**Date:** 2026-04-18
**Trigger:** Author self-correction — user-identified logical gap in §A11: "not invariant" does not entail "not encodable"

### Why addressed

§A11 repaired an ambiguity in $\mathsf{P3}$'s opening sentence by adding: *"Domain content (what fills the variables), cultural surface, and non-logical vocabulary are not encoded; they are reconstructed by the receiver from its own capacity and prior knowledge."*

The repair correctly identified that domain content is not § $\mathsf{P1}$invariant (not required for § $\mathsf{P1}$validity). But it stated a stronger claim: that domain content *is not encoded* — i.e., cannot appear in the packet. This does not follow. The logical gap:

- **What §A11 established:** domain content is surface form — not invariant structural content; a reconstruction in a different domain can still be § $\mathsf{P1}$valid.
- **What §A11 incorrectly inferred:** therefore domain content is never in the packet.

These are different claims. Something can be non-invariant (not required, not § $\mathsf{P1}$protected) and still be *optionally includable* in the packet as additional sender-supplied guidance. $\mathsf{P3}$'s grounding in optimisation theory (boundary conditions on a feasible set) does not prohibit domain constraints from being boundary conditions — it only specifies the type of what is encoded (constraints), not a ceiling on which constraints are permitted.

The overcorrection had a downstream consequence: it made the protocol appear to guarantee that no domain information is transmitted, which entailed that $\mathsf{P1}$-validity and communicative usefulness are permanently decoupled. This is the problem recorded in memory as *SIRC § $\mathsf{P1}$Validity vs. Communication Gap*. §A14 closes that gap.

### The Layer 1 / Layer 2 distinction

The correct account of $\mathsf{P3}$'s packet has two layers:

| Layer | Content | § $\mathsf{P1}$ status | Effect |
|---|---|---|---|
| **Layer 1 — required** | Typed DAG topology + operator types + entailment map | Invariant; receiver must preserve for § $\mathsf{P1}$validity | Logical form preservation |
| **Layer 2 — optional** | Domain constraints, vocabulary hints, context pointers | Surface form; not § $\mathsf{P1}$required; receiver not bound to follow for § $\mathsf{P1}$validity | Domain instantiation guidance |

Layer 2 is additional sender work on the $\mathsf{P4}$ curve. A sender who includes Layer 2 content is providing domain guidance that a receiver can use to instantiate the correct domain. A receiver who ignores Layer 2 and produces a domain-isomorphic reconstruction is still § $\mathsf{P1}$valid (§A12 stands). Layer 2 raises the probability of communicatively useful reconstruction; it does not change the § $\mathsf{P1}$validity criterion.

Without Layer 2: the protocol delivers logical form preservation; designed mutation (OQ2.1) is the expected outcome — the receiver instantiates whichever domain fits their prior knowledge and the topology.

With Layer 2: the protocol delivers reasoning communication — the receiver has domain guidance and is expected to instantiate within the specified domain.

### What changed

**In § $\mathsf{P3}$ opening:** the §A11 sentence "Domain content (what fills the variables), cultural surface, and non-logical vocabulary are not encoded; they are reconstructed by the receiver from its own capacity and prior knowledge" replaced with:

> `Domain content (what fills the variables), cultural surface, and non-logical vocabulary are not required to be encoded — they are not § $\mathsf{P1}$invariant structural content. A sender transmitting bare logical form accepts that the receiver will instantiate whatever domain fits the topology (designed mutation, OQ2.1). A sender who includes domain guidance in the packet as additional boundary conditions (Layer 2) provides the receiver with constraints that narrow domain instantiation; the receiver is not § $\mathsf{P1}$required to follow them, but doing so produces communicatively targeted reconstruction.`

**In § $\mathsf{P3}$ Definition:** Layer 1 / Layer 2 distinction added.

**In § $\mathsf{P2}$ OQ2.1:** Achilles/Susanoo note updated to reflect that designed mutation is the Layer 1-only outcome; Layer 2 domain guidance narrows instantiation.

### What this does not concede

§A11's core finding — that domain content is not § $\mathsf{P1}$invariant — is unchanged. §A12's finding — that formal topology cannot distinguish domain-isomorphic models — is unchanged. The §A14 correction adds an optional layer to the packet; it does not make domain content invariant or change the § $\mathsf{P1}$ criterion. A receiver who produces a domain-isomorphic reconstruction while ignoring Layer 2 guidance is still § $\mathsf{P1}$valid. Layer 2 is communicatively significant but not § $\mathsf{P1}$significant.

### Exploration value

The Layer 1 / Layer 2 distinction resolves the § $\mathsf{P1}$validity vs. communication gap and rehabilitates "Communication" in the protocol name. SIRC is a reasoning communication protocol — it transmits logical form (Layer 1, always) and optionally domain guidance (Layer 2, sender's choice). The degree to which a transmission constitutes communication in the full sense is a function of how much Layer 2 content the sender includes. This maps cleanly onto the $\mathsf{P4}$ curve: minimal sender work (Layer 1 only) → designed mutation; maximal sender work (Layer 1 + rich Layer 2) → targeted domain reconstruction. The two endpoints of the $\mathsf{P4}$ curve are now precisely characterised: one end is formal logical transmission; the other is full communicative transmission. Both are valid uses of the protocol.

---

## §A15

**Description:** $\mathsf{P4}$ omits cooperativity assumption for Layer 2 (soft guidance, not hard constraint; § $\mathsf{P1}$ permits discard) and phase transition regime restriction (inverse coupling holds over-constrained only; under-constrained coupling is direct)
**Source:** § $\mathsf{P4}$ Definition; § $\mathsf{P4}$ OQ4.1
**Date:** 2026-04-18
**Trigger:** Pass 18 — Layer 2 Epistemic Contradiction / § $\mathsf{P1}$ Loophole (Gemini counter-attack); sub-arguments 2–3 partially hold

### Why addressed

Two precision gaps in $\mathsf{P4}$ were identified. Neither requires retracting the inverse coupling claim; both require naming conditions under which it holds.

**Gap 1 — Cooperativity assumption.** $\mathsf{P1}$ states that surface form may differ. Layer 2 domain guidance is surface form (§A10, §A14). Therefore a receiver is § $\mathsf{P1}$compliant when discarding Layer 2. A receiver who discards it operates in the Layer 1-only Pure Formalism regime, where §A13's named exception applies (verification cost dominates, coupling is direct). $\mathsf{P4}$'s inverse coupling holds when the receiver uses the full packet cooperatively — i.e., follows Layer 2 guidance to identify the target domain and uses constraint propagation to search within it. Layer 2 is soft guidance: the receiver may follow it (producing communicatively targeted reconstruction) or discard it (producing § $\mathsf{P1}$valid but domain-unconstrained reconstruction). $\mathsf{P4}$'s description of the design space is accurate for cooperative use; it does not apply to a receiver who discards Layer 2.

**Gap 2 — Phase transition regime restriction.** The SAT/CSP phase transition establishes regime-dependent coupling:

| Regime | Constraint density | Solution density | Effect of adding constraints | Coupling |
|---|---|---|---|---|
| Under-constrained | Low | High | Moves toward phase transition; search cost rises | Direct |
| At phase transition | Critical | Minimal | Maximum backtracking | N/A (hardest point) |
| Over-constrained | High | Near-zero | Solver prunes to infeasibility quickly; cost falls | Inverse |

$\mathsf{P4}$'s inverse coupling — "more sender constraints → easier receiver search" — holds only in the over-constrained regime. In the under-constrained regime, the coupling is direct: adding constraints increases search cost by reducing solution density faster than constraint propagation can compensate. OQ4.1 already cited the SAT phase transition as a research pointer without stating that $\mathsf{P4}$'s coupling reverses below it — an internal inconsistency, since the cited result implies this reversal.

For typical SIRC use (small reasoning structure, large receiver knowledge graph), the system is likely under-constrained: a few-node entailment pattern embedded in a large domain graph has many valid matches. This means $\mathsf{P4}$'s inverse coupling likely does not apply to simple reasoning transmissions. The inverse coupling applies when the sender transmits a large, densely specified reasoning structure — one that is over-constrained relative to the receiver's knowledge graph. $\mathsf{P4}$ must name this assumption.

### What changed

**In § $\mathsf{P4}$ Definition:** two additions —
1. Cooperativity note: Layer 2 is soft guidance; the inverse coupling holds for cooperative receivers following Layer 2; § $\mathsf{P1}$legal discard reverts to §A13 exception.
2. Regime restriction: inverse coupling holds in the over-constrained regime; in the under-constrained regime, adding constraints increases search cost toward the phase transition.

**In § $\mathsf{P4}$ OQ4.1:** the phase transition pointer extended to state explicitly that the coupling direction reverses below the transition, and to name the over-constrained assumption as a load-bearing scope condition for $\mathsf{P4}$.

### What this does not concede

The inverse coupling is not retracted. It holds for cooperative receivers using the full packet in the over-constrained regime. What changes is the precision of its scope: it requires (a) cooperative use of Layer 2, and (b) an over-constrained constraint density. Both conditions are plausible for the complex reasoning structures $\mathsf{P4}$'s design targets — a sophisticated sender transmitting a rich reasoning structure to a cooperative receiver is the primary use case. Simple transmissions (bare A→B) in the under-constrained regime are better described by $\mathsf{P2}$ (accept the loss and move on) than by $\mathsf{P4}$'s design curve.

### Exploration value

The phase transition regime restriction reshapes $\mathsf{P4}$'s design guidance. The inverse coupling is most useful — and most reliable — when the sender has invested significant constraint-generation work (dense, large topology). In that regime, the receiver benefits from the constraint propagation pruning. Below the phase transition, the design guidance reverses: adding more constraints to an already under-constrained packet makes things harder, not easier. The practical implication: a sender should assess whether their reasoning structure, relative to the receiver's domain graph, is under- or over-constrained before choosing where to sit on the $\mathsf{P4}$ curve. The phase transition is the inflection point. This connects to OQ4.1's open question about the threshold where sender constraint-generation cost exceeds receiver search cost — the phase transition is precisely that threshold.

---

## §A16

**Description:** $\mathsf{P1}$ Node Identity two-level distinction (topological position in transmitted graph vs. entailment-map position) not explained explicitly enough to foreclose distance-metric misreading; operator type equivalence not stated as functional/truth-table criterion
**Source:** § $\mathsf{P1}$ Node Identity; § $\mathsf{P1}$ Definition item 3
**Date:** 2026-04-18
**Trigger:** Pass 20 — Topological Identity Contradiction (Gemini consistency attack); precision additions only; no structural concession

### Why addressed

**Gap 1 — Two-level identity explanation.** The Node Identity paragraph already contains the sentence: "Node identity as defined here treats topological position as the transmission-level identity criterion and inferential role equivalence as the reconstruction validity criterion; these are two distinct levels, not the same claim stated twice." This correctly names the two levels but does not explain what problem each level is solving or why they cannot contradict. Gemini's attack exploited this: if "topological position" is read as graph-distance from other nodes, then a receiver who introduces $C'$ (making $A \vdash C' \vdash B$) changes $B$'s distance from $A$, appearing to change $B$'s topological position.

The §A9 topological criterion solves one specific problem: intra-graph disambiguation — distinguishing nodes from each other within the single transmitted DAG. It is the answer to: "are these two transmitted nodes the same node?" (§A9's Disjunctive Collapse problem: two symmetric premises at distinct positions are distinct regardless of inferential-role symmetry.) It does not define how the receiver's reconstruction graph must be structured. The §A1 reconstruction criterion is: does the receiver's proposition for transmitted node $B$ participate in the same entailment pairs? That is answered by inferential role equivalence, not by graph-distance. The receiver's elaboration node $C'$ is not a transmitted node; $B$'s topological position in the transmitted graph is not changed by $C'$'s existence in the receiver's reconstruction.

**Gap 2 — Operator type equivalence.** § $\mathsf{P1}$ Definition item 3 states that "equivalent types in the target logic" are invariant, and that "relabelling a NOT node as 'complement' is surface variation." The equivalence criterion is implicit: two operator types are equivalent when they name the same logical function. Gemini's horn (b) exploits the gap: if equivalence is established by label ("this node is called NOT"), then labels are doing identity work — which would contradict §A10's claim that operator names are not surface form. The correct criterion is functional/truth-table: operator type equivalence holds when the input-output truth tables match, regardless of what the substrate calls the operator or how it physically implements it. This closes both horns: the invariant is the truth-table function (not the label, closing horn (b)); the verification question of whether a substrate's implementation matches a given truth table is OQ1.3's domain (already open, closing horn (a) by separating definition from verification).

### What changed

**In § $\mathsf{P1}$ Node Identity:** After the "two distinct levels" sentence, added explicit explanation: the §A9 topological criterion is intra-graph disambiguation (which transmitted node is which); the §A1 reconstruction criterion is entailment-map position (inferential role). Path-length variation is $\mathsf{P1}$-compliant because the receiver's elaboration node is not a transmitted proposition and does not change any transmitted node's entailment-map position.

**In § $\mathsf{P1}$ Definition item 3:** After the final sentence, added: operator type equivalence is functional/truth-table equivalence, not nominal identity. A NOT-type node is any node whose output holds iff its input does not hold, regardless of substrate implementation. The physical mechanism is surface form; the truth-table specification is the invariant. Verification tractability is OQ1.3's domain.

### What this does not concede

No structural claim in $\mathsf{P1}$ changes. The two-level distinction was already stated; this entry explains it. The operator type claim was already stated; this entry specifies the equivalence criterion. Neither addition is a retraction or a scope restriction.

### Exploration value

The explicit two-level explanation closes a class of "identity-topology deadlock" attacks by making the scope of each criterion precise. §A9's criterion answers one question (intra-graph node disambiguation); §A1's criterion answers a different question (cross-substrate reconstruction validity). An attacker can no longer claim the two criteria are in tension without engaging this distinction. Similarly, specifying operator type equivalence as functional/truth-table makes the invariant independently falsifiable at the substrate level: given two substrates, produce the input-output table for each operator implementation and check for match. Whether this is computationally tractable is OQ1.3; that it is well-defined is now explicit.