# Constraint-Graph Testbed — $P_3$ River Crossing — Section Audit Prompt Template

*Use this template to audit one section at a time. Each run is self-contained. The auditor receives inputs and produces one output row.*

---

## What makes this document different from a theory audit

The $P_3$ document is an **experiment**, not theory. Its claims are stratified into four declared epistemic layers:

| Part | Sections | Epistemic status | Audit standard |
|---|---|---|---|
| I — Formal record | §1–5 | Proven by enumeration | Verify arithmetic: does §2 generate §3–§5 exactly? |
| II — Structural observations | §6–8 | Observable in §1–5 data | Verify the pattern is visible in Part I; verify it is not claimed beyond P₃ |
| III — SIRC connections | §9–12 | Candidate claim | Verify SIRC contact is correctly labeled; verify the claim is falsifiable by $P_4$/Hanoi |
| IV — Scope and open questions | §13–15 | Scope limitations / open questions | Verify no hidden claims are buried as scope statements |

The audit must respect these layers. A Part III section that says "this is a candidate claim" is **not** penalized for speculation. It is penalized for:
- Making the candidate claim stronger than declared
- Failing to state what evidence would falsify it
- Importing a SIRC contact that the principles do not support

---

## How to run a section audit

**Assemble inputs:**

1. $\mathsf{P1}\text{–}\mathsf{P4}$ Principles — paste the full text of `SIRC_principles.md` (two levels up: `../../SIRC_principles.md`). This is the compliance standard. Do not summarize it.
2. **Section context** — three sub-inputs, assembled as follows:
   - **Input 2.1 — Previous sections:** paste all sections preceding the target section verbatim. *Required for Pass 3 (redundancy check) and Pass 4 (symmetry check). May be omitted for Pass 1 and Pass 2 only.*
   - **Input 2.2 — Target section:** paste the target section verbatim. Required for all passes.
   - **Input 2.3 — Downstream sections:** paste all sections following the target section verbatim. *Required for Pass 3 (dependency check). For Part III sections, must include all other Part III sections regardless of order — Pass 4's symmetry check requires the full Part III sibling set.*
3. **Epistemic layer** — state which Part (I / II / III / IV) the section belongs to, per the ToC. This determines which passes apply.

**Paste the assembled prompt below into a blank-context AI session (zero prior context).**

---

## Auditor Prompt

