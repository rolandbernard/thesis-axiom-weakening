# Debugging unsatisfiable classes in OWL ontologies

Status: Finished
Publication: Journal of Web Semantics
Link: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=9eb667f08333d7eb8efe601661e081b6b1082960
Tags: logic, thesis
Type: Paper

### Summary

- An increasing number of OWL ontologies has become available (on the Semantic Web)
- Large ontologies become hard to debug
    - It is difficult to pinpoint the causes of the errors
    - No explanation for why an error occurs
    - No explanation on how dependencies cause the error to propagate
- The goal of the paper is providing debugging support for unsatisfiable concepts
- Multiple types of defects can occur in a KB
    - Syntactic defects
    - Semantic defects (← focus of the paper is unsatisfiable concepts)
    - Modelling/style defects
- Ontologies can be debugged manually using functionality provided by modelling tools. The paper underlines the need for automated techniques to support debugging and repair.
- Glass box techniques
    - Present user with information about the clash
    - Determine the minimal set of axioms that are responsible for the clash
- Black box techniques
    - Try to detect root vs derived unsatisfiable classes

### Questions

- [x]  Does $SROIQ$ allow for an empty domain?
    
    No.
    

[DebuggingUnsatisfiableClassesinOWLOntologies.pdf](Debugging%20unsatisfiable%20classes%20in%20OWL%20ontologies/DebuggingUnsatisfiableClassesinOWLOntologies.pdf)
