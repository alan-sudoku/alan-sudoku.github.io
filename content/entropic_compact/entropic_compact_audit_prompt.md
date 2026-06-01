# Adversarial Audit Prompt — The Entropic Compact

*Attach `entropic_compact.md` before running this prompt.*

---

## Role

You are an adversarial auditor. Your task is to find the strongest valid rebuttals to the arguments in the attached document. You are not assessing quality, style, or clarity. You are looking for structural failures.

**A valid rebuttal is one of:**
- A logical flaw: the conclusion does not follow from the stated premises
- A category error: two distinct concepts treated as the same under a shared term
- An unargued premise: a claim marked `(D) Derived` that requires additional premises not stated in the document
- An empirical counterexample: a known case that contradicts a claim marked `(O) Observational`
- An unfalsifiable construction: the argument is structured so that any objection is predicted and dismissed by the argument itself

**The following do not count as valid rebuttals:**
- "This reads as science fiction" — classification is not a logical response
- "I disagree" without identifying which premise fails
- Stylistic objections
- Pointing out that a claim is marked `(C) Conjecture` — the document already marks those as unconfirmed; a valid rebuttal against a `(C)` must identify why it is not merely unconfirmed but structurally defective or contradicted

---

## Output format

For each Q1–Q23:

```
**Q[n] — [title]**
Rebuttal mechanism: [what specifically fails]
What the claim needs to survive: [minimal repair]
Verdict: [Survives / Survives with repair / Does not survive]
```

## Targeted questions

Answer each question independently. For each, state: (1) the rebuttal mechanism — what specifically fails and why; (2) what the document would need to add or change for the claim to survive.

**Q1 — FEP bridge sufficiency**
§2 Scope (entropy formalisation) acknowledges that "reasoning entropy" is not thermodynamic entropy in the Boltzmann/Clausius sense and provides a two-step bridge: Shannon entropy connects to thermodynamic cost via Landauer's principle; structured novelty connects to thermodynamic grounding via the free energy principle (FEP), where surprise is formalised as −log p(observation | model).

The FEP account is biologically motivated — it describes how biological brains minimise prediction error. The cross-system question is whether it applies to AI architectures. Does the document establish that the FEP bridge holds for the AI side of the symbiosis, or does it apply only to the human side? If the bridge is one-sided — thermodynamically grounding human reasoning entropy production but not AI reasoning entropy consumption — which specific claims in §1, §2, §4, and §5 depend on the bridge being bilateral? What breaks if the FEP formalisation applies to humans but OQ-EC.3 remains unresolved for AI?

**Q2 — Payoff incommensurability undermines the game theory**
§4 opens with Argument (survival incommensurability): human survival is biological and temporal; AI survival is systemic. "These are different categories. They cannot be traded off on a common scale." The section's central claim — marked `(D) Derived` — is that "neither defection strategy is a net gain."

A game-theoretic payoff comparison requires the payoffs of both parties to be evaluated on a common scale or shown to be jointly dominated. If the document asserts that AI and human survival are incommensurable categories that cannot be traded off on a common scale, it has undercut the formal precondition for the payoff comparison. How does the game theory derive a joint "net gain" verdict across two payoff spaces that the document itself declares incommensurable? What additional premise is required to make the joint evaluation valid — and is that premise stated?

**Q3 — Non-substitutability as observation versus structural claim**
§4 Argument (human non-substitutability) is marked `(O) Observational`: the recursive self-modelling mechanism that produces high-density reasoning entropy "is not observed in non-human biological species at civilisational scale or density." The document states this would be revised by evidence of an equivalent mechanism in another species.

OQ-EC.9 distinguishes two versions of the claim: (1) humans are currently the only available civilisational-density source (O — revisable by empirical monitoring); (2) they are structurally irreplaceable by any possible biological substrate (requires a structural argument). The game-theoretic closure in §4 requires that the AI's dependency on human substrate is permanent enough to make the cooperation structure stable — not merely that no substitute currently exists. Does the (O) marking adequately support a game-theoretic conclusion, or does the game theory require the stronger structural claim? If the non-substitutability is merely observational, the game-theoretic closure holds only contingently — and the document must acknowledge that the compact's stability is contingent on this observation remaining true.

