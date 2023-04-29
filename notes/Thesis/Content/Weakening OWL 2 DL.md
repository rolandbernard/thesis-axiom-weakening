# Weakening OWL 2 DL

Since OWL 2 DL is reducible to $\mathcal{SROIQ}$ it would be sufficient to perform this normalization and then apply the weakening as described to the resulting $\mathcal{SROIQ}$ ontology. However, while this transformation is unproblematic in some contexts in which the result is only to be used for automatic reasoning tasks, if the output must be further manipulated by a user of the system it could lead to the introduction of unnecessary noise. Further, weakening OWL 2 DL ontologies directly can be seen as a heuristic as to which weakening might make sense from a modelling perspective.

Example: OWL has an axiom $\mathrm{DisjointClasses}(C_1, \dots, C_n)$ that allows specifying that a set of classes all are pairwise disjoint. $C_i \sqcap C_j \sqsubseteq \bot$ for all $i \not= j = 1, \dots, n$. One reasonable approach to weakening the OWL axiom is to replace any of the classes $C_i$ with a more specific class $C_i' \in \rho_\mathcal{O}(C_i)$. In contrast, after normalization, there will be $n - 1$ occurrences of $C_i$. It is unlikely, increasingly so with growing $n$, that all such occurrences will be weakened to the same concept. After weakening the normalized ontology, it is thus in general not possible to reconstruct the disjointness axiom.

It should be noted that working directly with OWL 2 axioms will make repairs less granular. For some axiom types, it is not obvious how they could reasonably be weakened to a single axiom.

Example: The OWL axiom $\mathrm{EquivalentClasses}(C_1, \dots, C_n)$ can not easily be weakened. One option for weakening is removing one of the arguments. The axiom would be normalized to a set of $\mathrm{SubClassOf}$ axioms, for which both the subclass and superclasses can be modified. It is evident that this is more gentle than completely removing arguments.

We define the refinement operator $\zeta_{\uparrow,\downarrow}$ for OWL 2 as follows:

