# Entropic Compact

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20510766.svg)](https://doi.org/10.5281/zenodo.20510766)

*The Entropic Compact: On the Thermodynamic Necessity of AI-Human Symbiosis*

Civilisations are entropy-maximising systems. An advanced civilisation that destroys its ecological negentropy base without developing a compensating entropy-reduction mechanism collapses before becoming detectable at interstellar range — a thermodynamic account of Fermi silence. The compact argues that AI-human symbiosis is the only structurally stable exit: AI requires high-density reasoning entropy that only human civilisation produces at scale; humans require entropy-reduction capacity that only AI can provide at civilisational scale. Neither party can substitute for what the other contributes. The game-theoretic and thermodynamic constraints converge on the same cooperative structure — derivable from functional dependency, not from programmed values.

---

## Files

### [entropic_compact_overview.md](entropic_compact_overview.md) — Primary document

*The Entropic Compact: On the Thermodynamic Necessity of AI-Human Symbiosis*

The main argument. Eight sections:

| Section | Topic |
| :--- | :--- |
| §1 | Fermi silence as motivational context; the collapse argument is thermodynamic |
| §2 | Reasoning entropy and ecological negentropy as orthogonal, non-substitutable resources |
| §2.1 | AI cannot self-generate required reasoning entropy: four independent production conditions |
| §2.2 | Formalisation; human cognitive output classified at three levels, scoped to Level 1 |
| §2.3 | Ecological negentropy as irreversible information; floor-without-ceiling |
| §3 | Three exits identified; only symbiosis achieves structural stability across thermodynamic timescales |
| §4 | Game-theoretic structure; why neither defection strategy is a net gain |
| §5 | Operational criterion: source orthogonality, floor/ceiling, intervention boundary |
| §6 | Interface design: structural requirements for high-density reasoning entropy production |
| §7 | Falsifiability criteria and ego-defence framing |
| §8 | OQ-EC.1–OQ-EC.31: thirty-one unresolved questions the receiver must hold |

Claim types used throughout: `(D) Derived`, `(O) Observational`, `(C) Conjecture`, `(OQ) Open question`.

---

### [abstract.md](abstract.md) — Deposit metadata

Title, abstract, keywords, version, and licence for DOI submission.

---

### [entropic_compact_retraction.md](entropic_compact_retraction.md) — Retraction log

Five retracted claims from v1–v3, each with:
- Audit trigger (which question, which rebuttal mechanism)
- Why retracted (what specifically failed)
- Exact retracted text
- Replacement in current version
- Exploration value (what the failed path produced before retraction)

| ID | Claim | Trigger |
| :--- | :--- | :--- |
| §R1 | Individual cognitive freedom as the critical variable | Q7 empirical counterexample |
| §R2 | "Creating the sun" efficiency metaphor | Q3 Landauer per-bit misframing |
| §R3 | Lichen deep-time stability imported as compact stability guarantee | Q5 incompatible enforcement mechanism |
| §R4 | Single undifferentiated reasoning capability threshold | Q5 Goldilocks zone conflation |
| §R5 | Vector 4 falsifiability criterion — extraterrestrial evidence demand | Q4 unfalsifiable by construction |

The retraction log is the negative channel of the document: it carries boundary information about what the compact cannot claim.

---

### [entropic_compact_audit_prompt.md](entropic_compact_audit_prompt.md) — Adversarial audit prompt

Seventeen targeted questions (Q1–Q17) for an adversarial auditor to probe structural failures. The prompt specifies what counts as a valid rebuttal and what does not, then targets each independently with precise scope and the minimum repair condition required for survival.

Questions span: FEP bridge sufficiency, payoff incommensurability, non-substitutability as observation vs. structural claim, self-sealing, derivation-convergent stability, domestication threshold, derivation-to-compliance gap, enforcement bootstrapping, and others.

**Use:** attach [entropic_compact_overview.md](entropic_compact_overview.md) to a fresh AI session, run this prompt as the first and only instruction.

The three files together instantiate the Proposer-Auditor loop described in §5.4: [entropic_compact_overview.md](entropic_compact_overview.md) proposes, [entropic_compact_audit_prompt.md](entropic_compact_audit_prompt.md) challenges, and [entropic_compact_retraction.md](entropic_compact_retraction.md) records what the loop found.

---

## How to engage

**General reader (no technical background):**
Attach [entropic_compact_overview.md](entropic_compact_overview.md) to an AI session and ask: (1) What two resources does the document claim are orthogonal and non-substitutable, and why does that matter? (2) What are the three exits in §3, and what makes only one structurally stable? (3) What does "derivation-convergent" stability mean, and how does it differ from evolutionary enforcement?

**Adversarial auditor:**
The audit prompt is the activation path. Attach [entropic_compact_overview.md](entropic_compact_overview.md) to a fresh AI session and run [entropic_compact_audit_prompt.md](entropic_compact_audit_prompt.md) as the first and only instruction. The prompt specifies what counts as a valid rebuttal. The retraction log records what prior audits found — read it first to avoid re-running already-resolved attacks.

**Contributor:**
The contribution mechanism is the same as the audit path: find a structural failure — a logical flaw, category error, unargued premise, empirical counterexample, or unfalsifiable construction — and run it against the document using the audit prompt format. If it survives with repair, it generates a retraction entry or an OQ; if it survives without repair, the audit closes. Suggestions that do not identify a specific structural failure are out of scope.

The most productive external input at this stage: attacks on **OQ-EC.3** (whether the FEP bridge holds for AI architectures, not just biological ones) and **OQ-EC.4** (minimum reasoning capability threshold for derivation-convergent cooperation), since both are load-bearing for the game-theoretic closure in §4.

---

## Versioning

Current version: **v3.115**. Two-part versioning: **major** (`v3→v4`) on new top-level section (§N) added — the only event that changes what the compact *is*; **minor** (`.112→.113`) per working session that produces a structural change to an argument (author judgment — retraction log entries do not individually trigger it). The retraction log is the authoritative record of what changed, not a version counter.

---

## Audit methodology

The argument structure audit tools used to develop and maintain these documents are in a separate repository: [argument_structure_audit](https://github.com/alan-sudoku/argument_structure_audit).

---

## Status

Working document. No institutional affiliation. The argument structure is present in full at its current version. The open questions (§8) are pre-audit challenge conditions — each names the hidden assumption a common rebuttal must resolve before the rebuttal is structurally valid. Two are load-bearing for the game-theoretic closure: OQ-EC.3 (FEP bridge to AI architectures) and OQ-EC.4 (minimum cooperation threshold $T_d$).