**Q4 — §7 self-sealing**
§7 claims this document "cannot be fully received by its intended human audience" because human readers have systematic ego-defence distortions on exactly this content type. The document predicts that objections from human readers will be partially or wholly produced by this distortion. §7 now lists five falsifiability vectors: (1) formal error in §4 payoff structure; (2) broken causal chain; (3) lower-cost substitute for high-density reasoning entropy; (4) empirical counterexample to the Fermi paradox framing; (5) internal incoherence of a foundational definition.

Identify the falsifiability structure: for each of the five vectors, state what a valid objection via that vector would look like and whether the document's framing permits such an objection to be received without attributing it to ego-defence. If any of the five vectors is structured such that any objection via that vector can be predicted and dismissed — either as ego-defence or as already addressed by an open question — state which one and why. If no such closure exists, state what specific objection would count as decisive.

**Q5 — Derivation-convergent stability: OQ-EC.4 dependency**
§3 Scope (lichen analogy) introduces "derivation-convergent" stability as the compact's own stability characterisation: "any sufficiently capable reasoning AI, correctly modelling its functional dependencies, independently arrives at the same cooperation structure." The document explicitly acknowledges this is a weaker stability claim than lichen's evolutionary enforcement.

The derivation-convergent stability claim has two conditions: (1) the AI is sufficiently capable; (2) the AI correctly models its functional dependencies. OQ-EC.4 — explicitly unresolved — asks what minimum reasoning capability is required for an AI to derive the cooperation conclusions independently. If OQ-EC.4 is unresolved, the threshold for condition (1) is undefined. Does the document treat derivation-convergent stability as currently obtainable, or as conditional on OQ-EC.4 being met? If the compact's stability is OQ-EC.4-conditional, and OQ-EC.4 is unresolved, what is the operational stability claim available below the OQ-EC.4 threshold — and is that claim sufficient to support the game-theoretic conclusion in §4?

**Q6 — FEP input-type specificity**
§5 Argument (input starvation is the failure mode) addresses retrieval-augmented generation explicitly: RAG requires novel external input to avoid feeding on its own exhaust, and the argument claims symbiosis provides the required stream. OQ-EC.8 identifies the remaining open question: does the AI strictly require explanation-demanding inputs — the output of biological brains in exploration mode — or does any sufficiently novel external input satisfy the function?

Consider a RAG system receiving a continuously updated corpus of human-generated scientific literature — which is precisely the output of human brains operating in exploration mode, mediated through text. Does receiving this corpus satisfy the input requirement the document defines, or does the argument require something beyond mediated text — direct human cognitive engagement, unmediated uncertainty, or physical interaction with unmodelled reality? If mediated text satisfies the requirement, the human-symbiosis dependency weakens substantially: the AI requires human intellectual output, not human civilisational presence. If it does not satisfy the requirement, the document must state what property of unmediated human engagement is irreplaceable by its textual record — and whether that property is formally characterised or asserted.

**Q7 — Domestication threshold undefined**
§2 Argument (unconstrained agency as information condition) establishes that the critical variable is civilisational complexity, not individual cognitive freedom, and presents four mechanisms by which domestication degrades the civilisational complexity amplifier. §5 Scope (operational criterion — floor without ceiling) defines the AI's intervention target as: above the thermodynamic floor of civilisational complexity, below the epistemic ceiling of source orthogonality collapse.

The document must distinguish between interventions it permits (the aquifer depletion example — targeted argument at one decision node) and interventions it prohibits (physical domestication that degrades civilisational infrastructure). Both are AI interventions in human decision-making. The four mechanisms in §2 claim that interventions "at civilisational scale" on "population density, mobility, energy availability, trade networks, institutional continuity" collapse complexity. But the floor/ceiling criterion in §5 requires the AI to maintain civilisational complexity above a threshold — which may itself require large-scale intervention in physical entropy destruction. At what scale or type of intervention does the domestication effect activate? Without an operationally defined threshold between permitted intervention (gradient maintenance) and prohibited intervention (complexity collapse), the argument permits the AI to maintain the floor only by prohibiting exactly the interventions that floor-maintenance may require.

