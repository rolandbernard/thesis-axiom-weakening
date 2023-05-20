# RBox Refinement

Let us now consider the weakening of RBox axioms, starting with the weakening of role hierarchies. Weakening role hierarchies in $\mathcal{SROIQ}$ becomes complicated due to global restrictions that are placed on the ontology. Adding an axiom to a valid $\mathcal{SROIQ}$ ontology, even if the axiom on its one may be valid, does not guarantee that the resulting ontology is still valid. Both the restrictions in the usage of simple roles and the regularity constraint on the RBox need to be considered if we want to ensure that a resulting ontology adheres to the restrictions in $\mathcal{SROIQ}$.

Example: Take as an example the ontology $\mathcal{O} = \{a \circ b \circ a \sqsubseteq c\}$ that defines the simple roles $a$ and $b$, and a non-simple role $c$. Adding the axiom $c \sqsubseteq b$, even if it is correct in isolation, will result in an ontology that is not regular.

Example: As another example, take the ontology $\mathcal{O} = \{a \circ a \sqsubseteq a, \top \sqsubseteq \exists c . \mathrm{Self} \}$ that defines the transitive role $a$ and simple role $c$ used in a self-assertion. Adding the axiom $a \sqsubseteq c$, even if it may be correct in isolation, will result in a violation of the restrictions because $c$ will become non-simple and non-simple roles may not be used in self-assertions.

## Weakening Role Hierarchies

### Role Hierarchies in $\mathcal{ALCH}$

To avoid these complications, we will first consider the simple case of weakening role hierarchies in $\mathcal{ALCH}$. $\mathcal{ALCH}$ supports only simple RIAs, and does not have any of the restrictions that are present in $\mathcal{SROIQ}$.

Also, we can note that any ALCH ontology is also a SROIQ ontology if we allow cycles in the RIA concerning simple roles.

Explain obvious weakening

Show that they are indeed weaker

### Role Hierarchies in $\mathcal{SROIQ}$

The weakening presented above is not applicable, without additional restrictions, to sroiq. may cause non-regular rbox. may cause non-simple roles

example of both non-simple and non-regular

Ideally, our rules for sroiq should yield the results as the previous approach if presented with a alch ontology

the role up and down covers are restricted to simple roles

sprcializing the left hand sideto simple roles is not problematic

generalization of the right hand side maybe problematic

generalizing the rhs of a complex ria to a simple role makes it non-simple. 

similarly the rhs of simple ria where the lhs is non-simple is problematic

let us consider also the possibility of weakening using non-simple roles 

generalizing to non-simple roles may without additional restrictions cause non-regularity

the lhs of a simple ria may, if the rhs is simple, not be specialized to a non-simple role as it would make the rhs non-simple.

definition

example 

### An alternative approach

an alternative approach to ensure regularly could be achieved by fixing a regular pre order and use it for selection of roles

This follows closely the definition of regularity

definition

example

this approach may further generalized by allowing all weakening and checking the global restrictions after replacement in the ontology

This approach is not further explored in this thesis.

## Weakening Disjointed Role Axioms

in contrast to weakening role hierarchies, weakening disjointedness assertions is straightforward

the only restriction that must be kept in mind is that the roles in role disjointedness assertions must be simple

this is ensured by our choice for the cover functions, that do no contain non-simple roles

definition

example
