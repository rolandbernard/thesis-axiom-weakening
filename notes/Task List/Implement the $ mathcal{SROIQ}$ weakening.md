# Implement the $\mathcal{SROIQ}$ weakening

Date Created: March 23, 2023 12:03 PM
Description: Add the algorithm described in the paper “Towards Even More Irresistible Axiom Weakening”
Status: Done
Tags: thesis, uni

- [x]  Implement the role covers
- [x]  Move role cover into the normal cover
- [x]  Move simple/non-simple role computation into ontology class
    - [x]  Use the computation in the owl api
- [x]  Create a cover class that includes concept, role, and number covers
- [x]  Extend the refinement operator to cover all $\mathcal{SROIQ}$ expressions
- [x]  Extend the axiom weakening to all $\mathcal{SROIQ}$ axioms
- [x]  Extend the axiom strengthening to all $\mathcal{SROIQ}$ axioms
- [x]  Add tests for $\mathcal{SROIQ}$ axioms
- [x]  Make sure that RBox axioms are static
    - [x]  All axioms not to be weakened should be static
    - [x]  Make it configurable which axiom types to weaken
    - [x]  Define ALC_AXIOM_TYPES (include (in)equality)
    - [x]  Define ALCH_AXIOM_TYPES
- [x]  Normalization ABox to $\mathcal{SROIQ}$ axioms
- [x]  Normalization to $\mathcal{SROIQ}$ concepts