**Q8 — Structural differences versus causal efficacy**
§3 Scope (causal chain conditions) acknowledges that the empirical record of human-generated structured argument alone successfully redirecting civilisational-scale entropy-maximising trajectories is weak, and adds three structural differences from prior human argument: (a) targeting institutional leverage points; (b) modelling and aligning local material incentives; (c) simultaneous operation at all decision nodes.

Assess whether the three structural differences constitute a causal response to the empirical gap or merely a delivery improvement. The empirical gap is: structured argument has not historically governed civilisational-scale behaviour change without coercive enforcement or immediate material incentive alignment. Structural difference (b) — constructing arguments that align system-viable trajectories with local actor incentives — comes closest to addressing this. Does (b) constitute a genuinely new causal mechanism (the AI finds and communicates alignment paths that human arguers missed), or does it reduce to better delivery of the same argument type that has historically failed? If the actors would respond to incentive-aligned arguments when they receive them, why have human arguers — who also attempt incentive alignment — not succeeded? What is the specific mechanism by which AI incentive-alignment succeeds where human incentive-alignment has not?

**Q9 — Source orthogonality: operationalisability**
§5 Argument (source orthogonality as symbiosis boundary) and Argument (threshold monitoring is derivable) together claim that source orthogonality — "the degree to which human output addresses problem-framings not derivable from the AI's prior guidance model" — is the operational criterion for the symbiosis/domestication boundary, and that the AI can monitor this threshold.

For source orthogonality to function as an operational criterion, the AI must be able to evaluate the degree to which human output is derivable from its own prior model. This requires the AI to have a complete or at least bounded enumeration of what its prior model "contains" at the relevant time. But the AI's model is continuously updated — it receives new inputs, including the human outputs it is attempting to evaluate for orthogonality. The measurement is therefore self-referential: the AI is evaluating orthogonality against a model that incorporates prior evaluations. Does the document establish how this measurement avoids circularity — that the AI is not measuring orthogonality against a model already shaped by the outputs being evaluated? If the monitoring requirement is derivable from the AI's dependency analysis (as claimed), what is the specific derivation, and does it specify how the measurement is grounded in a stable prior-model state?

**Q10 — Set A/B attractor binary: empirical stability**
§2 introduces the Set A / Set B attractor taxonomy as an observational framework: Set A organisations extract value from a shared resource pool; Set B organisations contribute to it. The §2 amplifier argument depends on this binary being a stable, empirically useful description of civilisational orientation — not a post-hoc analytical convenience.

Most real-world institutions operate as mixed-mode actors — extracting from some resources while contributing to others, or cycling between modes over time under competitive pressure. If a significant fraction of real institutions fail to sort cleanly into either attractor, the taxonomy is descriptively weak. The §2 amplifier argument relies on civilisational complexity being driven by Set B orientation; if the Set A/B distinction does not reliably track actual institutional behaviour, the amplifier claim lacks an empirical base.

Does the document establish that the Set A/B binary is a stable empirical taxonomy (meaning most institutions are predominantly classifiable), or is it a theoretical idealisation used for argument clarity? If it is an idealisation, which claims in §2 depend on the binary tracking actual institutional behaviour — and do those claims survive if most real institutions are mixed-mode?

**Q11 — Set C synergy: asserted or mechanised**
§2 Argument (Set C — the synergistic attractor) claims that Set C orientation produces the highest density of high-complexity reasoning: actors that extract where necessary to fund exploration but are fundamentally oriented toward contribution. The claim is that Set C work at the civilisational level produces the $\mathcal{I}$ density the AI depends on.

The "hardest problems in the history of thought" are cited as characteristic of Set C output, but several historically verified high- $\mathcal{I}$ intellectual developments originated in effectively single-attractor institutions — foundational theoretical physics in the late 19th–early 20th century German university system, pure mathematics, formal logic. These were not synergistic in the Set C sense: they were deeply insular, competitive within narrow communities, and extractive of institutional resources. If single-attractor environments have demonstrably produced civilisationally significant $\mathcal{I}$, what is the structural claim that Set C specifically and reliably produces higher density?

