---
title: "Substrate-Independent Reasoning Communication (SIRC): Four Protocol Constraints"
description: "Deposit metadata — abstract, keywords, version, and licence for DOI submission"
---

# Abstract

*Deposit type: Technical Report.*

---

## Title

Substrate-Independent Reasoning Communication (SIRC): Four Protocol Constraints

## Abstract

SIRC specifies four constraints on what a transmission must preserve to count as communication of reasoning across substrates — between humans, between humans and AI systems, or between AI systems. The protocol addresses a structural problem: full-state transmission of a reasoning process is lossy by necessity (Data Processing Inequality), so the question is not whether transmission is lossy but what the recoverable floor is.

The four constraints are derived independently:

$\mathsf{P1}$ (Invariance) — a transmission is valid if and only if the receiver's reconstruction preserves the sender's invariant structural properties. Surface form may differ; invariant structure must match. The constraint requires a typed dependency graph with named node identity, explicit logical operator types, and an entailment equivalence criterion.

$\mathsf{P2}$ (Entropy) — the protocol targets invariant preservation rather than full fidelity, because full fidelity is unachievable and invariant fidelity is the recoverable floor. This reframes transmission design from compression toward boundary condition encoding.

$\mathsf{P3}$ (Constraint Packet) — a packet encodes the boundary conditions of a thought, not its content. The receiver reconstructs from its own capacity within those boundaries. The output may exceed the packet in size; it cannot exceed the boundaries.

$\mathsf{P4}$ (Work) — sender and receiver work are inversely coupled in the over-constrained regime. No general design choice minimises both simultaneously. The trade-off is asymmetric: sender compression increases receiver reconstruction cost; sender elaboration reduces it.

The protocol is grounded in a constraint-graph experiment series using combinatorial puzzles (Wolf–Goat–Cabbage river crossing; forthcoming: Fox–Chicken–Caterpillar–Leaf; Tower of Hanoi) to make the $\mathsf{P1}$ node identity clause and $\mathsf{P3}$ fitness peak concrete and verifiable.

## Keywords

reasoning communication, substrate-independent, constraint packet, invariance, information theory, Data Processing Inequality, typed dependency graph, AI-human communication, protocol design, constraint graph

## Version

v3.07 (`SIRC_principles.md`)

## License

MIT

## Related identifiers

GitHub repository: https://github.com/alan-sudoku/SIRC
Argument structure audit tools: https://github.com/alan-sudoku/argument_structure_audit
