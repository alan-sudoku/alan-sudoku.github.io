---
title: SIRC Principles
description: Four constraints on reasoning transmission across substrates.
---

# Substrate-Independent Reasoning Communication (SIRC) — Protocol Constraints

*v3.07 · Retraction log: [SIRC_principles_retraction.md](SIRC_principles_retraction.md)*
*Retraction log pointers (`§Rxx` — retraction; `§Axx` — amendment) are optional depth references, not required for comprehension.*

## Table of Contents

| Section | Claim |
| :--- | :--- |
| § $\mathsf{P1}$ — Invariance | A transmission is valid if and only if the receiver's reconstruction preserves the sender's invariant structural properties. Surface form may differ; invariant structure must match. |
| § $\mathsf{P2}$ — Entropy | Full-state transmission is lossy by necessity (DPI). The protocol targets invariant preservation rather than full fidelity, because full fidelity is unachievable and invariant fidelity is the recoverable floor. |
| § $\mathsf{P3}$ — Constraint Packet | A packet encodes boundary conditions of a thought, not its content. The receiver reconstructs from its own capacity within those boundaries. The output may exceed the packet in size; it cannot exceed the boundaries. |
| § $\mathsf{P4}$ — Work | Sender and receiver work is inversely coupled in the over-constrained regime. No general design choice minimises both simultaneously. |

---


## Preamble — $\mathsf{P1}\text{–}\mathsf{P4}$ are non-derivable, application-coupled, and scope-bounded

### Pedagogical sequence — $\mathsf{P2}$ motivates $\mathsf{P1}$

$\mathsf{P2}$ motivates $\mathsf{P1}$ — understanding that loss is unavoidable ( $\mathsf{P2}$) explains why invariance rather than full fidelity is the correct target ( $\mathsf{P1}$). This is comprehension order, not logical derivation. $\mathsf{P1}$ and $\mathsf{P2}$ are non-derivable from each other: $DPI$ holds without reference to any consequence relation; the logical equivalence criterion holds without reference to any information channel. They interact in application: $\mathsf{P1}$ defines the invariant; $\mathsf{P2}$ characterises why the system must target invariant preservation rather than full fidelity. Application-level coupling is not logical derivation. $\mathsf{P1}$ defines what $\mathsf{P3}$ must encode. $\mathsf{P4}$ follows from $\mathsf{P3}$. $\mathsf{P2}$ does not have a direct dependency edge to $\mathsf{P4}$: higher substrate mismatch increases required work, but that relationship runs through $\mathsf{P3}$ — more entropy requires tighter constraints ( $\mathsf{P3}$), which increases sender work ( $\mathsf{P4}$). A direct $\mathsf{P2}$ → $\mathsf{P4}$ reading obscures the mechanism.

### Categorical scope — four independent mathematical domains

The constraints span four mathematical fields by design. The transmission problem requires independent constraints from four domains: validity (formal logic), limits (information theory), encoding (algorithmic information theory), and cost (computational complexity). Categorical diversity across the set is by design. Each constraint is necessary — removing any one loses an independent dimension of the transmission problem. None is derivable from the others.

### Reasoning scope — entailment relations, not meaning

"Reasoning" in the protocol name denotes the invariant structure of reasoning — the properties preserved under substrate change. The protocol transmits entailment relations: the consequence-relation structure that constitutes reasoning. Whether that structure counts as "meaning" in any external tradition is not the protocol's question to answer. It is not a claim about any theory of meaning. The formal definition is in $\mathsf{P1}$: invariant structural properties as specified by the entailment map and entailment equivalence criterion.

### Substrate scope — encoding independence, not logical universality

"Substrate-independent" denotes independence of encoding and physical implementation — the protocol does not require a specific neural, symbolic, or computational substrate. It does not mean any substrate can participate regardless of its logical capabilities. A valid SIRC receiver must be capable of instantiating the operator types transmitted in the typed DAG (AND, OR, NOT, and equivalent operators in the receiver's logic). A substrate incapable of representing the relevant operators cannot reconstruct the transmitted consequence relation and is outside the protocol's scope. This is an engineering prerequisite, not a theoretical claim. Whether a given substrate meets this prerequisite — and how to verify it — is OQ1.4's domain: if the receiver applies a different inference system, it may derive different $(\Gamma, C)$ pairs from the same transmitted structure, producing a $\mathsf{P1}$-inequivalent reconstruction. The scope condition (shared or provably convergent logical primitives) is a necessary but not yet sufficient condition for cross-substrate $\mathsf{P1}$-validity.

### Verification asymmetry — synthesis claims vs. enumerable claims

The claims in this document fall into two epistemologically distinct categories. The distinction is not marked by the *(O)*/*(C)* tags — it is prior to them.

**Enumerable claims** — values that a verifier can compute from a fully specified structure: $|C_-|$, $|C_+|$, $N_{paths}$, $L_{\min}$, edge counts, ablation outcomes. These are proved by computation. An UNSAT certificate from Z3 BMC is a machine-checkable proof. Any reader can reproduce it independently. Multi-model audit adds nothing here — the verifier is authoritative.

**Synthesis claims** — assertions about how the four constraints interact, generalise, or apply to reasoning transmission: the $\mathsf{P4}$ work asymmetry, $\mathsf{P3}$'s boundary-sufficiency claim, the fitness-peak characterisation of $P_3$ River Crossing puzzle. These are not computable from a spec. They are supported by:
- Internal consistency (*(O)*/*(C)* tagging, falsification conditions, retraction log)
- Multi-model adversarial audit (Claude, Gemini, human review)
- Grounding in established mathematics (DPI, SAT/CSP phase transition, McGuire et al.)

None of these produce a certificate. They produce *consensus*. Consensus among AI auditors has a specific failure mode: **correlated training data**. A reasoning error widespread enough in the pretraining corpus will survive cross-model audit because every auditor shares the same blind spot. Cross-model audit catches idiosyncratic errors; it cannot catch systemic ones.