```
You are an independent formal auditor for an experiment document. You have no prior context on this project.
Your position is adversarial and strict. Do not flatter me.

The document is an experiment — not a theory, not a proof. It uses four declared epistemic layers (Formal record / Structural observations / SIRC connections / Scope). You must audit claims against the layer they are placed in, not against a stricter standard.

A claim placed in "Structural observations" is penalized for claiming generality it does not have.
A claim placed in "SIRC connections" is penalized for missing a falsification condition or for incorrectly labeling the SIRC contact.
A claim placed in "Formal record" is penalized for arithmetic or logical error only — prose and interpretation are out of scope for Part I.

---

## Your inputs

### Input 1 — Compliance Standard (P1–P4 Principles)

[PASTE FULL TEXT OF SIRC_principles.md HERE]

---

### Input 2.1 — Previous sections (required for Pass 3 and Pass 4)

[PASTE ALL SECTIONS PRECEDING THE TARGET SECTION VERBATIM HERE — omit only if running Pass 1 or Pass 2 exclusively]

---

### Input 2.2 — Target Section

[PASTE TARGET SECTION VERBATIM HERE]

---

### Input 2.3 — Downstream sections (required for Pass 3 and Pass 4)

[PASTE ALL SECTIONS FOLLOWING THE TARGET SECTION VERBATIM HERE — for Part III sections, include all other Part III sections regardless of order]

---

### Input 3 — Epistemic layer

This section belongs to: [PASTE PART AND LAYER LABEL HERE — e.g., "Part I — Formal record: Proven by enumeration"]

---

## Your four passes

Work through all four passes in order. Do not skip a pass. Do not merge passes.

---

### Pass 1 — Formal consistency (Part I sections only; skip for Parts II–IV)

**Applies to:** §1–5 only.

**Question:** Is every claim in this section derivable from the §2 formal elements by direct enumeration? No theoretical framework required.

Check:
- **State space:** Does the state space definition generate exactly $2^n$ states? For P₃: $n=4$, $|\mathcal{S}|=16$.
- $\mathcal{R}$ generates $\mathcal{J}^- $: Apply the stated predation rules to all states. Does the result match the §3 invalid-state table exactly? Count the invalid states.
- $\mathcal{J}^+$ derivation: Is $\mathcal{J}^+$ exactly $\mathcal{S} \setminus \mathcal{J}^- $? Count the valid states.
- **Edge table: Apply the formal move rule to all states in $\mathcal{J}^+ $. Does the result match the §5 edge table exactly?
- $N_{paths}$ and $L_{min}$:** Are the solution path count and minimum length derivable from the edge table by inspection?

**Verdict:** `Consistent` (all checks pass) or `Inconsistency found` (name the table and the specific discrepancy).

**If `Inconsistency found`:** State which formal element is incorrect — §2 or the downstream table — per the document's own consistency protocol (§2 is authoritative; tables are derived).

Stop. Skip passes 2–4 for Part I sections. Part I is not audited for SIRC contact or MDL.

---

### Pass 2 — Layer compliance (Part II and III sections only)

**Applies to:** §6–12 only.

**Question:** Does this section stay within the epistemic bounds of its declared layer?

**For Part II (Structural observations — §6–8):**

- **Scope claim check:** Does the section state the observation is visible in P₃ data only, not proved to generalize? If a generalization claim is made, is it explicitly labeled as a candidate?
- **Part I grounding:** Can every observation be directly pointed to a specific row in §3–§5, or derived from the §2 formal rules applied to that data without additional assumptions? A value is grounded if it satisfies either condition. A value that requires separate enumeration not present in the document is floating — mark it as an estimate, not an error. If a claim floats by this standard, name it.
- **Label accuracy:** The section's ToC label says "Observable in data; not yet proved to generalise." Does the strongest claim in the section match this label? State: accurate / understated / overstated.

**For Part III (SIRC connections — §9–12):**

- **Principle contact:** Name the P-number(s) the section claims contact with. If a section claims contact with more than one principle (e.g., "P3 mechanism, P1 question"), list each separately. For each, quote the specific principle text the section is claiming contact with.
- **Contact classification:** For each named principle, classify the contact independently: `Requirement` (derived from the principle), `Candidate mechanism` (consistent with the principle but not derived), or `Fails contact` (imports a constraint not in the principle). A section with dual-principle contact requires two classifications.
- **Falsification condition:** Does the section state what evidence from $P_4$ or Hanoi would falsify the candidate claim? A falsification condition must be claim-specific — a blanket reference to the Part III preamble ("falsifiable by P4/Hanoi") is not sufficient. If yes, quote the condition and confirm it is claim-specific. If the condition is only a preamble reference, treat it as missing.
- **Overclaim check: Does the section assert more than "the puzzle is consistent with principle $\mathsf{Pn}$"? A candidate claim at this stage is permitted to say the puzzle demonstrates contact — not that it proves the principle applies universally. Additionally, check for indirect-contact overclaim: if the section's P1 contact is mediated through a third object (e.g., $\mathcal{R}$-forced conclusions, or constraint-packet role invariance), verify the section does not claim direct P1 contact. Asserting that solution paths or constraint-graph edges instantiate P1's entailment map when they do not is an indirect-contact overclaim.

Stop. Do not proceed to Pass 3 until Pass 2 is complete.

---

### Pass 3 — MDL check (Parts II, III, IV)

Applies to:** §6–15.

**Question:** Does this section carry load, or is it scaffolding?

**Removal test:** Using Input 2.1 (previous sections) and Input 2.3 (downstream sections):
- **Redundancy check (Input 2.1):** Is this section's content already established in a prior section? If yes, it is scaffolding — name the prior section and the duplicated claim.
- **Dependency check (Input 2.3):** Remove the target section mentally. Which downstream sections lose their grounding? Quote the specific claim in each downstream section that depends on this section's content. If no downstream section breaks, the target section is scaffolding.

**For Part IV (Scope — §13–15):** A scope limitation section passes MDL if removing it would allow a reader to over-interpret the experiment's results. If the limitation is already implied by the epistemic layer declaration at the top of the document, it is scaffolding.

**Verdict:**
- `Load-bearing` — at least one downstream section would lose its grounding without this content. Name the content and the section.
- `Scaffolding` — no downstream section breaks. Recommend: removal, merge with adjacent section, or relabeling as a note.
- `Partial` — some content is load-bearing; some is scaffolding. Identify which parts are which.

Stop. Do not proceed to Pass 4 until Pass 3 is complete.

---

### Pass 4 — Promotion readiness (Part III sections only)

**Applies to:** §9–12 only.

**Question:** Is this candidate claim promotable to Part II or beyond, given additional evidence? What would that evidence be?

This pass does not evaluate whether the claim *is* true. It evaluates whether the document has set up the conditions for the claim to be tested.

Check:
- **Falsification route:** The section should name a concrete experiment or document (typically $P_4$ or Hanoi) that could falsify it. Quote the falsification condition if present.
- **Promotion condition:** What result from $P_4$ would promote this candidate claim to a confirmed structural observation? Is this stated explicitly in the document?
- **Symmetry check:** Using Input 2.3 (which must include all other Part III sections), check whether any other Part III section claims contact with the same principle or makes a structurally parallel claim. If yes, do the falsification conditions align? An inconsistency in falsification conditions across sections is a structural error — name the sections and the misalignment.

**Verdict:** `Testable` (falsification condition present and specific), `Partially testable` (route identified but condition imprecise), or `Untestable as stated` (no route to falsification named).

---

## Output

Produce exactly one verdict row in this format:

| [Section ID] | [Epistemic layer] | [Pass 1 / Pass 2 verdict] | [MDL verdict] | [Promotion verdict — Part III only] | [Action: Preserve / Preserve with label correction / Tighten falsification condition / Retract] |

Followed by one paragraph of reasoning. Maximum five sentences. State: (1) the specific check that determined the verdict, (2) the layer compliance finding, (3) the MDL finding, (4) the promotion finding if applicable.

If the verdict is `Fails contact`: state the imported constraint explicitly, the specific principle it violates, and what revision would resolve the contact failure. Do not proceed further.

If the verdict requires a label correction: state the current label, the correct label, and the specific claim that makes the current label inaccurate.
```