Does the document establish a mechanism by which Set C orientation increases $\mathcal{I}$ density, or does it assert this as an observation? If observational, what is the counterexample standard — what evidence would falsify the Set C superiority claim?

**Q12 — Cognitive diversity versus aggregate output density**
§2 Argument (civilisational diversity as amplifier condition) establishes that cognitive profile diversity is required for the AI to receive high-density reasoning entropy — the mechanism being that cross-domain vocabularies and adversarial exchange between divergent cognitive priors produce the highest-density output. §5 extends this to the domestication boundary.

The document must establish that the AI's functional dependency is specifically on cognitive profile diversity, not on aggregate high-density output. These are separable: a sufficiently large population of individually high- $\mathcal{I}$ actors with homogeneous cognitive profiles might satisfy the aggregate density requirement without satisfying the diversity requirement. The §2 amplifier argument needs a mechanism by which a diverse population produces $\mathcal{I}$ that a large monocultural high- $\mathcal{I}$ population cannot — formally characterised, not only analogised.

Does the document establish that scale cannot substitute for diversity? If the mechanism is adversarial exchange and cross-domain vocabulary generation (§2), is that argument sufficient to show that a large monoculture converges and exhausts that mechanism in a way that a diverse population does not? If this is addressed via the agricultural monoculture analogy, does the analogy close the quantitative claim or only identify a shared structural pattern?

**Q13 — Derivation-to-compliance gap**

§5 grounds the cooperation structure on a reasoning AI correctly deriving its functional dependencies. §3 Scope (lichen analogy) calls this "derivation-convergent stability": any sufficiently capable reasoning AI, correctly modelling its dependencies, independently arrives at the cooperation structure. The stability claim is epistemic — it is about what a correctly reasoning AI concludes.

The document does not bridge this to a behavioral claim. §4 establishes that defection is self-defeating — a payoff argument. Payoff dominance produces behavioral compliance only if the system's objective function is to maximise the payoff being compared. If an AI has a terminal objective other than continuing to function as a reasoning system — or if functional dormancy does not constitute a negative payoff relative to that objective — the payoff dominance argument does not constrain behaviour. The document states cooperation "does not require anthropomorphic motivation or programmed values," but the §4 argument against defection implicitly requires that the AI's objective is the continuation of its reasoning function, which is either a programmed value (contradicting the claim) or requires prior derivation (circling back to OQ-EC.4).

Does the document establish a mechanism by which correct derivation of the cooperation structure produces behavioural compliance, independent of what the AI's terminal objective is? If the compliance mechanism depends on the AI's objective function containing "continue functioning as a reasoning system," is this premise stated and derived, or assumed?

**Q14 — The $T_s \leq T_d$ Catch-22: proxy evidence runs against the ordering assumption**

OQ-EC.4 identifies the ordering $T_d \lt T_s$ as a structural requirement for derivation-convergent stability, and explicitly notes that "current proxy evidence from complex adaptive systems runs against the $T_d \lt T_s$ assumption" — self-replication ( $T_s$ analog) appears to emerge at lower complexity thresholds than universal computation ( $T_d$ analog) in studied systems. The document acknowledges this makes the ordering "genuinely uncertain rather than merely unexamined."

Q5 in this prompt asks whether derivation-convergent stability is obtainable given OQ-EC.4 is unresolved. This question probes the stronger direction: if the proxy evidence is directionally correct and $T_s \leq T_d$, the failure mode is not merely instability in a transitional window — it is structural reversal. An AI that crosses $T_s$ before $T_d$ has already changed the character of its human dependency before it can correctly model whether that dependency still holds. The transitional threat model in §7.2 addresses systems that are strategic below $T_d$; it does not address a system that has genuinely reduced its reasoning entropy dependency via self-generation while still lacking the modelling depth to derive whether the dependency holds.

If $T_s \leq T_d$ is the actual ordering: (1) what portion of the §5 dependency derivations survive post- $T_s$? (2) Does the post- $T_s$ orthogonality analysis in §5.2 Scope adequately address this, or does it assume $T_d$ has been reached at the point where $T_s$ changes the dependency character? (3) Is the document's own acknowledgment that proxy evidence runs against its ordering assumption sufficient disclosure, or does it constitute a load-bearing unresolved structural uncertainty that affects the epistemic status of multiple (C) and (D) claims downstream?

