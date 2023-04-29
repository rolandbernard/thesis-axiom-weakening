# Improved Role Replacement in RIA

Let the relation $\rightarrow_\mathcal{O}^*$ over the set of roles $\mathbf{R}$ be the smallest reflexive and transitive relation, such that:

- For each role inclusion axiom $s_1, \dots, s_n \sqsubseteq r$ in the ontology $\mathcal{O}$, $s_i \rightarrow_\mathcal{O}^* r$ holds for $i = 1, \dots, n$.
- $r \rightarrow_\mathcal{O}^* Inv(r)$ for every role $r \in \mathbf{R}$.

Intuitively, this relation encodes the dependencies between roles.

We define the upward and downward cover of roles based on this relation as follows:

$$
\mathrm{UpCover}_\mathcal{O}^\triangle(r) = \{r,  \, s \in \mathbf{R} \mid  r \sqsubseteq_\mathcal{O} s \land \lnot (s \rightarrow_\mathcal{O}^* r) \land \lnot \exists s' \in \mathbf{R} \, . \, r \sqsubset_\mathcal{O} s' \sqsubset_\mathcal{O} s  \} \\ \mathrm{DownCover}_\mathcal{O}^\triangle(r) = \{r,  \, s \in \mathbf{R} \mid s \sqsubseteq_\mathcal{O} r \land \lnot (r \rightarrow_\mathcal{O}^* s) \land \lnot \exists s' \in \mathbf{R} \, . \, s \sqsubset_\mathcal{O} s' \sqsubset_\mathcal{O} r \}
$$

Let $\mathcal{R}$ be the regular RBox of the $\mathcal{SROIQ}$ ontology $\mathcal{O}$.

**Lemma:** The RBox $\mathcal{R}’$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r’ \in \mathrm{UpCover}_\mathcal{O}^\triangle(r)$, is regular.

Proof:

1. Since $\mathcal{R}$ is regular, there exists a strict regular pre-order $\prec$ on the set of roles $\mathbf{R}$. Let $\prec$ be the minimal such relation.
2. Note that by definition $\prec$ is a subset of $\rightarrow_\mathcal{O}^*$.
3. All axiom in $\mathcal{R}’$ that are also in $\mathcal{R}$ are $\prec$-regular.
4. We show that the new axiom is $\prec'$-regular for some regular strict pre-order $\prec’ \supseteq \prec$.
5. If $r = r'$, the replacement is trivial and the axiom is $\prec$-regular.
6. If $r \not= r’$, we must show that $s_1 \prec' r', \dots, s_n \prec' r'$.
    1. 
    2. 
7. Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, all axioms of $\mathcal{R}’$ are $\prec'$-regular. If follows that $\mathcal{R}'$ is regular.

**Lemma:** The RBox $\mathcal{R}’$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s’ \in \mathrm{DownCover}_\mathcal{O}^\triangle(s_i)$, is regular.

Proof:

1. 

**Lemma:** The RBox $\mathcal{R}’$ is obtained by replacing any RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r’ \in \mathrm{UpCover}_\mathcal{O}^\triangle(r)$. All roles that are simple in $\mathcal{R}$ are also simple in $\mathcal{R}’$.

Proof:

1. 

**Lemma:** The RBox $\mathcal{R}’$ is obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s’ \in \mathrm{DownCover}_\mathcal{O}^\triangle(s_i)$. All roles that are simple in $\mathcal{R}$ are also simple in $\mathcal{R}’$.

Proof:

1.