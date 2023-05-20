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

in (sroiq weakening) the authors exhend the approach presented in (alc weakening) to sroiq, as such they must take special care to maintain the global restrictions present in sroiq

to achieve this, they make a number of simplifications

only simple roles are contained in the upward and downward cover.

in (sroiq weakening) the authers do not explicitly state in which ontology the roles must be simple.

it would be natural to assume that they must be simple with respect to the reference ontology, however this is insufficient if the reference ontology does not contain all role inclusion axioms

example (mcs not inclusing some rbox axiom makin a role non simple, causing invalid weakening)

we conclude that they must be simple with respect to the ontologies the weakened axioms are used in.

an alternative if to force all ria to be in the reference ontology. This is in some ways more restrictive, as it does not allow an arbitrary reference ontology to be chosen 

the second simplification comes from the fact that they do not consider weakening of the RBox axioms.

As such, the RBox must be consistent, also for there proof of almost certain termination, this is clearly a prerequisite 

In addition to the requirement of RBox consistency, the absence of RBox axiom Weakening reduces the number of possible repairs.

examle (example of an ontology with consistent rbox where a repair can be made by removing rbox axioms)

Another assumption made in (sroiq weakening) is that the existential and universal roles are simple.

while this is not a significant restriction in theory, it contradicts the owl 2 specification, which directly defines these roles to be non-simplee in every ontology

therefor, this thesis will consider, as stated in (secotion about sroiq syntax), the universal role to be non-simple, for easier implementation of the proposed approach using existing owl 2 dl reasoners.
