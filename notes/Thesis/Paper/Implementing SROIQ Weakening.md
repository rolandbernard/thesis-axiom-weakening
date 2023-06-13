# Implementing SROIQ Weakening

the proposed weakeing operator may be used for implementing an automated ontology repair algorithms. We implement the same algorithm discussed in (cite alc weakening) and (sroiq weakening). We will give a brief summary of the algorithm.

algorithm: (list the repair by weakening algorithm)

the algorithm, RepairByWeakenong, depocted in (ref to algo), procedes by repretedly selecting bad axioms and replacing them with randomlybselected weakenings until the ontology becomes consistent. while the termination of this algorithm is not guaranteed, it has been shown in (sroiq weakening) that this algorithm almost surely terminates if weaker axioms are chosen uniformly at random from the set of weakenings. There a a number of possible implementations for FindBadAxiom. One possible implementation simply selects random axioms. A more sophisticated approach is to sample some (or all) minimal inconsistent subsets of the ontology and select one of the axioms that occur the most often.

Since the ontology to be repaired is inconsistent, it is not a usefull ontology for use as the reference ontology in the axioms weakening operator. The algorithm therefore needs as input the reference ontology. Just like selecting bad axioms, finding a reference ontology can be implemented in different ways. One option is to select ny maximal consistent subset, while another is to select the instruction of some or all of them.

The axiom weakening operator and repair for ALC have already been implemented for (alc weakening). Based on this, we have now extended the implementation to cover the full range of SROIQ axioms and concepts unsing the approach presented in this paper.

The implementation will spend the most its time during 9repairs calling the reasoners. In order to reduce these calls and accelerate the computation of upward and downward cover sets we implemented some cacheing. This is a obvious place in which to apply caching, since the upward and downward convers are applyed many times during a repair, and uses a static reference ontology. When following directly the definition of cover sets presented on (ref to def of cover), one will compute a large number of subsumptions, many of which will be the same across multiple cover computations.

Rather than apply only a simple cache, however, we found it worthwhile to create a cache for subsumption, in which we also infer extra information from the transitivity of subsumption after each query to the reasoner.  This is in effect similar to the teqnique presented in (cite the papaer) for creating taxonomies, but applied also to complex concepts. Additionally, we used some basic rules to compute subsumption containing conjunctions and disjunctions from results about the conjuncts aor disjuncts. In our implementation, subsumptions are computed only when requested. While it would allow ordering of the reasoner queries to maximise information gain, preconputing the complete relation over the subconcepts, like one may do with a taxonomy, was disadvantageous in our brief testing, since in general not all results are required for a single repair. 

algorithm: list update add knowm algorithm 

algorithm: list update remove possible 

algorithm: cachedtestSubsumbtion

We will now briefly describe the algorithm CachedTestSubsumption. We keep two global variables, one containing sets of know  tuples and one the set of possible tuples. Wenn querying a subsumption, it is first checked whether the result can be determined using the known information, and if not, the reasoner is used to compute the correct results. For every new negative result, RemovePossible is invoked with the parameters of the test.  And for every positive result, AddKnown is called. The algorithm is based on the two implications

C not sub D and C sub E and F sub D implies E not sub F, and

C sub D and D sub E implies C sub E.

There is one further step, used for computing subsumption between concepts. It is applied immediately before possibly calling the reasoner, should none of the rules match. It is given by the following implications.

Ci not sub D implies C1 union … union Cn not sub D

Ci sub D for all i = 1, …., n implies C1 union… union Cn sub D

Ci sub D implies C1 inters … inters Cn sub D

C not sub Di implies C not sub D1 inters … inters Dn

C sub Di for all i = 1, …, n implies C sub D1 inters … inters Dn

C sub Di implies C sub D1 union … union Bn
