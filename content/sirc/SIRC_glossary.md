# SIRC Glossary

Cross-document vocabulary. Each entry names the authoritative source; definitions here are distillations for point-of-use reference.

---

## Notation: negative and positive channels

Two notations are in use across the SIRC document set. They are **not interchangeable**.

| Notation | Level | Where used | Meaning |
|:---|:---|:---|:---|
| $C_- $, $C_+$ (subscript) | Abstract / concept-level | `SIRC_principles.md` | Concept structure: $C_-$ is the negative boundary the sender encodes; $C_+$ is the invariant content the receiver reconstructs. Applies to all SIRC transmissions. |
| $\mathcal{J}^- $, $\mathcal{J}^+$ (superscript, mathcal J) | Concrete / state-set | testbed documents | Enumerated sets: $\mathcal{J}^-$ is the retracted state set (states ruled out by applying constraint rules to the state space); $\mathcal{J}^+$ is the complement set of valid states. Applies only to finite puzzle testbeds. $\mathcal{J}$ is used specifically to avoid collision with the abstract $C_-$ / $C_+$ notation and has no established meaning in the fields SIRC spans. |

Source: `SIRC_principles.md` § $\mathsf{P3}$ (abstract channel usage) and the constraint-graph experiment documents (concrete state-set usage).

### Entries

| Symbol | Term | Definition |
|:---|:---|:---|
| $C_-$ | Negative channel (abstract) | The negative boundary the sender encodes — what a concept excludes. Carried by failed probes, retracted claims, and closed exploration paths. Constrains the receiver's search space by eliminating what the concept cannot be. At document level: the retraction log is the $C_-$ of the principles document. |
| $C_+$ | Positive channel (abstract) | The invariant content that survives audit — what the receiver reconstructs. At document level: `SIRC_principles.md` is the $C_+$ of the document pair. |
| $\mathcal{J}^-$ | Retracted state set (concrete) | The enumerated set of states ruled out when constraint rules are applied to a finite state space. Used in testbed documents only. Note: $\mathcal{J}^-$ is the *extension* (the generated excluded set) — it is not what is transmitted. The transmitted object is $\mathcal{R}$ (the constraint rules, the intension). Relationship: $\mathcal{J}^- = \{ s \in \mathcal{S} \mid \mathcal{R}(s) = \text{invalid} \}$. Abstract $C_-$ maps to $\mathcal{R}$ in the concrete case, not to $\mathcal{J}^- $. (Example from the river crossing puzzle: $\mathcal{R}$ = 2 predation rules transmitted; $\mathcal{J}^-$ = 6 retracted states derived by the receiver — the rules are the packet, the retracted set is the result.) |
| $\mathcal{J}^+$ | Valid state set (concrete) | The complement of $\mathcal{J}^-$ — the set of states consistent with all constraints. Used in testbed documents only. |