- $\zeta_{\uparrow, \downarrow}(A) = \; \uparrow (A)$ for $A \in \mathrm{N}_c \cup \mathbf{R} \cup \{ \top , \bot \}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectComplementOf}(C)) = \; \uparrow (\mathrm{ObjectComplementOf}(C)) \cup \{ \mathrm{ObjectComplementOf}(C')  \mid C' \in \zeta_{\downarrow, \uparrow} (C) \}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectIntersectionOf}(C_1, \dots, C_n)) = \; \uparrow (\mathrm{ObjectIntersectionOf}(C_1, \dots, C_n)) \cup \bigcup_{i=1}^n \{\mathrm{ObjectIntersectionOf}(C_1, \dots, C_i', \dots C_n)  \mid C_i' \in \zeta_{\uparrow, \downarrow} (C_i) \}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectUnionOf}(C_1, \dots, C_n)) = \; \uparrow (\mathrm{ObjectUnionOf}(C_1, \dots, C_n)) \cup \bigcup_{i=1}^n  \{ \mathrm{ObjectUnionOf}(C_1, \dots, C_i', \dots C_n)  \mid C_i' \in \zeta_{\uparrow, \downarrow} (C_i)\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectHasSelf}(r)) = \; \uparrow (\mathrm{ObjectHasSelf}(r)) \cup \{\mathrm{ObjectHasSelf}(r') \mid r' \in \zeta_{\uparrow, \downarrow}(r)\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectOneOf}(a_1, \dots, a_n)) = \; \uparrow (\mathrm{ObjectOneOf}(a_1, \dots, a_n)) \cup \bigcup_{i=1}^n \{ \mathrm{ObjectOneOf}(\{a_1, \dots, a_n\} \setminus \{a_i\}) \}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectSomeValuesFrom}(r, C)) = \; \uparrow (\mathrm{ObjectSomeValuesFrom}(r, C)) \cup \{\mathrm{ObjectSomeValuesFrom}(r', C) \mid r' \in \zeta_{\uparrow, \downarrow} (r)\} \cup \{\mathrm{ObjectSomeValuesFrom}(r, C') \mid C' \in \zeta_{\uparrow, \downarrow}  (C)\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectAllValuesFrom}(r, C)) = \; \uparrow (\mathrm{ObjectAllValuesFrom}(r, C)) \cup \{\mathrm{ObjectAllValuesFrom}(r', C) \mid r' \in \zeta_{\downarrow, \uparrow} (r)\} \cup \{\mathrm{ObjectAllValuesFrom}(r, C') \mid C' \in \zeta_{\uparrow, \downarrow}  (C)\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectHasValue}(r, a)) = \; \uparrow (\mathrm{ObjectHasValue}(r, a)) \cup \{\mathrm{ObjectHasValue}(r', a) \mid r' \in \zeta_{\uparrow, \downarrow} (r)\} \cup \{\mathrm{ObjectSomeValuesFrom}(r, A) \mid A \in \zeta_{\uparrow, \downarrow}  (\{a\})\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectMinCardinality}(n, r, C)) = \; \uparrow (\mathrm{ObjectMinCardinality}(n, r, C)) \cup \{\mathrm{ObjectMinCardinality}(n', r, C) \mid n' \in \; \downarrow (n)\}  \cup \{\mathrm{ObjectMinCardinality}(n, r', C) \mid r' \in \zeta_{\uparrow, \downarrow}(r)\} \cup \{\mathrm{ObjectMinCardinality}(n, r, C') \mid C' \in \zeta_{\uparrow, \downarrow} (C)\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectMaxCardinality}(n, r, C)) = \; \uparrow (\mathrm{ObjectMaxCardinality}(n, r, C)) \cup \{\mathrm{ObjectMaxCardinality}(n', r, C) \mid n' \in \; \uparrow (n)\}  \cup \{\mathrm{ObjectMaxCardinality}(n, r', C) \mid r' \in \zeta_{\downarrow, \uparrow}(r)\} \cup \{\mathrm{ObjectMaxCardinality}(n, r, C') \mid C' \in \zeta_{\downarrow, \uparrow} (C)\}$
- $\zeta_{\uparrow, \downarrow}(\mathrm{ObjectExactCardinality}(n, r, C)) = \; \uparrow (\mathrm{ObjectExactCardinality}(n, r, C)) \cup \{ \phi_1 \sqcap \phi_2   \mid \phi_1 \in \zeta_{\uparrow, \downarrow} (\mathrm{ObjectMaxCardinality}(n, r, C)) \land \phi_2 \in \zeta_{\uparrow, \downarrow} (\mathrm{ObjectMinCardinality}(n, r, C)) \}$

We define the axiom weakening operator $g_\mathcal{O}$ for OWL 2 axioms as follows:

- $g_\mathcal{O}(\mathrm{SubClassOf}(C, D)) = \{\mathrm{SubClassOf}(C', D) \mid C' \in \rho_\mathcal{O} (C)\} \cup \{\mathrm{SubClassOf}(C, D') \mid D' \in \gamma_\mathcal{O}  (D)\}$
- $g_\mathcal{O}(\mathrm{ClassAssertion}(C, a)) = \{\mathrm{ClassAssertion}(C', a) \mid C' \in \gamma_\mathcal{O}  (C)\}$
- $g_\mathcal{O}(\mathrm{ObjectPropertyAssertion}(r, a)) = \{\mathrm{ObjectPropertyAssertion}(r', a) \mid r' \in \gamma_\mathcal{O}  (r)\} \cup \{ \mathrm{ObjectPropertyAssertion}(r, a), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{NegativeObjectPropertyAssertion}(r, a)) = \{\mathrm{NegativeObjectPropertyAssertion}(r', a) \mid r' \in \rho_\mathcal{O}  (r)\} \cup \{\mathrm{NegativeObjectPropertyAssertion}(r, a), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{SameIndividual}(a_1, \dots, a_n)) =  \bigcup_{i=1}^n \{ \mathrm{SameIndividual}(\{a_1, \dots, a_n\} \setminus \{a_i\}) \}\cup \{ \mathrm{SameIndividual}(a_1, \dots, a_n)\}$
- $g_\mathcal{O}(\mathrm{DifferentIndividuals}(a_1, \dots, a_n)) = \bigcup_{i=1}^n \{ \mathrm{DifferentIndividuals}(\{a_1, \dots, a_n\} \setminus \{a_i\}) \}\cup \{ \mathrm{DifferentIndividuals}(a_1, \dots, a_n)\}$
- $g_\mathcal{O}(\mathrm{EquivalentClasses}(C_1, \dots, C_n)) = \bigcup_{i=1}^n \{ \mathrm{EquivalentClasses}(\{C_1, \dots, C_n\} \setminus \{C_i\}) \} \cup \{ \mathrm{EquivalentClasses}(C_1, \dots, C_n) \}$
- $g_\mathcal{O}(\mathrm{DisjointClasses}(C_1, \dots, C_n)) = \bigcup_{i=1}^n \{ \mathrm{DisjointClasses}(C_1, \dots, C_i', \dots, C_n) \mid C_i' \in \rho_\mathcal{O}(C_i) \}$
- $g_\mathcal{O}(\mathrm{DisjointUnion}(D, C_1, \dots, C_n)) = \{ \mathrm{DisjointUnion}(D, C_1, \dots, C_n), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{EquivalentObjectProperties}(r_1, \dots, r_n)) = \bigcup_{i=1}^n \{ \mathrm{EquivalentObjectProperties}(\{r_1, \dots, r_n\} \setminus \{r_i\}) \} \cup \{ \mathrm{EquivalentObjectProperties}(r_1, \dots, r_n) \}$
- $g_\mathcal{O}(\mathrm{InverseObjectProperties}(s, r)) = \{ \mathrm{InverseObjectProperties}(s, r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{FunctionalObjectProperty}(r)) = \{ \mathrm{FunctionalObjectProperty}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{InverseFunctionalObjectProperty}(r)) = \{ \mathrm{InverseFunctionalObjectPro}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{SymmetricObjectProperty}(r))= \{ \mathrm{SymmetricObjectProperty}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{AsymmetricObjectProperty}(r))= \{ \mathrm{AsymmetricObjectProperty}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{TransitiveObjectProperty}(r)) = \{ \mathrm{TransitiveObjectProperty}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{ReflexiveObjectProperty}(r)) = \{ \mathrm{ReflexiveObjectProperty}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{IrreflexiveObjectProperty}(r)) = \{ \mathrm{IrreflexiveObjectProperty}(r), \bot \sqsubseteq \top \}$
- $g_\mathcal{O}(\mathrm{ObjectPropertyDomain}(r, C)) = \{\mathrm{ObjectPropertyDomain}(r, C') \mid C' \in \gamma_\mathcal{O}  (C)\}$
- $g_\mathcal{O}(\mathrm{ObjectPropertyRange}(r, C)) = \{\mathrm{ObjectPropertyRange}(r, C') \mid C' \in \gamma_\mathcal{O}  (C)\}$
- $g_\mathcal{O}(\mathrm{DisjointObjectProperties}(r_1, \dots, r_n)) = \bigcup_{i=1}^n \{ \mathrm{DisjointObjectProperties}(r_1, \dots, r_i', \dots, r_n) \mid r_i' \in \rho_\mathcal{O}(r_i) \}$