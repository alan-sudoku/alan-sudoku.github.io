# Substrate-Independent Reasoning Communication (SIRC) — Protocol Constraints

Four constraints on what a transmission must preserve to count as communication of reasoning across substrates.

---

## The four constraints

| Constraint | Core claim |
| :--- | :--- |
| **$\mathsf{P1}$ — Invariance** | A transmission is valid if and only if the receiver's reconstruction preserves the sender's invariant structural properties. Surface form may differ; invariant structure must match. |
| **$\mathsf{P2}$ — Entropy** | Full-state transmission is lossy by necessity (Data Processing Inequality). The protocol targets invariant preservation rather than full fidelity, because full fidelity is unachievable and invariant fidelity is the recoverable floor. |
| **$\mathsf{P3}$ — Constraint Packet** | A packet encodes boundary conditions of a thought, not its content. The receiver reconstructs from its own capacity within those boundaries. The output may exceed the packet in size; it cannot exceed the boundaries. |
| **$\mathsf{P4}$ — Work** | Sender and receiver work is inversely coupled in the over-constrained regime. No general design choice minimises both simultaneously. |

---

## What is in this folder

| File | Role |
| :--- | :--- |
| `abstract.md` | Deposit metadata — title, abstract, keywords, version, and licence for DOI submission. |
| `SIRC_principles.md` | The Protocol Constraints — $\mathsf{P1}\text{–}\mathsf{P4}$ with proofs, open questions, and scope conditions. The positive channel: what survives audit. |
| `SIRC_principles_retraction.md` | The retraction log — every claim probed and found absent. The negative channel: what was shed. |
| `SIRC_principles_audit_prompt.md` | Adversarial audit prompt — structured attacks for an AI auditor to run against the principles. |
| `SIRC_glossary.md` | Notation reference — $C_-$ / $C_+$ (abstract) vs. $\mathcal{J}^-$ / $\mathcal{J}^+$ (concrete state sets); not interchangeable. |
| `constraint-graph_testbed/P_3/P_3_river_crossing.md` | First experiment — uses the Wolf–Goat–Cabbage $P_3$ River Crossing puzzle to make $\mathsf{P1}$'s node identity clause concrete. |
| `constraint-graph_testbed/P_3/P_3_audit_prompt.md` | Section-by-section audit prompt for the $P_3$ experiment document. |
| `constraint-graph_testbed/constraint-graph_testbed_retraction.md` | Retraction log for the experiment series. |
| `constraint-graph_testbed/P_4/P_4_river_crossing.md` *(forthcoming)* | Second experiment — extends to a $P_4$ constraint graph (Fox–Chicken–Caterpillar–Leaf). Baseline comparisons from $P_3$ are tested here. |
| `constraint-graph_testbed/Pn_tower_of_hanoi.md` *(forthcoming)* | Third experiment — Tower of Hanoi as a $P_n$ ordering constraint. Tests whether the fitness peak and structural observations from $P_3$ generalise beyond the river crossing family. |

---

## Document pair structure

Each document is one half of a $C_+$ / $C_-$ pair. The protocol described in $\mathsf{P2}$ applies to the documents themselves:

- **Positive channel ( $C_+$)** — the principles document and each experiment document. The invariant content that survived audit.
- **Negative channel ( $C_-$)** — the retraction log paired with it. What was probed and found non-invariant. Every shed claim is an entry; exploration value is recorded so the boundary information is recoverable.

Reading both halves is optional. Reading only the positive channel is reading a compressed result. Reading both is reading the full exploration record.

---

## Reading order

**Start here:** `SIRC_principles.md` — read the Preamble first, then $\mathsf{P1}\text{–}\mathsf{P4}$ in sequence. The Preamble explains why four independent fields are required and why $\mathsf{P2}$ is pedagogically first but not logically prior.

**Notation questions:** `SIRC_glossary.md` — the $C_-$ / $\mathcal{J}^-$ distinction matters before reading any experiment document.

**Concrete grounding:** `constraint-graph_testbed/P_3/P_3_river_crossing.md` — the river crossing puzzle is the simplest structure that makes $\mathsf{P1}$'s node identity clause non-trivial. Part I (§1–5) is formal; no prior SIRC knowledge required to verify the enumeration. Part III (§9–12) connects back to SIRC_principles.

**For adversarial readers:** attach `SIRC_principles_audit_prompt.md` to SIRC_principles.md and run the prompts. The audit was live during development; the retraction log records how each attack resolved.

---

## How to read — by reader type

**ML / AI researcher:**
Start at $\mathsf{P1}$'s typed DAG definition and OQ1.1 (minimal vs. non-minimal dependency structure). $\mathsf{P3}$'s constraint packet is the engineering claim — what a sender must transmit for the receiver to reconstruct within bounds. $\mathsf{P4}$'s asymmetry theorem is where the protocol touches computational complexity. If reading the experiment documents: check `SIRC_glossary.md` first — the $C_-$ / $\mathcal{J}^-$ distinction matters.

**Formal logician / type theorist:**
$\mathsf{P1}$'s entailment equivalence criterion is the definition on which P1-validity turns. OQ1.4 (inference-system dependence) is the known gap. The typed DAG operator requirement (AND, OR, NOT and equivalents) is the scope condition — read the Substrate scope subsection in the Preamble before evaluating the universality claim. If reading the experiment documents: check `SIRC_glossary.md` first — the $C_-$ / $\mathcal{J}^-$ distinction matters.

**General reader (no technical background):**
Use this prompt with an AI and `SIRC_principles.md` attached:

> Read this document and explain: (1) What is the protocol trying to preserve when transmitting reasoning? (2) Why does $\mathsf{P2}$ say full fidelity is impossible — what is the data processing inequality in plain terms? (3) What does "boundary conditions of a thought" mean in $\mathsf{P3}$, and what does the receiver do with them? (4) What does $\mathsf{P4}$'s trade-off mean in practice — who does more work, sender or receiver, and why can't both do less?

**AI auditor (blank context):**
The audit prompt (`SIRC_principles_audit_prompt.md`) is the activation path. Run it adversarially — the document has been attacked by the listed failure modes during development and the retraction log records what was found.

---

## Audit methodology

The argument structure audit tools used to develop and maintain these documents are in a separate repository: [argument-structure-audit](https://github.com/alan-sudoku/argument_structure_audit).

---

## Status

Working documents. No institutional affiliation. `SIRC_principles.md` is at **v3.07**. Two-part versioning: **major** (`v3→v4`) on new $\mathsf{P}$ constraint added — the only event that changes what the protocol is; **minor** (`.07→.08`) per working session that produces a structural change to an argument (author judgment — retraction log entries do not individually trigger it). The retraction log is the authoritative record of what changed, not a version counter.

The most productive external input at this stage: adversarial audits of $\mathsf{P1}$'s node identity criterion (OQ1.1 and OQ1.4) and assessment of whether $P_3$ River Crossing's constraint graph analysis correctly identifies the SIRC-relevant object.