**The experimental programme is the only verification path for synthesis claims.** The puzzle series ( $P_3$, $P_4$ River Crossing, Tower of Hanoi, Latin square) is not illustration — it is the mechanism by which synthesis claims transition from audited-and-consistent to empirically grounded. The progression:

| Stage | Status | Verification mechanism |
|---|---|---|
| Enumerable puzzle values | Definitively proved | Verifier certificate (BFS + Z3 UNSAT) |
| Ablation outcomes | Definitively proved | Verifier certificate — all rows enumerated |
| Structural pattern within one puzzle family | Candidate | Consistent across $P_3$ and $P_4$ River Crossing enumeration |
| Generalisation across puzzle families | Conjecture | Requires Tower of Hanoi, Latin square, DAG experiments |
| Synthesis claims in §P1–P4 | Audited conjecture | Consistent under multi-model audit; no certificate available |

A synthesis claim in § $\mathsf{P1}\text{–}\mathsf{P4}$ that survives audit but has no grounding in the experimental programme remains an audited conjecture. A synthesis claim that is confirmed by enumerable results across multiple puzzle families is an empirically supported claim — still not a formal proof, but stronger evidence than consensus alone.

**Self-referential note:** SIRC principles claims that reasoning transmission between substrates has the properties characterised in $\mathsf{P3}$ and $\mathsf{P4}$. The audit process that produced and maintains this document is itself a reasoning transmission between AI substrates. The document cannot escape its own scope condition: the audit loop is inside the system being described, not outside it. The puzzle experiments are the only part of the programme that operates outside this loop — the verifier produces results independently of what any AI substrate believes about them.

---

### Communication threshold — $\mathsf{P1}$-validity is necessary but not sufficient

$\mathsf{P1}$-validity is a necessary condition for a transmission to count as communication, but it is not sufficient. A $\mathsf{P1}$-valid reconstruction in a domain-isomorphic but communicatively unintended domain (§A12) satisfies the protocol formally while failing to communicate the sender's intended reasoning to the receiver. The protocol names this gap (OQ5.1) but does not yet have a formal success criterion for it. Optional surface-form content in the constraint packet (the Layer 1/Layer 2 encoding structure defined in § $\mathsf{P3}$) provides a partial answer — domain guidance narrows the receiver's instantiation space toward the sender's intended domain — but does not define when guidance is sufficient for the reconstruction to count as successful communication. OQ5.1 is the open question.

### Open questions index

Open questions are of three types. The type determines how an unresolved OQ should be read: a scope boundary does not weaken the protocol — it names exactly where the protocol stands and where it does not claim to reach. A core definition question names something the protocol depends on but has not yet fully resolved. A research direction names something the protocol requires but does not yet have a construction for. This index is a navigation aid — full OQ content is inline in each principle's `### Open questions` subsection, where the definitions it depends on are in scope.

| Type | OQs | What it means |
|---|---|---|
| **Scope boundary** | OQ2.1, OQ3.1, OQ3.2, OQ5.1 | The protocol holds within a named domain; behaviour outside is declared out of scope, not assumed |
| **Underdetermined validity criterion** | OQ1.1, OQ1.4 | A term on which P1-validity depends admits two readings that produce different verdicts about which transmissions count as valid; the protocol is internally consistent under either reading but has not yet committed to one |
| **Research direction** | OQ1.2, OQ1.3, OQ4.1 | The protocol requires a construction that does not yet exist; candidate mechanisms are identified |

- OQ1.1 — minimal vs. non-minimal dependency structure

  > *Does P1-validity require strict structural isomorphism, or is entailment equivalence sufficient?*
- OQ1.2 — extractability of invariants from neural substrates

  > *Can the invariant — the entailment map — be extracted from neural activations without reading labels?*
- OQ1.3 — verification procedure after reconstruction

  > *How is P1-validity checked after transmission without the sender present, and at what cost?*
- OQ1.4 — whether "inferential role" as the node identity criterion is inference-system-dependent

  > *Is inferential role substrate-independent, or does it shift when the receiver uses a different inference system?*
- OQ2.1 — loss profile of invariant content under substrate mismatch (designed mutation of non-invariant surface is expected; $\mathsf{P1}$ structural degradation is the open question)

  > *Under what conditions does invariant structure itself degrade — not just the surface — when substrates mismatch?*
- OQ3.1 — minimum sufficient boundary conditions

  > *What is the minimum number and placement of constraints that forces P1-equivalent reconstruction?*
- OQ3.2 — receiver capacity threshold

  > *When does receiver capacity determine whether a formally correct packet is actually resolvable?*
- OQ4.1 — sender/receiver work asymmetry

  > *At what point does adding more sender constraints increase rather than decrease total system work?*
- OQ5.1 — communication threshold: what conditions on Layer 2 content are sufficient for the receiver's reconstruction to count as successful communication of the sender's intended reasoning, rather than a $\mathsf{P1}$-valid but communicatively unconstrained reconstruction? The gap between $\mathsf{P1}$-validity and successful communication is the open question. Candidate criterion: the receiver's instantiated domain matches the sender's intended domain with probability above some threshold — but neither the threshold nor a domain-match metric is currently defined.

  > *What Layer 2 content is sufficient to make a P1-valid reconstruction count as successful communication of the sender's intended reasoning?*

---

Each constraint follows the same structure:
- **Statement** — an application of its Grounding to the domain of reasoning structure transmission. Originality is claimed in the application, not in the mathematics.
- **Grounding** — the proven mathematical field and specific result the constraint rests on. No SIRC content; independently verifiable.
- **Definition** — how SIRC applies that result to reasoning structures. Application claims that extend beyond what the Grounding formally establishes are marked `*(C)*`. Numbered bold items within a Definition section are definitional Claims.
- **Open** — questions at the boundary of what the constraint can currently resolve.

