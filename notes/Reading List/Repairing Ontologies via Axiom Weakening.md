# Repairing Ontologies via Axiom Weakening

Status: Finished
Authors: Daniele Porello, Nicolas Troquard, Oliver Kutz, Pietro Galliani, Rafael Peñaloza, Roberto Confalonieri
Published: April 25, 2018
Publication: Proceedings of the AAAI Conference on Artificial Intelligence
Link: https://arxiv.org/pdf/1711.03430.pdf
Tags: logic, thesis
Type: Paper

### Summary

- As ontologies grow, automated methods are needed to repair them, preserving as much knowledge as possible
- Most previous approaches are based on removing axioms
- This paper proposes a method based on weakening axioms instead of removing them
- The paper uses, as an example, ALC based ontologies
- Set of all subconcepts of $\mathcal{T}$ as $\text{sub} (\mathcal{T})$
- The size $\left| C \right|$ of a concept $C$ is defined by the number of syntactic tree nodes
    - The size of a concept or TBox is at least as large as the cardinality of its set of subconcepts
- Upward $\text{UpCov}_\mathcal{T}(C)$ and downward $\text{DownCov}_\mathcal{T} (C)$ cover based on some reference TBox $\mathcal{T}$
    - Set of most specific/general subconcepts from $\mathcal{T}$ subsumed by/that subsume $C$
    - Only meaningful for a consistent reference ontology
- Define an abstract refinement operator $\zeta_{\uparrow,\downarrow}$ and two concrete refinement operators
    - Generalization operator $\gamma_\mathcal{T} = \zeta_{\text{UpConv}_\mathcal{T}, \text{DownConv}_\mathcal{T}}$
    - Specialization operator $\rho_\mathcal{T} = \zeta_{\text{DownConv}_\mathcal{T}, \text{UpConv}_\mathcal{T}}$
    - Define also $\zeta_{\uparrow, \downarrow}^i$ as the i-th refinement iteration
- Complexity of deciding $\gamma_\mathcal{T}$ and $\rho_\mathcal{T}$ membership is not harder than atomic concept subsumption in $\mathcal{ACL}$ or $\mathcal{EL}$
- Otology repair using axiom removal
    1. While $O$ is inconsistent
        1. Select an axiom $a$ from $O$
        2. Remove $a$ from $O$
    2. Return the now consistent ontology $O$
- The refinement operators can be used for repairing inconsistent ontologies $O$
    1. Find a consistent reference ontology $O^\text{ref}$
    2. While $O$ is inconsistent
        1. Select an axiom $a$ from the ontology $O$
        2. Weaken the axiom $a$ by selecting an axiom $a'$ from $g_O(a)$ where $g_O$ is a weakening operator using $\gamma_O$ and $\rho_O$
        3. Replace $a$ with $a'$ in O
    3. Return the now consistent ontology $O$
- To evaluate the quality of a repair, the number of inferred class subsumptions is compared
    - $\text{Inf}(O)$ is the set of class subsumptions that are entailed by $O$
    - $O_1$ is a better repair than $O_2$ if $\textbf{card}( \text{Inf}(O_1) \setminus \text{Inf}(O_2) ) > \textbf{card} ( \text{Inf}(O_2) \setminus \text{Inf}(O_1) )$
    - The weakening method is able to preserve more information than axiom removal

### Questions

- [ ]  Is the choice of generalization and specialization operators arbitrary?
- [ ]  Why is the inferred class hierarchy a good measure for repair quality?
- [ ]  The individual role assertions are not considered during weakening?

[RepairingOntologiesviaAxiomWeakening.pdf](Repairing%20Ontologies%20via%20Axiom%20Weakening/RepairingOntologiesviaAxiomWeakening.pdf)
