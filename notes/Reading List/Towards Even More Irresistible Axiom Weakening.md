# Towards Even More Irresistible Axiom Weakening

Status: Finished
Link: https://ceur-ws.org/Vol-2663/paper-8.pdf
Tags: logic, thesis
Type: Paper

### Summary

- Extends the axiom weakening procedure to the description logic $\mathcal{SROIQ}$.
- Introduces in addition to the TBox $\mathcal{T}$ and ABox $\mathcal{A}$ also the RBox $\mathcal{R}$ for subsumptions between relations.
- A role $R \in N_R$ is simple in $\mathcal{R}$ if it is not implied by any composition of roles.
- Some expressions allow only simple roles, like for example the counting quantifiers.
- Specific changes had to be made to handle role constructs.
- The upward and downward cover for rules allows only simple roles. This is to ensure the closure of $\mathcal{SROIQ}$ under the two refinement operators $\gamma_\mathcal{O}$ and $\rho_\mathcal{O}$.
- $\gamma_\mathcal{O}$ and $\rho_\mathcal{O}$ membership can be computed efficiently, that is, they are N2ExpTime-complete.
- The paper also proposes an algorithm for repairing ontologies using the defined operators.
- The refinement process will almost certainly, that is, with probability $1$, terminate in a finite number of steps.

### Questions

- [ ]  Could we also refine the RBox of the ontology during the repair?
- [x]  Can there even be an inconsistency in the RBox?
    
    Yes
    
- [ ]  Could we have two different covers, one for simple and one for non-simple roles?
- [ ]  Is it possible to simply try the weakening and if it breaks some rules find another one?
- [x]  Can the solvers compute role subsumption?
    
    Yes, but not simplicity.
    
- [ ]  What if we remove equivalent concepts from the refinement results?
    
    Would that ensure that the algorithm converges?
    

[TowardsEvenMoreIrresistibleAxiomWeakening.pdf](Towards%20Even%20More%20Irresistible%20Axiom%20Weakening/paper-8.pdf)