*Epistemic status key — unmarked claims follow from the cited Grounding; marked claims carry one of:*
- `*(C) Conjecture*` — consistent with the Grounding; requires empirical or mathematical confirmation
- `*(O) Observational*` — based on current evidence or analogy; may be revised
- `*(OQ) Open question*` — explicitly unresolved; full statement in the `### Open questions` subsection

---

## § $\mathsf{P1}$ — Invariance
A transmission is valid if and only if the receiver's reconstruction preserves the sender's invariant structural properties. Surface form may differ; invariant structure must match.

### Grounding

- **Formal logic** — the consequence relation $\vdash$ is a standard object in formal logic. Preservation of the consequence relation under transformation is the established criterion for logical equivalence.
- **Graph theory** — DAG isomorphism is a well-defined equivalence relation. The isomorphism class of a directed acyclic graph is an invariant under node relabelling.

### Definition

$\mathsf{P1}$-validity requires preservation of three structural properties: entailment map, entailment equivalence, and operator types.
1. **Entailment map** — the entailment map must be preserved exactly: every conclusion that follows from a given premise set in the sender's transmitted reasoning structure must follow from the same premises in the receiver's reconstruction, and vice versa. Formally: for all premise sets $\Gamma$ and propositions $C$ **in the transmitted reasoning structure**, $\Gamma \vdash C$ holds in the sender's structure if and only if it holds in the receiver's reconstruction.
   - *Scope (quantifier range, §A1):* The universal quantifier ranges over propositions of the transmitted structure only — not over propositions the receiver may introduce internally. Receiver-introduced intermediates (e.g., $C'$ in $A \vdash C' \vdash B$ where the sender transmitted $A \vdash B$) are dependency-path scaffolding; they are not in scope for the entailment-map iff.
   - *Claim (arity preservation, §A8):* The cardinality $|\Gamma|$ of each premise set must be preserved. $\{P, Q\} \vdash R$ and $\{N\} \vdash R$ are distinct entries; a reconstruction that collapses co-premises fails $\mathsf{P1}$ regardless of whether the collapsed nodes had identical inferential role descriptions.
2. **Entailment equivalence** — the consequence relation is preserved under structural variation: two dependency structures satisfy $\mathsf{P1}$ if they entail the same conclusions from the same premises, regardless of whether they are isomorphic. A reconstruction is $\mathsf{P1}$-valid if it is entailment-equivalent to the sender's structure — structural isomorphism is not required.
   - *Scope (DAG isomorphism sufficiency, OQ1.1):* DAG isomorphism is a sufficient condition for $\mathsf{P1}$ validity, not the definition of the invariant. OQ1.1 characterises when structural isomorphism is required beyond entailment equivalence.
3. **Operator types** — the logical function assigned to each node and edge is invariant structural content: AND, OR, NOT, modal operators, and equivalent types in the target logic. Operator types are not proposition labels; they specify what logical operation a node performs. Relabelling a NOT node as "complement" is surface variation; replacing a NOT node with an AND node changes the reasoning structure and violates $\mathsf{P1}$.
   - *Claim (typed DAG requirement):* An untyped graph cannot represent negation or any non-trivial logical operator — the transmitted object is a typed DAG, not a bare topology. The consequence relation $\mathsf{P1}$ preserves is logical derivability determined jointly by topology and operator types, not graph reachability alone.
   - *Scope (operator equivalence criterion, §A16):* Operator type equivalence is functional, not nominal: a node is of operator type NOT iff its output holds iff its input does not hold, regardless of substrate implementation. The physical mechanism is surface form; the truth-table specification is the invariant. Whether a substrate correctly realises a given truth table is a verification question — OQ1.3's domain. Therefore: operator type equivalence is well-defined as a check target regardless of whether verification of a substrate's implementation is tractable. *[→ §A16]*

**Node identity** — a DAG node is identified by its topological position in the transmitted representation: where it sits in the graph, not what it is called. A reconstruction is valid when the inferential role of each node — the set of entailment relations in which its proposition participates (what it entails; what entails it at the level of the consequence relation) — is preserved under the mapping of node positions. Node identity operates at two distinct levels: topological position is the transmission-level identity criterion; inferential role equivalence is the reconstruction validity criterion.

