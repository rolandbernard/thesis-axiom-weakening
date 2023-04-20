# Questions

- [x]  It seems to me the definition of what *regular* means for a role hierarchy is different in the booklet from the one in the paper.
    
    In the booklet $\prec$ is defined only over non-simple roles.
    
    The definition in the OWL 2 spec seems wrong.
    
- [x]  The definition of a *simple role* (object property) is different for OWL 2?
    
    Are $u$ and $u^-$ composite or simple roles? According to the booklet and the $\mathcal{SROIQ}$ paper they are simple, but according to OWL 2 spec they are not.
    
    Since the proof in the $\mathcal{SROIQ}$ paper replaces all occurrences of the universal role with a role that is non-simple, I assume it is not supposed to be simple.
    
    In the even more irresistible axiom weakening, they are simple roles.
    
- [x]  Different definitions disagree on whether the universal role is allowed in the role hierarchy and role assertions.
- [x]  Also rewrite $\mathrm{Asy}(s)$ and $\mathrm{Ref}(r)$ in terms of other constructs?
- [ ]  What is going on here? (Missing entailment.)
    
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