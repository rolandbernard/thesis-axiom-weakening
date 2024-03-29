# Ontology Bugs

As software systems evolve, it becomes harder to avoid the introduction of bugs. Similarly, in ontology engineering, bugs can be introduced into an ontology. With increased size and complexity of a system, it becomes harder to debug these defects, both for software systems and ontologies.

## Categories of Bugs

Defects, in both software systems and ontologies, can be due to a number of different reasons. In [Debugging unsatisfiable classes in OWL ontologies](../../Reading%20List/Debugging%20unsatisfiable%20classes%20in%20OWL%20ontologies.md) the authors identify three broad categories of defects that can be present in an ontology: *syntactic defects*, *semantic defects,* and *modelling defects*.

### Syntactic Defects

Syntactic defects in an ontology can be caused by a statement that does not conform to the grammar of the employed logic. Similarly, for software systems, these defects may be the result of programs that are not consistent with the grammar of the chosen programming language. These sorts of syntactic defects are easy to locate and correct. In general, tool support for these kinds of defects is able to pinpoint the location of the defect and give an explanation to the user.

Example:

There may however be some additional restrictions on what constitutes a valid ontology or program that is not based solely on the grammatical rules. For ontologies, these might be for example the restrictions placed upon the form of the graph for a specific OWL profile. For programming languages, a similar restriction to this may be the requirement for definition before use or the presence of a type system. These restrictions reduce the space of valid programs. Restrictions of this kind can often be much easier to violate and harder to debug than the first kind of syntactic defects that is a violation of the grammar.

Example:

### Semantic Defects

For ontologies, semantic defects, as defined in [Debugging unsatisfiable classes in OWL ontologies](../../Reading%20List/Debugging%20unsatisfiable%20classes%20in%20OWL%20ontologies.md)  are those which can be discovered by a reasoner given an ontology free of syntactic defects. This includes for example the inconsistency of the ontology, or the unsatisfiability of a concept. The presence of such defects is generally not hard to identify, given the availability of a reasoner for the logic of the ontology. It is, however, often not trivial to understand the underlying source of the defect.

Example:

A close analogy to these kinds of defects from the perspective of a software system is the raising of an error during the execution. An error is an indication of a defect in the software, and depending on tooling support they may be more or less difficult to understand and rectify.

### Modelling Defects

Modelling defects are those defects that are not syntactically or semantically invalid. The presence of unintended inferences in an ontology is one such defect. These defects can also be of more stylistic nature. Redundancy or unused parts of the ontology may be considered as defects, since they do not add any knowledge to the ontology.

For software systems, modelling defects are bugs that do not cause any errors, but which produce undesired behaviour. An example for such a defect could be that the result of a calculation is wrong, or that the software includes security vulnerabilities. For software systems, there might be other non-functional requirements, that if not met constitute defects in the software. These may for example be unsatisfactory performance or unmaintainable code organization.

These kinds of defects can in general not be detected automatically by tools. They require careful attention and domain specific knowledge to be revealed and corrected. In some scenarios, testing may be used to uncover and prevent against some modelling defects, by expressing more explicitly the modellers/programmers intend. This can be done both for software systems and for ontologies.

## Causes of Bugs

Mistakes by the ontology modeller

These mistakes can be typos, especially in the case of syntactic errors

or, especially for semantic errors and modelling errors, they might result from an oversight by the ontology developer.

Combining different ontologies from separate sources

Different ontologies might model the same domain in different ways

This can easily lead to modelling defects.

However, it could also result in semantic defects, such as unsatisfiable concepts or an inconsistent ontology

Example (of how the combination of two ontologies can make a concept unsatisfiable)

Additionally, the combination of ontologies can lead to violations of the global constraints of for example OWL 2 DL.

Combining two OWL 2 DL ontologies might therefore yield an ontology that is no longer valid in OWL 2 DL. This then represents a syntactic defect.

Example (ontology 1 using transitive isPartOf, ontology 2 using isPartOf in cardinality consraint)