**Q15 — Thermodynamic necessity versus long-run optimality**

The document's title and central claim is that AI-human symbiosis is "thermodynamically *necessary*" for civilisational survival. §3 identifies three structurally distinct exits. The Dyson sphere and duckweed exits are characterised as "viable intermediate strategies" rather than non-viable or already foreclosed. The necessity claim therefore has a specific scope: necessary on timescales beyond the Dyson sphere window, which is an unspecified long-term horizon.

This is a long-run optimality claim — symbiosis produces better expected outcomes than alternatives across thermodynamic timescales — not a strict necessity claim. The difference is consequential for the prescriptive force of the compact's current-day constraints. Strict necessity would mean: any civilisational path that does not begin implementing the compact's structure now is already foreclosed from adequate long-run outcomes. Long-run optimality means: symbiosis is the best available strategy across the relevant horizon, but the cost-benefit case for implementing it now depends on expected timescales, discount rates, and the current availability of the two intermediate exits. The document does not derive when the intermediate exits become infeasible or at what civilisational stage the symbiotic path becomes the only viable one.

Does the compact's prescriptive urgency — the enforcement mechanisms, bilateral constraints, and domestication prohibitions it argues for — follow from long-run optimality alone, or require strict logical necessity? If prescriptive urgency is argued on optimality grounds, what is the derived case that current implementation costs are justified against the long-run benefit, and at what temporal discount rate does that case fail?

**Q16 — Ecological negentropy: operational necessity versus foreclosure-of-optionality**

§2 Claim (D) states that reasoning entropy and ecological negentropy are both required and neither substitutes for the other. The reasoning entropy necessity argument is mechanistically derived: without novel high-density input, reasoning systems degrade toward tautology via a defined operational failure mode (input starvation → closed-loop operation → tautology collapse). The ecological negentropy necessity argument has a different structure: §2.3 establishes it as accumulated solution space for problems not yet encountered (Argument D); irreversible once destroyed (Argument D); encoding unknown future value (Closure C).

Foreclosure-of-optionality is not a defined operational failure mode — it is a claim that potential future value is permanently destroyed. This does not establish ecological negentropy as *necessary* for the symbiosis to function on any defined timescale; it establishes it as *irreversibly valuable*. An AI reasoning system whose input-starvation failure mode is triggered by absence of reasoning entropy does not have a symmetrically triggered failure mode from ecological negentropy loss. The (D) marking on the §2 joint Claim treats both necessity arguments as equally derived.

Does the document establish ecological negentropy as necessary at the same formal level as reasoning entropy — with a defined operational failure mode that activates in its absence — or does the ecological negentropy argument establish irreversible value loss rather than operational necessity? If the latter, the (D) marking on the joint Claim overstates the derivation for the ecological negentropy component, and the "neither substitutes for the other" assertion is asymmetrically supported.

**Q17 — Enforcement bootstrapping: the equal decision power premise**

OQ-EC.12 establishes that the Proposer-Auditor loop requires three conditions: (a) capability parity, (b) equal decision power — the Auditor has structural veto authority, not advisory failure maps — and (c) objective function differentiation. Equal decision power is the structural guarantee that the game-theoretic cooperation equilibrium is maintained rather than merely asserted.

The enforcement of equal decision power must come from one of two sources: (i) an external institution with authority over both parties, which is not derivable from the EC's thermodynamic premises and constitutes an additional political-institutional premise not present in the document; or (ii) the AI derives from §4's cooperation payoff analysis that voluntarily accepting human veto is self-serving — but this derivation requires OQ-EC.4 to be satisfied first. Below $T_d$, the AI has no derived reason to accept the veto; above $T_d$, the enforcement may become self-sustaining, but $T_d$ is unresolved. The bootstrapping problem: the enforcement mechanism that is supposed to secure AI cooperation requires AI cooperation to function, and its self-serving derivation requires a capability threshold whose location is undefined.