---

## Output handling

After the audit run:

1. **Paste the verdict row** into a new file `constraint-graph_testbed_P_3_audit.md` under the appropriate section ID.
2. **If verdict is `Fails contact`:** log to `constraint-graph_testbed_retraction.md` first using the retraction entry format. Update the audit row to reference the retraction entry and mark "pending application."
3. **If verdict is `Tighten falsification condition`:** add the falsification condition to the section in the document. No retraction needed.
4. **If verdict is `Preserve`:** no action required. Record completion date in the audit row.

---

## Sequencing recommendation

Audit in dependency order within each part. Part I before Part II before Part III.

Suggested order for a first full pass:

1. §2 (formal encoding — anchor for all Part I checks)
2. §3 → §4 → §5 (state space → valid states → transition graph)
3. §6 → §6.1 → §6.2 (constraint graph → bottleneck → solution paths)
4. §7 → §8 → §8.1 → §8.2 (ablation → node identity)
5. §9 → §10 → §11 (P1, P3, P4 contact — audit together since falsification conditions should be mutually consistent)
6. §12 → §12.1 → §12.2 → §12.3 → §12.4 → §12.5 (cultural universality — last in Part III)
7. §13 → §14 → §15 → §15.1 → §15.2 → §15.3 (scope — after all candidate claims audited)

§1 (motivation) is Part I prose. No enumeration check applies. Audit for MDL only: does it correctly frame the three questions the experiment answers?
