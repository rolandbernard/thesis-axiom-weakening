# Presentation

1. Title slide
2. Description Logics
    1. Individuals, Concepts, and Roles
    2. Concept expressions
        1. Proportional formulas
        2. Quantifiers
    3. Axioms
        1. Concept inclusions
        2. Concept assertions
3. Expressive Description Logics
    1. Have more concept expressions and axioms
    2. Require additional constraints
        1. simple and non-simple roles
        2. regularly
    3. SROIQ and the Web Ontology Language
4. Knowledge Refinement in Expressive Description Logics
    1. Iteratively modify knowledge to improve or correct it
    2. Concept refinement
        1. Specialization
        2. Generalization
    3. Axiom weakening
5. Motivation
    1. Repairing ontologies
        1. Removing unintended consequences
        2. Inconsistent ontologies
        3. Incoherent ontologies
    2. Combination of conflicting knowledge
        1. Also for concept combination
    3. Machine learning
6. Difficulties and Solutions
    1. simple and non-simple
    2. regularity
    3. restrictions have been added to prevent problems
        1. only refine with simple roles
        2. make sure simple roles remain simple
7. Implementation
    1. Implemented in Java using the OWL API
    2. Using highly-optimized of-the-shelf reasoners
    3. Extensive tests of the functionality
        1. Some manual test cases
        2. Some automatically generated asserting general properties and invariants
8. Plugin for Protégé
    1. Manual axiom weakening and strengthening
    2. Configurable automatic repairs
9. How to Evaluate
    1. Keep as many consequences as possible
        1. Approximate consequences by looking at hierarchy of atomic concepts
    2. For comparing two repairs O1 and O2 use IIC
        1. 1 if O1 has all consequences of O2 and some additional 
        2. 0.5 if both O1 and O2 have the same hierarchy
        3. 0 if O2 has all consequences of O1 and some additional 
        4. Some value in between these based on which repair has a bigger hierarchy
10. Evaluation Results
11. Outcomes
    1. Extended axiom weakening operator
        1. Showed that it maintains global constraints
    2. A Protégé plugin for applying the techniques discussed in the thesis
    3. Evaluation of the proposed approach
12. Future Outlook
13. End slide