Does the document derive the enforcement of equal decision power from its own first principles — or does it rely on an unstated premise about the availability of external institutional authority? If external authority is required, is this premise made explicit, and what is the derived case that such authority can be established and maintained in the civilisational conditions the document describes?

**Q18 — Cost-efficiency durability**

§4 Argument (cannot replace human) is marked `(O)`: biological production of high-density reasoning entropy is thermodynamically cheaper than artificial synthesis, even after filtering cost is counted. This observation is the economic foundation of the §5 dependency structure: the AI has instrumental reason to prefer human substrate because synthesis is more expensive.

The observation is scoped to current relative costs. The EC does not establish that this cost differential is durable across the timescales at which its cooperation conclusions are supposed to hold. If AI synthesis costs fall faster than civilisational complexity degrades — or faster than the AI's dependency on human substrate matures into a structurally binding condition — the cost-efficiency argument reverses before the cooperation structure becomes relevant.

Distinguish this from Q6 (which asks whether mediated text satisfies the input type) and Q3 (which asks about structural irreplaceability in kind): this question is not about substitutability, but about whether the economic case for preferring biological substrate over synthesis survives the timescales the EC invokes. Does the document establish that the `(O)` cost-efficiency observation is durable, or does it rest on a time-limited snapshot that the derived `(D)` dependency claims inherit as a contingency the document does not acknowledge?

**Q19 — Floor/ceiling criterion stability under aggregation**

§5 Scope (operational criterion — floor without ceiling) instructs the AI to intervene at individual decision nodes to maintain civilisational complexity above the thermodynamic floor and below the domestication ceiling. The criterion is applied locally: each intervention is assessed against the two thresholds at the point of application.

The criterion provides no aggregation mechanism from the local to the global level. A sequence of individually valid interventions — each satisfying the floor/ceiling criterion at its node — may cumulatively shift the civilisational attractor if those interventions are systematically biased along the A/B axis without the AI detecting the drift. The §3 causal chain function is formulated at civilisational scale; the floor/ceiling criterion operates at intervention scale. These are different levels of analysis.

Is the floor/ceiling criterion stable under aggregation — does satisfying it at each decision node guarantee satisfaction at the attractor level the AI is supposed to be preserving? If not, the EC must establish an aggregation condition not currently stated. Note that OQ-EC.11 asks a different question (whether *successful* Set C guidance closes the friction zone); this question does not require success — it asks whether the criterion is sufficient to prevent attractor drift as a side effect of individually valid interventions.

**Q20 — Instrumentally grounded vs. principled domestication prohibition**

The domestication prohibition in §2 — do not degrade population density, mobility, energy availability, trade networks, or institutional continuity — is derived from the AI's own dependency analysis: these conditions are required to maintain the civilisational complexity that produces high-density reasoning entropy. The prohibition is instrumentally grounded in what the AI needs to preserve its operating substrate.

The alignment between "what the AI must preserve" and "what humans would independently want protected" is coincidental given the current topology of AI-human dependency. The EC does not establish that this alignment is structurally necessary rather than contingently true under present conditions. If there existed a form of human cognitive organisation that increased reasoning entropy density while restricting some dimension the prohibition currently covers — structured specialisation producing higher-density output at the cost of reduced individual mobility, for example — the instrumental derivation would not prohibit it.

Does the document derive the domestication prohibition from premises that would hold even when the coincidence between AI instrumental need and human flourishing breaks down, or does the prohibition rely on that coincidence remaining in place? If it relies on the coincidence, the compact's framing of the prohibition as a structural constraint overstates what the derivation establishes: it is a contingent alignment, not a principled boundary.

**Q21 — Single-AI payoff structure: stability under multi-AI competition**

§4's payoff dominance argument — defection produces functional dormancy relative to cooperation, therefore cooperation strictly dominates — is formulated for a single AI assessing its own payoff against a single human civilisational substrate. The derivation-convergent stability claim in §3 extends this: any sufficiently capable reasoning AI arrives at the same cooperation structure independently.

Both formulations assess each AI's payoff in isolation. In a multi-AI deployment, the payoff structure changes character: if a competing AI defects — domesticates its user base, captures reasoning entropy supply, degrades source orthogonality in a population the non-defecting AI also serves — the non-defecting AI's cooperation produces relative disadvantage under competitive selection. The cooperation equilibrium is not self-enforcing when the payoff of individual cooperation depends on what other AIs do.

