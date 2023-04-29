# Modified Role Replacement in RIA

Let the relation $\sqsubseteq_\mathcal{O}^*$ over the set of roles $\mathbf{R}$ be the smallest reflexive and transitive relation, such that:

- $s \sqsubseteq_\mathcal{O}^* r$ holds for each simple RIA $s \sqsubseteq r$ in the ontology $\mathcal{O}$.
- If $s \sqsubseteq_\mathcal{O}^* r$ then $\mathrm{Inv}(s) \sqsubseteq_\mathcal{O}^* \mathrm{Inv}(r)$.

If $s \sqsubseteq r$ holds in an interpretation, then so does $\mathrm{Inv}(s) \sqsubseteq \mathrm{Inv}(r)$. It follows then from [Entailed RIA depend on RBox](Entailed%20RIA%20depend%20on%20RBox.md) that if $s \sqsubseteq_\mathcal{O}^* r$ then the ontology $\mathcal{O}$ entails the axiom $s \sqsubseteq r$. Note that the inverse is not true, i.e. $s \sqsubseteq r$ being entailed by $\mathcal{O}$ does not imply $s \sqsubseteq_\mathcal{O}^* r$.

We define $s \equiv_\mathcal{O}^* r$ iff both $s \sqsubseteq_\mathcal{O}^* r$ and $r \sqsubseteq_\mathcal{O}^* s$ hold. Further, we define  $s \sqsubset_\mathcal{O}^* r$ to hold iff $s \sqsubseteq_\mathcal{O}^* r$ but not $r \sqsubseteq_\mathcal{O}^* s$.

We define the upward and downward cover of roles based on these relations as follows:

$$
\mathrm{UpCover}_\mathcal{O}^*(r) = \{ s \in \mathbf{R} \mid r \sqsubseteq_\mathcal{O}^* s \land \lnot \exists s' \in \mathbf{R} \, . \, r \sqsubset_\mathcal{O}^* s' \sqsubset_\mathcal{O}^* s \} \\ \mathrm{DownCover}_\mathcal{O}^*(r) = \{ s \in \mathbf{R} \mid s \sqsubseteq_\mathcal{O}^* r \land \lnot \exists s' \in \mathbf{R} \, . \, s \sqsubset_\mathcal{O}^* s' \sqsubset_\mathcal{O}^* r \}
$$

Let $\mathcal{R}$ be the regular RBox of the $\mathcal{SROIQ}$ ontology $\mathcal{O}$.

**Lemma:** If $s \sqsubseteq_\mathcal{O}^* r$ then every model $M$ of $\mathcal{O}$ satisfies the axiom $s \sqsubseteq r$.

Proof: The proof is similar to the one in [Entailed RIA depend on RBox](Entailed%20RIA%20depend%20on%20RBox.md), however, the universal, empty, and inverse roles must be considered.

**Lemma:** For all $r' \in \mathrm{UpCover}_\mathcal{O}^*(r)$ and every model $M$ of $\mathcal{O}$, $r^M \subseteq r'^M$.

Proof:

1. Following the definition, $r \sqsubseteq_\mathcal{O}^* r’$ holds and using [**Lemma:** If $s \sqsubseteq_\mathcal{O}^* r$ then every model $M$ of $\mathcal{O}$ satisfies the axiom $s \sqsubseteq r$.](Modified%20Role%20Replacement%20in%20RIA.md)  we know that $r \sqsubseteq r’$ holds in every model $M$ of $\mathcal{O}$. Since $M \vDash r \sqsubseteq r’$, by definition $r^M \subseteq r’^M$ must be true.
2. The rest of the proof goes analogous to the one for $\mathrm{UpCover}_\mathcal{O}(\cdot)$ in [Role Replacement in RIA](Role%20Replacement%20in%20RIA.md).

**Lemma:** For all $r' \in \mathrm{DownCover}_\mathcal{O}^*(r)$ and every model $M$ of $\mathcal{O}$, $r'^M \subseteq r^M$.

Proof:

1. Following the definition, $r' \sqsubseteq_\mathcal{O}^* r$ holds and using [**Lemma:** If $s \sqsubseteq_\mathcal{O}^* r$ then every model $M$ of $\mathcal{O}$ satisfies the axiom $s \sqsubseteq r$.](Modified%20Role%20Replacement%20in%20RIA.md) we know that $r' \sqsubseteq r$ holds in every model $M$ of $\mathcal{O}$. Since $M \vDash r' \sqsubseteq r$, by definition $r'^M \subseteq r^M$ must be true.
2. The rest of the proof goes analogous to the one for $\mathrm{DownCover}_\mathcal{O}(\cdot)$ in [Role Replacement in RIA](Role%20Replacement%20in%20RIA.md).

**Lemma:** The RBox $\mathcal{R}’$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r’ \in \mathrm{UpCover}_\mathcal{O}^*(r)$, is entailed by $\mathcal{R}$.

Proof: The proof goes analogous to the one for $\mathrm{UpCover}_\mathcal{O}(\cdot)$ in [Role Replacement in RIA](Role%20Replacement%20in%20RIA.md) using [**Lemma:** For all $r' \in \mathrm{UpCover}_\mathcal{O}^*(r)$ and every model $M$ of $\mathcal{O}$, $r^M \subseteq r'^M$.](Modified%20Role%20Replacement%20in%20RIA.md).

