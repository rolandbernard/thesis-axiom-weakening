# Entailed RIA depend on RBox

The statement I wanted to proof is not true. Since the ontology can be restricted to contain only a finite number of individuals, and it is possible to fully specify the roles in such a case, role subsumptions can be implied without any RBox axioms.

**Counterexample:** Using only $\mathcal{ACL}$ axioms, the following ontology $\mathcal{O}$ entails $s \sqsubseteq r$ without any TBox axioms:

- $\top \sqsubseteq \forall s . \bot$

**Counterexample:** If the universal role $u$ is simple, the following ontology $\mathcal{O}$ entails $s \sqsubseteq r$ without any TBox axioms:

- $\top \sqsubseteq \; \leq 1 u.\top$
- $\lnot s (u, u)$
- $r(u, u)$

**Counterexample:** Nominals can be used, the following ontology $\mathcal{O}$ entails $s \sqsubseteq r$ without any TBox axioms:

- $\top \sqsubseteq \{ a \}$
- $\lnot s (u, u)$
- $r(u, u)$

**Lemma:** Let $\mathcal{O}$ be a $\mathcal{SROIQ}$ ontology. $\mathcal{O}$ entails $s \sqsubseteq r$ for two roles $s$ and $r$ if ~~and only if~~ there exists a path $a_1, \dots, a_n \in \mathcal{O}$ of simple role inclusion axioms $a_i = s_i \sqsubseteq r_i$ such that $s_1 = s$, $r_n = r$ and $r_i = s_{i + 1}$ for $i = 1, \dots, n - 1$.

Proof (if-direction):

The if-direction follows from the definition of axiom satisfaction in $\mathcal{SROIQ}$.

1. Let $M$ be an arbitrary model of $\mathcal{O}$.
2. It follows that $M \vDash a_i$ for $i = 1, \dots, n$.
3. This means $s_i^M \subseteq r_i^M$ for $i = 1, \dots, n$.
4. By transitivity of the subset relation on sets, we obtain that $s_1^M \subseteq r_n^M$ and $s^M \subseteq r^M$.
5. By definition of the RIA, we conclude that $M$ satisfies $s \sqsubseteq r$.
6. Since $M$ is an arbitrary model, all such models must satisfy $s \sqsubseteq r$ and $\mathcal{O} \vDash s \sqsubseteq r$.

~~Proof (only-if-direction):~~

1. 

**Lemma~~:** Let $\mathcal{O}$ be a $\mathcal{SROIQ}$ ontology that entails an axiom of the form $s \sqsubseteq r$ for two roles $s$ and $r$. The ontology $\mathcal{O}'$ obtained by removing all axioms from $\mathcal{O}$ that are not simple role inclusion axioms also entails $s \sqsubseteq r$.~~

~~Proof:~~

1. ~~By contradiction, assume that $\mathcal{O}'$ does not entail $s \sqsubseteq r$.~~
2. ~~Since $\mathcal{O}' \not\vDash s \sqsubseteq r$ the exists a model $M \vDash \mathcal{O}'$ that does not satisfy $s \sqsubseteq r$.~~
3.
