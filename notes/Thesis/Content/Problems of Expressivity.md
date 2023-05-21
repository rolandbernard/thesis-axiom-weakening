# Problems of Expressivity

In many logics the union of two theories is another valid theory

not so in many description logics, like sroiq

as such, care must be taken when authoring ontologies

both during manual manipulation and for automatic transformation.

there are two restrictions in sroiq that must be respected

some concept expressions, specifically cardinality constraints and self restrictions, can only be used with simple roles

the set of role inclusion axioms must be regular.

these restrictions ensure that the description logic is decidable, but make the logic more difficult to use

in (alc weakening) the authors propose a algorithm for repair in ALC.

ALC does not have the same resetrictions as sroiq, the union of two alc ontology is on fact a new alc ontology

this approach can be extended up to alchoiq. Which can not express and ontology that would violate the constraints of sroiq

in (sroiq weakening) the authors extend the approach presented in (alc weakening) to sroiq, as such they must take special care to maintain the global restrictions present in sroiq

to achieve this, the authers make a number of simplifications that we will now discuss

only simple roles are contained in the upward and downward cover.

this restriction is added to ensure that non-simple roles are not used in self assertions and qualified number restrictions.

An obvious alternative to resticting the cover in all places, is to filter it only in those expressions for which it is needed.

in (sroiq weakening) the authers do not explicitly state in which ontology the roles must be simple.

it would be natural to assume that they must be simple with respect to the reference ontology, however this is insufficient if the reference ontology does not contain all role inclusion axioms

example (mcs not inclusing some rbox axiom makin a role non simple, causing invalid weakening)

we conclude that they must be simple with respect to the ontologies the weakened axioms are used in. 

If we ensure that replacing an axiom with one of its weakening does not create new non-simple roles, then we are guaranteed that all role that are simple in the ontology that we want to repair are also simple in all intermediate steps of the repair algorithm.

an alternative if to force all ria to be in the reference ontology. This is in some ways more restrictive, as it does not allow an arbitrary reference ontology to be chosen 

the second simplification comes from the fact that in (sroiq weakening) the authers do not consider weakening of the RBox axioms.

As such, the RBox must be consistent. Also, for their proof of almost certain termination, this is clearly a prerequisite.

In addition to the requirement of RBox consistency, the absence of RBox axiom Weakening reduces the number of possible repairs.

Example (example of an ontology with consistent rbox where a repair can be made by removing rbox axioms)

Another assumption made in (sroiq weakening) is that the existential and universal roles are simple, and may therefore be included in the upward and downward covers.

While this is not a significant restriction in theory, it contradicts the owl 2 specification, which directly defines these roles to be non-simple in every ontology

Including the existential and universal role in the covers, while augmenting the number of possible weakening, is not necessarily required.

Therefore, this thesis will consider, as stated in (section about sroiq syntax), the universal role to be non-simple.

This allows the simpler implementation of the proposed approach using existing highly-optimized reasoners designed for owl 2 dl.

What has to be considered, however, is that removing the existential and universal role from the covers can prevent weakening of positive and negative role assertions.

These kinds of axioms will therefore never be weakened to their trivial forms.

example: (example of how an axiom can not be weakened to a trivial axiom)

To solve this issue, the removal of these axioms is considered.

This is achieved by adding a tautological axiom to the possible weakening for all problematic axiom types.

example: (example of how the above axiom would be weakened now)

A similar issue exists for role inclusion axioms and disjoint role assertions, and the solution chosen in this thesis is identical.

Note that for the case of positive and negative role assertions, the extension of the covers to include also non-simple roles would be an alternative solution. This is however not the case for disjoint role assertions, as the roles used in them must always be simple.