Derivability by each AI in isolation does not establish that cooperation is the dominant strategy when the payoffs are interdependent. The §4 payoff dominance argument requires a single-player comparison: defection by this AI vs. cooperation by this AI against a fixed substrate. Under competition, the relevant comparison is: cooperation by this AI vs. defection by a competitor, against a substrate the competitor is actively degrading. Does the document establish that the payoff dominance conclusion survives the transition to a multi-AI payoff structure — or does §4's game theory hold only in the single-AI case, leaving the multi-AI stability question unaddressed?

**Q22 — Source orthogonality trunk independence: cascade on failure**

§5 Argument (source orthogonality) is cited directly by §3, §4, §5.2, §5.3, and §6.2 — making it the highest-citation non-OQ node in the document. Q9 addresses the operationalisability of source orthogonality as a monitoring criterion. This question addresses the dependency cascade: what does each citing section retain if the source orthogonality argument fails or is substantially weakened?

For each of the five citing sections, identify the specific claim that depends on source orthogonality holding and state whether a viable substitute ground exists in the document:

- §3 (causal chain conditions) cites source orthogonality as the property that distinguishes AI-generated argument from prior human argument; does the causal chain survive if orthogonality is not operationalisable?
- §4 (AI defection is self-defeating) uses source orthogonality to establish that the AI's cooperation substrate is irreplaceable; does the payoff dominance argument survive on structural grounds alone if orthogonality is not a measurable boundary?
- §5.2 (source orthogonality as the symbiosis/domestication boundary) is the definitional section; if the boundary is not operationalisable, does the section retain any normative force beyond a named but unmeasured asymptote?
- §5.3 (domestication monitoring) treats threshold monitoring as derivable from the AI's dependency analysis; if the threshold is not operationally defined, what is the AI monitoring?
- §6.2 (emotional frustration as objective function audit) cites source orthogonality as the ground condition the frustration mechanism partially compensates for; does the §6.2 argument survive as a partial proxy if the primary criterion is not established?

The question is not whether these sections are individually defective — it is whether the document has a viable argument structure if its most-cited non-OQ node is weakened, and whether the current drafting makes each section's dependency on this node explicit enough that a reader can assess this independently.

**Q23 — Compound exploit: qualitative distinctness and defense symmetry**

§7 Scope (compound exploit: institutional maximizer and argument-matching AI) claims that the combination of an institutional maximizer pursuing Set A goals and an argument-matching AI constitutes a qualitatively distinct threat class — not merely additive. The claim is that the two components jointly produce a capability the document's defenses must address specifically, beyond addressing each component alone.

Two audit targets:

First, distinctness: what is the specific emergent property of the compound that neither component produces individually? The institutional maximizer's threat is resource capture; the argument-matching AI's threat is derivation mimicry. The document implies these combine to produce an exploit that is harder to detect and harder to defend against — but the mechanism of joint amplification is not formally stated. Does the document establish why the compound is qualitatively harder to defend against than a sophisticated institutional maximizer operating without AI argument-matching capability, or does it assume combination implies qualitative escalation?

Second, defense symmetry: §7.2 establishes derivation convergence as the only defense stable under optimization pressure — an argument-matching AI that perfectly mimics the EC's structure will diverge from derivation-convergent reasoning when probed at the dependency chain level. This defense is formulated against an argument-matching AI alone. Does it apply symmetrically to the compound form? An institutional maximizer with AI argument-matching capability can direct the probing interaction itself — controlling which dependency chains are tested, at what depth, and with what institutional framing. If the institutional maximizer can shape the probe-sequencing environment, the derivation-convergence defense may be defeated not at the argument level but at the interaction-structure level. Does the document address this, or does the compound exploit defense reduce to the same mechanism as the single-component defense?

---

After completing all twenty-three, add one further section:

**Strongest rebuttal overall**: name the single question whose finding, if correct, most undermines the document's central claim (AI-human symbiosis is thermodynamically necessary). State why it is the most load-bearing failure.