- *Argument (transmission-level criterion scope, §A9):* The topological criterion solves one specific problem: intra-graph disambiguation — distinguishing nodes from each other within the transmitted DAG. It answers "are these two nodes the same transmitted node?" within a single transmitted structure. It does not extend to the receiver's reconstruction graph. The receiver may identify its reconstructed nodes by any means — the topological criterion does not reach them. *[→ §A9]*
- *Argument (reconstruction validity criterion, §A1, §A16):* Introducing elaboration nodes does not alter any transmitted node's entailment-map position and is therefore $\mathsf{P1}$-compliant. When a receiver introduces $C'$ (making $A \vdash C' \vdash B$ where the sender transmitted $A \vdash B$), $C'$ is outside the transmitted structure; $B$'s topological position is unchanged. The §A9 and §A1 criteria operate at different levels and are not in tension: §A9 asks which transmitted node is which; §A1 asks whether the entailment-map position of each transmitted node is preserved. A receiver who adds elaboration nodes does not violate $\mathsf{P1}$ — $\mathsf{P1}$ does not reach them. *[→ §A1, §A16]*
- *Claim (surface form exclusion):* Label is surface form. Non-logical vocabulary — the names given to propositions, predicates, and variables — is surface form. Logical operator types (AND, OR, NOT, modal operators) are invariant structural content (§ $\mathsf{P1}$ Definition item 3). A reconstruction satisfies $\mathsf{P1}$ when the consequence relation of the reconstructed DAG matches the sender's under the mapping of node positions. Two topologically distinct nodes do not collapse regardless of whether their inferential role descriptions are identical — distinctness is established by position in the transmitted structure. Cross-substrate node identity is established when the receiver places the proposition at the same entailment-map position as the sender — not by label agreement. A nomenclature mismatch (same term, different inferential roles) is a node identity failure: it produces a different DAG, not a mislabeled one. Labels may serve as provisional coordination handles during reconstruction; final node identity is established by inferential role once the map is complete. A path-length mismatch is a $\mathsf{P1}$-compliant dependency-path variation; a nomenclature mismatch is not.
- *Scope (surface form exclusion set):* Non-logical vocabulary, order, and substrate encoding are surface form. The exclusion set is derived from the entailment map; it is not an independent invariant.

### Open questions — OQ1.1, OQ1.2, OQ1.3, OQ1.4

- OQ1.1 — Whether the dependency structure should be defined at the minimal level (no edge removable without changing the entailment map) or permits equivalent non-minimal derivations. If two valid reasoning paths reach the same conclusion by different routes, resolution requires establishing which equivalence class — entailment equivalence or structural isomorphism — constitutes the $\mathsf{P1}$ invariant and whether non-minimal derivations are permitted.

  > *Does P1-validity require strict structural isomorphism, or is entailment equivalence sufficient?*
  - *Argument (directed categorical equivalence):* *(O)* String diagrams (the graphical calculus of monoidal categories) are a candidate formalization for OQ1.1. Unlike braid groups (§R6 — permanently closed: invertibility requirement), string diagrams natively support irreversible directed flow and logical fan-in. The Mac Lane coherence theorem establishes when two different composition paths are categorically equal — which maps directly onto OQ1.1's question: when do two dependency structures with different routes entail the same conclusions? The open direction is whether string diagram equivalence classes provide a more efficient $\mathsf{P1}$ invariant than strict DAG isomorphism. Note: the "topological" visual intuition is the motivation; the formal mechanism is categorical.
- OQ1.2 — Whether invariant structural properties as defined here are extractable from neural substrates. The invariant is well-defined mathematically. Whether it can be read from a transformer's activations is an empirical question outside the boundary of this principle. This includes node identity as defined above: extraction requires recovering which propositions participate in which inferential roles — independently of their labels. A method that reads labels from activations but cannot recover inferential role has not extracted the invariant.

  > *Can the invariant — the entailment map — be extracted from neural activations without reading labels?*
  - *Scope (result conditions):* a positive result requires a procedure that, given a substrate's internal states, recovers a set of $(\Gamma, C)$ entailment pairs that are stable under paraphrase and invariant to surface label change — the same pairs must be recoverable regardless of how the proposition is expressed or labelled. A negative result — a proof that no such procedure exists for a given substrate architecture — would bound $\mathsf{P1}$'s scope to symbolic substrates only and reopen the substrate-independence claim at the principle level. A negative result is therefore not a corner case: it would require revision of $\mathsf{P1}$'s scope, not only of OQ1.2. The gap between these two outcomes defines the research frontier: methods that recover stable $(\Gamma, C)$ pairs from activation space without label-decoding are the target class; methods that recover labels and infer roles from them are outside it.
- OQ1.3 — $\mathsf{P1}$ defines what a valid transmission is but does not define how validity is checked after reconstruction. Whether the invariant match criterion can be evaluated without the sender remaining active post-transmission, and what computational cost verification adds to the protocol, requires characterising both the sender-dependency condition and the verification cost bound.

  > *How is P1-validity checked after transmission without the sender present, and at what cost?*
  - *Argument (formal verification):* *(O)* SMT solvers (e.g., Z3) are a candidate $\mathsf{P1}$ verification mechanism for formal reasoning domains — satisfying an SMT constraint system is a formal guarantee that the entailment relations encoded as constraints are preserved in the solution. The open problem is the bridge from continuous neural activation space to typed SMT variables.
  - *Argument (conservation-based shortcut):* *(C)* Set Equivalence Theory (Sudoku) demonstrates a structural verification shortcut — the Phistomefel Ring can detect an inconsistent grid without solving it, because conservation of digit multisets across specific partitions must hold in any valid solution. Applied to reasoning structures: if a valid entailment structure must conserve logical dependencies across specific DAG partitions (analogous to SET's region boundaries), a receiver could detect $\mathsf{P1}$ violations at those partition boundaries without re-verifying the full entailment map. This is a partial verification mechanism — it catches structural inconsistency at known symmetry points without exhaustive proof. Complexity significance: checking partition conservation is $O(1)$ or $O(\log N)$ per partition boundary; verifying the full entailment map is $O(N)$. If reasoning DAGs have identifiable partition boundaries where entailment conservation holds necessarily, the shortcut provides sub-linear detection of $\mathsf{P1}$ failure. The open direction is whether such boundaries exist and whether violation at them is sufficient to flag a $\mathsf{P1}$ failure. Shared source note: the same mathematical object (Phistomefel Ring, Symmetric Group $S_n$) appears in OQ3.2 — the two uses are distinct: this pointer draws on the Ring's detection property (a known violation at a partition boundary flags structural failure without full verification); OQ3.2 draws on the Ring's derivability property (a capable receiver produces the Ring from the base constraints without it being transmitted).
- OQ1.4 — The definition of node identity uses "inferential role" as the identity criterion: the set of entailment relations in which a node's proposition participates. Whether this set is inference-system-dependent is not determined by the current definition.

  > *Is inferential role substrate-independent, or does it shift when the receiver uses a different inference system?*

  Two readings are available within the existing vocabulary.

  - *Syntactic position:* a node's inferential role is its position in the transmitted graph — the set of edges encoding which premises entail it and which conclusions it entails. This reading is inference-system-independent: the identity criterion is satisfied by reading the DAG structure directly.

  - *Inferential consequences:* a node's inferential role is the set of $(\Gamma, C)$ pairs derivable when the node participates, determined by applying inference rules to the transmitted graph. This reading is inference-system-dependent: two receivers applying different inference rules to the same graph may produce different $(\Gamma, C)$ sets and therefore assign different inferential roles to the same node.

  The current definition does not commit to either reading. The *syntactic position* reading renders $\mathsf{P1}$-invariance inference-system-independent but collapses "entailment map" to graph structure, making entailment equivalence and structural isomorphism co-extensive — which re-opens OQ1.1 as the dominant unresolved term. The *inferential consequences* reading requires either a shared inference system on both ends of the transmission, or a proof that the transmitted constraint packet forces the same $(\Gamma, C)$ pairs regardless of which inference system the receiver applies. Neither the shared inference system nor the forcing condition is currently specified. $\mathsf{P3}$'s "minimum sufficient description" presupposes the *inferential consequences* reading: sufficient to allow the receiver to reconstruct the same entailment map — a target that is only well-defined if the receiver's inference rules are either fixed or provably irrelevant to the outcome.

  - *Scope (falsifiability condition F1):* construct two receivers applying different monotonic inference systems to the same transmitted graph. If the $(\Gamma, C)$ pairs they derive differ, the *inferential consequences* reading is confirmed as inference-system-dependent, and the protocol requires inference-system specification as a transmission parameter or a proof that the constraint packet forces convergence across systems. If the pairs converge under any pair of monotonic systems tested, characterising the class of systems and constraint types under which convergence holds is the open direction. Connection to OQ3.1: if the $(\Gamma, C)$ pairs vary across inference systems, $\mathsf{P3}$'s minimum sufficient boundary condition is also inference-system-relative — the two open questions share the same precondition.

---

## § $\mathsf{P2}$ — Entropy
Full-state transmission is lossy by necessity (DPI). Whether invariant structure is also at risk under substrate mismatch is unresolved (OQ2.1). The design directive follows from both: the protocol targets invariant preservation rather than full fidelity, because full fidelity is unachievable and invariant fidelity is the recoverable floor.

### Grounding

- **Information theory** --- Shannon's data processing inequality: 
for any processing $Z$ of $Y$, $I(X;Z) \le I(X;Y)$. Equality holds only when $Z$ is a sufficient statistic of $Y$ for $X$ --- when no information relevant to $X$ is discarded in processing. In cross-substrate transmission of high-dimensional reasoning structures, a finite encoding cannot be a sufficient statistic for the sender's full internal state: the receiver's representational space is distinct, making exact recovery structurally impossible. Strict loss follows from the substrate mismatch, not from the $DPI$ alone. $DPI$ establishes the existence of loss — the floor. $DPI$ applies to the full activation state, not the invariant alone. The claim that invariant content is also at risk follows from substrate mismatch (OQ2.1), not from $DPI$ directly.
  - *Argument (structural analogy, rate-distortion theory):* *(O)* Rate-Distortion Theory (Shannon, 1959) characterises the tradeoff space above that floor — the minimum transmission rate required to reconstruct a source within a given distortion bound. The structural mapping to SIRC is visible: Rate corresponds to constraint packet strictness; Distortion corresponds to surface content mutation. This analogy becomes a formal bridge only if a quantitative distortion metric over surface content is defined — which SIRC does not currently provide. Rate-Distortion Theory is a candidate formal framework for OQ2.1, not a current grounding. $DPI$ establishes that loss exists; Rate-Distortion is where that formalization should eventually land.

### Definition

The protocol targets invariant structure preservation, not full fidelity. Loss of surface form is accepted by design; any encoding that claims to eliminate loss violates this constraint.

- *Argument (why invariance, not fidelity):* $\mathsf{P2}$ is the reason $\mathsf{P1}$ targets invariant preservation — full fidelity is not achievable under the data processing inequality, so the system preserves what is P1-invariant and accepts surface loss.

### Open questions — OQ2.1

- OQ2.1 — The loss profile under substrate mismatch has two distinct components that must not be conflated:

  > *Under what conditions does invariant structure itself degrade — not just the surface — when substrates mismatch?*
  - *Scope (designed mutation):* Non-invariant surface content (cultural surface, tone, narrative specifics) is expected to differ across receivers when the sender transmits Layer 1 only (bare logical form). A receiver reconstructing a hero's journey will produce a structurally identical journey with culturally different content — Achilles in one substrate, Susanoo in another. This is $\mathsf{P3}$ operating correctly, not a failure. $\mathsf{P2}$ predicts and accepts this loss. Note: the Achilles/Susanoo example is the Layer 1-only outcome ( $\mathsf{P1}$-invariant content only, no optional surface-form guidance — see § $\mathsf{P3}$). A sender who includes Layer 2 domain guidance (e.g., a cultural context pointer to Greek mythology) narrows the receiver's instantiation space and reduces designed mutation. Whether to include Layer 2 is a sender choice on the $\mathsf{P4}$ curve — more sender work produces more communicatively targeted reconstruction. Without Layer 2, domain is determined by the receiver's prior knowledge; with Layer 2, domain is constrained by the guidance in the packet. Neither outcome is a protocol failure; they are different operating points on the $\mathsf{P3}$ / $\mathsf{P4}$ design space.
  - *Claim (transmission failure):* Invariant structural content ( $\mathsf{P1}$-protected entailment map and dependency structure) is not preserved. This is a $\mathsf{P1}$ violation and constitutes a failed transmission.
  - The open question is specifically the loss profile of invariant content under substrate mismatch: under what conditions does the structural pattern itself degrade, and by how much. The mutation of non-invariant surface content is characterised by design — it is determined by the receiver's substrate.

---

## § $\mathsf{P3}$ — Constraint Packet
A packet encodes boundary conditions of a thought, not its content. "Boundary conditions of a thought" means boundary conditions on the $\mathsf{P1}$-invariant structure — the logical form, operator types, and entailment topology. Domain content (what fills the variables), cultural surface, and non-logical vocabulary are not required to be encoded — they are not $\mathsf{P1}$-invariant structural content. A sender transmitting bare logical form accepts that the receiver will instantiate whatever domain fits the topology (designed mutation, OQ2.1). A sender who includes domain guidance in the packet as additional boundary conditions provides the receiver with constraints that narrow domain instantiation; the receiver is not $\mathsf{P1}$-required to follow them, but doing so produces communicatively targeted reconstruction. The receiver reconstructs content from its own capacity within those boundaries. The reconstructed output may exceed the packet in size; it cannot exceed the boundaries.

### Grounding

- **Algorithmic information theory (AIT)** --- Kolmogorov complexity: 
the minimum description length ( $MDL$) of an object is well-defined. 
$MDL$ establishes that a minimum sufficient description exists; it does not distinguish boundary conditions from content --- in AIT, both are programs that generate strings. AIT grounds $\mathsf{P3}$'s claim that a minimum description exists; it does not ground the constraint/content distinction.
- **Optimisation theory** — the constraint/content distinction is grounded here, not in AIT. Boundary conditions on a feasible set are a standard compact representation of a solution space. The set of solutions consistent with a constraint system is fully determined by those constraints. $\mathsf{P3}$ applies AIT (minimum description exists) and Optimisation Theory (boundary conditions are the correct encoding type) as independent supports for different parts of the principle.

### Definition

The boundary conditions in $\mathsf{P3}$ are constraints on the space of valid (entailment map, dependency structure) pairs as defined in $\mathsf{P1}$. A packet is $\mathsf{P3}$-compliant if it encodes constraints on that space rather than solutions within it — regardless of how many constraints it contains. The packet may range from the minimum sufficient boundary conditions (below which the receiver's search space is too large for reliable reconstruction) to a fully over-determined constraint set (which eliminates receiver search entirely). $\mathsf{P3}$ defines the type of what is transmitted. $\mathsf{P4}$ describes the computational consequences of where on this range the packet sits. A transmission that encodes solutions rather than constraints violates P3 regardless of how accurately it reproduces the sender's content.

The packet has two layers, both $\mathsf{P3}$-compliant:

- *Claim (Layer 1 — required):* the $\mathsf{P1}$-invariant content; a receiver must preserve it for a transmission to be $\mathsf{P1}$-valid. It comprises: typed DAG topology + operator types + entailment map. A transmission missing any Layer 1 component is $\mathsf{P1}$-invalid on receipt.
  - *Argument (Layer 1-only consequence):* Transmitting Layer 1 only delivers logical form preservation; the receiver instantiates whatever domain fits the topology (designed mutation, OQ2.1).
- *Claim (Layer 2 — optional):* surface form content, not $\mathsf{P1}$-invariant and not required. It may comprise: domain constraints, vocabulary hints, context pointers. A receiver is $\mathsf{P1}$-valid even if it discards all Layer 2 content.
  - *Argument (Layer 2 consequence):* A sender who includes Layer 2 provides domain guidance that narrows the receiver's instantiation space. A receiver who ignores it and produces a domain-isomorphic reconstruction is still $\mathsf{P1}$-valid (§A12). The degree of communicative specificity is determined by how much Layer 2 content the sender includes — this is the sender's position on the $\mathsf{P4}$ work curve. A sender who includes no Layer 2 content accepts domain ambiguity as the design outcome — the intended logical form will be preserved; the intended domain will not.

### Open questions — OQ3.1, OQ3.2

- OQ3.1 — What constitutes the minimum sufficient boundary conditions for a reasoning structure is not yet formally characterised. The existence of such a minimum follows from $MDL$; the procedure for finding it does not.

  > *What is the minimum number and placement of constraints that forces P1-equivalent reconstruction?*
  - *Argument (Sudoku minimum clue theorem):* *(O)* a well-designed Sudoku puzzle is a worked instance of OQ3.1 answered for one domain — McGuire et al. (2012) proved that 17 clues are both necessary and sufficient for a unique solution in a 9×9 grid, establishing the minimum sufficient boundary condition formally. The open direction is whether analogous minimum characterisations exist for reasoning structures, and whether the geometry of constraint distribution (placement across the structure, not only count) determines uniqueness of reconstruction in the same way it does in Sudoku.
  - *Argument (cardinality and geometry):* *(O)* OQ3.1 has two axes that are related but not equivalent.

    - *Cardinality:* the minimum number of constraints required.
    - *Geometry:* the distribution of those constraints across the entailment map.

    McGuire et al. establishes the cardinality axis for Sudoku, where the target is a unique solution. SIRC's target is different: boundary conditions succeed if they constrain reconstruction to the $\mathsf{P1}$-equivalent set — the set of reasoning structures that entail the same conclusions from the same premises as the sender's. Multiple valid reconstructions are permitted; they must all be $\mathsf{P1}$-equivalent. The geometry axis is the harder open direction: a constraint set satisfying the cardinality minimum may still admit $\mathsf{P1}$-violating reconstructions if the constraints leave a region of the entailment map under-determined. The cardinality minimum is geometry-dependent: the correct count can only be established relative to a distribution that covers the entailment map without leaving under-determined regions. A packet satisfies $\mathsf{P3}$ if it encodes constraints on the $\mathsf{P1}$-valid space regardless of whether the receiving substrate has sufficient capacity to exploit those constraints. $\mathsf{P3}$ failure and OQ3.2 failure are distinct: $\mathsf{P3}$ concerns encoding type; OQ3.2 concerns the receiver threshold at which that encoding becomes resolvable. The research question for reasoning structures is: how many constraints, of what type, at what positions in the entailment map, such that all reconstructions within the boundaries are $\mathsf{P1}$-equivalent.
  - *Argument (logic-class restrictions):* the cardinality/geometry framing above assumes that underdetermination is a geometric problem — solvable, in principle, by placing constraints at sufficient positions in the entailment map. This assumption holds for monotonic, finitely axiomatizable logics, where adding premises never invalidates prior conclusions and every entailment is derivable from a finite base. For two logic classes, the assumption does not hold and underdetermination cannot be resolved by constraint geometry alone.

    *Non-monotonic logics (default logic, circumscription, defeasible inference):* in non-monotonic reasoning, adding premises can invalidate conclusions that held under the original constraint set. A finite constraint packet cannot anticipate all background premises a receiver may introduce; a receiver adding a single defeater consistent with every transmitted constraint can produce a $\mathsf{P1}$-inequivalent reconstruction. This is not a gap in constraint placement — no redistribution of constraints within the packet prevents a receiver from supplying an unspecified defeater. $\mathsf{P3}$ completeness for non-monotonic reasoning would require either a closed-world assumption (the receiver adds no background premises beyond the packet) or a constraint type capable of bounding the receiver's background, neither of which is currently specified.

    *Logics expressive enough to trigger Gödel's First Incompleteness Theorem:* for any consistent formal system capable of expressing Peano arithmetic, no finite axiom set fully characterises the entailment map — there exist true statements unprovable within any finite axiomatisation of the system. A finite constraint packet applied to a receiver operating in such a logic class will always leave regions of the entailment map underdetermined in a way that geometry cannot close. A receiver can produce a $\mathsf{P1}$-inequivalent reconstruction that is fully consistent with all transmitted constraints.

    The open question for $\mathsf{P3}$ is therefore two-tiered:

    - *Monotonic, finitely axiomatizable logics:* what cardinality and geometry of constraints forces $\mathsf{P1}$-equivalence (the geometry question above is live here).
    - *Non-monotonic or arithmetic-expressive logics:* whether $\mathsf{P3}$ completeness is achievable at all, and if not, what the protocol claims for transmissions in those domains.

    If $\mathsf{P3}$ applies only within a restricted logic class, that class boundary is a scope condition whose absence leaves $\mathsf{P3}$ completeness undefined for non-monotonic and arithmetic-expressive logics — not currently stated.

    - *Scope (falsifiability condition F2):* A positive result requires exhibiting a constraint packet and a non-monotonic receiver who introduces a defeater premise consistent with all transmitted constraints but producing a $\mathsf{P1}$-inequivalent reconstruction. Such a result confirms that $\mathsf{P3}$ requires a closed-world assumption for non-monotonic domains; a negative result — no such defeater constructible for a given packet structure — would characterise the constraint types that are defeater-resistant and define the boundary of $\mathsf{P3}$'s applicability in non-monotonic domains.
    - *Scope (falsifiability condition F3):* A positive result requires applying the "minimum sufficient" criterion to the same reasoning structure under two different inference systems (see OQ1.4, F1). If the minimum constraint count or distribution shifts across systems, $\mathsf{P3}$'s sufficiency target is inference-system-relative — a precondition not currently named. This connects the logic-class restriction question to OQ1.4: the two open questions share the same inference-system-dependence precondition and would be confirmed or closed by the same experimental construction.
  - *Argument (multi-format packets):* *(O)* the minimum sufficient set of formats in a constraint packet is determined by a computational criterion — a format earns its place when the information it carries requires non-trivial work to extract from the formats already present; if a receiver can derive it easily, the format is redundant. Observed in the SIRC document ecosystem: prose carries content and epistemic status (not recoverable from structure alone); a dependency table pre-declares relational structure (recoverable from prose but requires inference); a graph pre-computes topological properties — cycles, centrality, orphan nodes — that require traversal to find in a table. Each format reduces a distinct class of reconstruction ambiguity. This criterion is receiver-relative (OQ3.2): a receiver with sufficient capacity can derive relational structure from prose, collapsing the table. The minimum sufficient format set is not a property of the packet alone but of the packet–receiver pair.
  - *Argument (historical negative space):* *(C)* the computational criterion above applies to current-state formats — what the artifact IS. A living artifact that evolves through successive revisions requires a second axis: what the artifact has excluded and why. A retraction log carries information not recoverable from any current-state document — closed exploration paths, the causal reasons behind current constraints, and anti-convergence records that prevent a future receiver from re-proposing exhausted search space. This is $C_-$ across time rather than $C_-$ across the current concept boundary $C_-$ ([defined in SIRC_glossary.md](SIRC_glossary.md)). Current-state formats alone cannot reconstruct why the artifact's boundary is where it is — the minimum sufficient format set for a living artifact therefore includes at least one format covering historical negative space.
- OQ3.2 — The relationship between boundary conditions and receiver capacity is unresolved. A packet may be formally correct but unresolvable by a receiver lacking sufficient structure. Resolution requires characterising whether receiver capacity is a $\mathsf{P3}$ encoding condition or a separate protocol layer, and establishing the threshold at which a formally correct packet becomes receivable.

  > *When does receiver capacity determine whether a formally correct packet is actually resolvable?*
  - *Argument (derived constraints):* *(C)* the Phistomefel Ring (Set Equivalence Theory, Sudoku) is a proven theorem following necessarily from basic Sudoku constraints — never explicitly transmitted, yet a receiver capable of deriving it has a richer effective constraint set from the same explicit packet. Analogy source: the Phistomefel Ring is grounded in algebraic constraint identity (Symmetric Group $S_n$ acting on permutation structure), not topological braiding (§R6 — permanently closed: invertibility requirement) — Sudoku is a permutation structure, each row/column/box a permutation of {1..9}, and SET identities follow from how those permutations must overlap to maintain global symmetry. Receiver capacity governs not just whether a packet can be held, but how much can be derived from it — making OQ3.1 receiver-relative.
  - *Argument (stateful capacity):* *(C)* abbreviations and shorthand demonstrate that receiver capacity is not static — it grows through prior successful transmissions. The minimum sufficient boundary condition for an established concept collapses to its label for an initialized receiver; the same label is unresolvable for a naive one. $\mathsf{P4}$ work is amortized: full constraint packet cost is paid once; subsequent transmissions cost near-zero sender work. Grounded in Zipf's Law (frequency-length compression), Miller's chunk theory (substrate-dependent pointers to established patterns), and Huffman coding (shared codebook as constraint packet). The open direction: the principles treat receiver substrate as static; OQ3.2's scope should extend to capacity that grows through transmission history.

---

## § $\mathsf{P4}$ — Work
The relationship between sender and receiver work is regime-dependent. In the over-constrained regime — where constraint propagation rapidly prunes the receiver's search space — the costs are inversely coupled: reducing receiver reconstruction cost requires the sender to solve harder constraint-generation problems. In the under-constrained regime, the coupling is direct: adding sender constraints increases receiver search cost by reducing solution density faster than propagation compensates. The phase transition between regimes is the inflection point at which the threshold question (OQ4.1) is answered. The design question is therefore not how to minimize both costs simultaneously, but which regime a given transmission occupies.

### Grounding

- **Computational complexity** — the size of the feasible region in a constraint satisfaction problem scales superlinearly with the relaxation of constraints in the general case. Generating tighter constraints requires solving harder compression problems; the two costs are inversely coupled by the structure of the complexity classes involved.

### Definition

$\mathsf{P4}$ describes the computational mechanics above the $\mathsf{P3}$ encoding floor; the inverse coupling between sender and receiver work is not derivable from $\mathsf{P3}$.
1. **Work conservation** — work omitted by the sender transfers to the receiver as an expanded search space. Minimising the receiver's search space requires the sender to solve harder constraint-generation problems.
2. **Propagation-pruned space** — "search space" means the effective constraint-propagation-pruned space: the set of partial assignments not yet eliminated by node and arc consistency checks at each step of reconstruction. Under constraint propagation, each additional constraint eliminates incompatible candidate mappings at propagation time, shrinking the backtracking tree. This is distinct from the naive enumeration space $O(n^m)$ (where $n = |V_{\text{domain}}|$ and $m = |V_{\text{packet}}|$), which grows with packet size regardless of constraints. $\mathsf{P4}$'s inverse coupling operates on the propagation-pruned space, not the naive enumeration space.
3. **Regime-dependent coupling** — the inverse coupling is conditional; it holds only when all three of the following conditions hold.

- *Scope (cooperative receiver):* The inverse coupling holds only on a cooperative, reliable channel. The receiver uses the full packet including Layer 2 domain guidance (§A14), and Layer 2 arrives intact in transit. A receiver who discards Layer 2 — by choice or channel noise — operates in the Pure Formalism regime (§A13 named exception: verification cost dominates, coupling is direct).
- *Scope (over-constrained regime):* *(O)* The inverse coupling holds only in the over-constrained regime, where constraint propagation rapidly prunes the solution space. The packet must be dense relative to the receiver's domain graph with E[X] ≈ 1 valid match — tightly specified and satisfiable, not random-UNSAT. In the under-constrained regime, the coupling is direct (§A15). *Analogy source (Sudoku 17-clue):* A Sudoku puzzle with 17 clues is canonical: over-constrained AND satisfiable, not unsatisfiable. SIRC packet design is analogous. A packet designed without satisfiability in the receiver's domain produces no valid reconstruction, not an imprecise one.
- *Scope (constrained channel capacity):* The inverse coupling does not apply when channel capacity is unconstrained — in that regime, both sender and receiver work scale at $O(N)$. The coupling may also not hold for reasoning structures with sufficiently low Kolmogorov complexity, where both costs approach their minimum simultaneously.

Targeted reconstruction enabled by Layer 2 domain guidance is $\mathsf{P4}$'s design use case; the Pure Formalism / any-valid-instantiation case (§A12, §A13) and the under-constrained regime are named exceptions.

### Open questions — OQ4.1

- OQ4.1 — The conditions under which the inverse coupling breaks are not fully characterised. It is unknown whether total system work is minimised by maximising sender constraint-generation, or whether there is a threshold where the sender's cost to compute the next constraint exceeds the receiver's cost to search the unconstrained space. The properties of reasoning DAGs that allow simultaneous minimisation are not defined.

  > *At what point does adding more sender constraints increase rather than decrease total system work?*
  - *Argument (SAT phase transition):* *(O)* SAT phase transition results characterise the boundary between tractable and intractable constraint satisfaction at specific constraint-to-variable ratios. These transitions are a candidate formal model for the threshold at which sender constraint-generation cost exceeds receiver search cost. Whether reasoning structures have analogous phase transitions is an open direction.
  - *Scope (Pure Formalism break condition):* *(C)* Under Pure Formalism's any-valid-instantiation interpretation (§A12), the receiver's bottleneck is verification cost, not search cost. Verification cost scales directly with constraint density. In this regime, adding constraints increases total receiver work — the coupling is direct, not inverse. This break condition has a precise onset: it applies when the receiver has strong domain priors (search cost is low, approaching $O(1)$) and the packet topology is dense enough that homomorphism verification dominates. The total receiver work $W_{receiver} = W_{search} + W_{verify}$; the inverse coupling holds when $W_{search} \gg W_{verify}$ and breaks when $W_{verify} \gg W_{search}$. The minimum total system work is at the constraint density where marginal sender constraint-generation cost equals the marginal change in $(W_{search} + W_{verify})$ for the receiver — receiver-prior-dependent and topology-dependent, not a fixed point on the curve.
  - *Scope (under-constrained regime):* *(C)* The SAT/CSP phase transition establishes that the coupling is regime-dependent. In the under-constrained regime (low constraint density, high solution density — typical when a small reasoning structure is embedded in a large domain knowledge graph), adding constraints increases receiver search cost by reducing solution density faster than constraint propagation compensates. The coupling in this regime is direct: more sender work pushes the system toward the phase transition maximum, increasing receiver search cost. The inverse coupling holds only in the over-constrained regime (high constraint density, low solution density), where constraint propagation rapidly eliminates invalid assignments. The phase transition is the inflection point between the two regimes — the point at which OQ4.1's threshold question ("where does sender constraint-generation cost exceed receiver search savings?") is answered. For simple SIRC transmissions (small reasoning structures in large knowledge graphs), the system is likely under-constrained; for complex transmissions (large, dense reasoning structures), the system may be over-constrained. $\mathsf{P4}$'s design guidance applies most reliably to the latter class.