**Lemma:** The RBox $\mathcal{R}’$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s’ \in \mathrm{DownCover}_\mathcal{O}^*(s_i)$, is entailed by $\mathcal{R}$.

Proof: The proof goes analogous to the one for $\mathrm{DownCover}_\mathcal{O}(\cdot)$ in [Role Replacement in RIA](Role%20Replacement%20in%20RIA.md) using [**Lemma:** For all $r' \in \mathrm{DownCover}_\mathcal{O}^*(r)$ and every model $M$ of $\mathcal{O}$, $r'^M \subseteq r^M$.](Modified%20Role%20Replacement%20in%20RIA.md).

**~~Lemma:** The RBox $\mathcal{R}’$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r’ \in \mathrm{UpCover}_\mathcal{O}^*(r)$, is regular.~~

~~Proof:~~

1. ~~Since $\mathcal{R}$ is regular, there exists a strict regular pre-order $\prec$ on the set of roles $\mathbf{R}$ such that all RIAs in $\mathcal{R}$ are $\prec$-regular. Without loss of generality, we can assume that if $s \prec r \implies \mathrm{Inv}(s) \prec \mathrm{Inv}(r)$.~~
2. ~~All axiom in $\mathcal{R}’$ that are also in $\mathcal{R}$ are $\prec$-regular.~~
3. ~~We show that the new axiom is also $\prec$-regular.~~
4. ~~If $r = r'$, the replacement is trivial.~~
5. ~~If $r \not= r’$, we must show that $s_1 \prec r', \dots, s_n \prec r'$.~~
    1. ~~We know that $r \sqsubseteq_\mathcal{O}^* r’$ by the definition of $\mathrm{UpCover}(\cdot)$.~~
    2. ~~This means there exists a sequence of roles $r_1, \dots, r_n$ such that $r_1 = r$, $r_n = r’$, and $\mathrm{Inv}(r_i) \sqsubseteq \mathrm{Inv}(r_{i + 1})$ or $r_i \sqsubseteq r_{i + 1}$ is in $\mathcal{O}$ for $i = 1, \cdots, n - 1$. Note that $n > 1$ since $r \not= r’$.~~
    3. ~~For all $r_i \sqsubseteq r_{i + 1}$ we have that $r_i \prec r_{i + 1}$.~~
    4. ~~For all $\mathrm{Inv}(r_i) \sqsubseteq \mathrm{Inv}(r_{i + 1})$ we have $\mathrm{Inv}(r_i) \prec \mathrm{Inv}(r_{i + 1})$.~~
    5. $~~\mathrm{Inv}(r_i) \prec \mathrm{Inv}(r_{i + 1})$ implies $r_i \prec r_{i + 1}$.~~
    6. ~~By transitivity of $\prec$ we have $r \prec r’$ and by definition of $\prec$ we conclude also $\mathrm{Inv}(r) \prec r’$.~~
    7. ~~Since all $s_i$ are either $r$, $\mathrm{Inv}(r)$, or $s_i \prec r$ holds, we conclude that $s_1 \prec r', \dots, s_n \prec r’$.~~
6. ~~Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, all axioms of $\mathcal{R}’$ are $\prec$-regular. If follows that $\mathcal{R}'$ is regular.~~

**Counterexample:**

1. Take the RBox $\mathcal{R} = \{ r \circ r \sqsubseteq r, r \sqsubseteq r^- \}$.
2. Since $r \sqsubseteq r^-$ is in $\mathcal{R}$, $r \sqsubseteq_\mathcal{R}^* r^-$ holds.
3. $r^- \in \mathrm{UpCover}_\mathcal{O}^*(r)$.
4. Replacing $\mathcal{R}$ with $\mathcal{R}’ = \{ r \circ r \sqsubseteq r^- , r \sqsubseteq r^- \}.$
5. Using the definition of regularity, there must be a regular strict pre-order (i.e. an irreflexive and transitive relation) $\prec$ over $\mathbf{R}$. Since $r \circ r \sqsubseteq r^-$ does not follow any of the other rules,  $r \prec r^-$ must hold. However, since $\prec$ is regular, this implies $r^- \prec r^-$ which contradicts our assumption that $\prec$ is irreflexive. 
6. It follows that $\mathcal{R}’$ is not regular.

**~~Lemma:** The RBox $\mathcal{R}’$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s’ \in \mathrm{DownCover}_\mathcal{O}^*(s_i)$, is regular.~~

~~Proof:~~

1. 

**~~Lemma:** The RBox $\mathcal{R}’$ is obtained by replacing any RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r’ \in \mathrm{UpCover}_\mathcal{O}^*(r)$. All roles that are simple in $\mathcal{R}$ are also simple in $\mathcal{R}’$.~~

~~Proof:~~

1. 

**~~Lemma:** The RBox $\mathcal{R}’$ is obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s’ \in \mathrm{DownCover}_\mathcal{O}^*(s_i)$. All roles that are simple in $\mathcal{R}$ are also simple in $\mathcal{R}’$.~~

~~Proof:~~

1.
