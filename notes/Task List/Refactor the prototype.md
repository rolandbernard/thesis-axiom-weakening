# Refactor the prototype

Date Created: April 4, 2023 11:57 AM
Status: Done
Tags: thesis, uni

- [x]  Migrate to a modern Java version (take what we used for computer networks)
- [x]  Everything should use the public API, and not the *Impl classes
- [x]  Migrate to JUnit 5
- [x]  Rewrite everything (not everything, but a lot of stuff)
- [x]  Most time is spent creating ontologies and reasoners
- [x]  Implement LRU cache
- [x]  Combine axiom weakening and strengthening to avoid duplication
- [x]  Add tests for axiom weakening
- [x]  Give options for bad axiom strategy
    - [x]  Random axiom
    - [x]  Random axiom not in unspecified maximal consistent subset
    - [x]  Random axiom not in the largest maximal consistent subset
    - [x]  Random axiom in least maximal consistent subsets
- [x]  Give options for reference ontology
    - [x]  Random maximal consistent subset
    - [x]  Unspecified maximal consistent subset
    - [x]  Largest maximal consistent subset
    - [x]  Intersection of maximal consistent subsets
- [x]  Clean up the remaining classes
