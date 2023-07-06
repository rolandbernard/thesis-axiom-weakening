# Figure out what causes missing entailment

Date Created: April 18, 2023 7:17 PM
Status: Rejected
Tags: thesis, uni

```java
OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
OWLDataFactory df = manager.getOWLDataFactory();
OWLOntology ontology = manager.createOntology();
ontology.addAxioms(
    df.getOWLDeclarationAxiom(df.getOWLObjectProperty("sub")),
    df.getOWLDeclarationAxiom(df.getOWLObjectProperty("super")),
    df.getOWLSubClassOfAxiom(df.getOWLThing(), df.getOWLObjectHasSelf(df.getOWLObjectProperty("sub"))),
    df.getOWLSubObjectPropertyOfAxiom(df.getOWLObjectProperty("sub"), df.getOWLObjectProperty("super"))
);
OWLReasoner reasoner = OpenlletReasonerFactory.getInstance().createReasoner(ontology);
System.out.println(reasoner.isEntailed(
    df.getOWLSubClassOfAxiom(df.getOWLThing(), df.getOWLObjectHasSelf(df.getOWLObjectProperty("super")))
));
```
