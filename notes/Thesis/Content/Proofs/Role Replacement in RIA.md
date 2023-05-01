# Role Replacement in RIA

We take $s \sqsubseteq_\mathcal{O} r$ to hold if in every model $M$ of the ontology $\mathcal{O}$, $s^M \subseteq r^M$ holds. Further, $s \sqsubset_\mathcal{O} r$ holds if and only if $s \sqsubseteq_\mathcal{O} r$ and not $r \sqsubseteq_\mathcal{O} s$.

We define the upward and downward cover of roles based on these relations as follows:

$$
\mathrm{UpCover}_\mathcal{O}(r) = \{ s \in \mathbf{R}^S \mid r \sqsubseteq_\mathcal{O} s \land \lnot \exists s' \in \mathbf{R}^S \, . \, r \sqsubset_\mathcal{O} s' \sqsubset_\mathcal{O} s \} \\ \mathrm{DownCover}_\mathcal{O}(r) = \{ s \in \mathbf{R}^S \mid s \sqsubseteq_\mathcal{O} r \land \lnot \exists s' \in \mathbf{R}^S \, . \, s \sqsubset_\mathcal{O} s' \sqsubset_\mathcal{O} r \}
$$

Let $\mathcal{R}$ be the regular RBox of the $\mathcal{SROIQ}$ ontology $\mathcal{O}$. A model of a $\mathcal{R}$ is an interpretation that satisfies all axioms in $\mathcal{R}$. We say that an $\mathcal{R}$ entails another RBox $\mathcal{R}'$(or $\mathcal{R}'$ is entailed by $\mathcal{R}$), if every model of $\mathcal{R}$ is also a model of $\mathcal{R}'$.

**Lemma:** For all $r' \in \mathrm{UpCover}_\mathcal{O}(r)$ and every model $M$ of $\mathcal{O}$, $r^M \subseteq r'^M$.

Proof: Following the definition of $\mathrm{UpCover}_\mathcal{O}(\cdot)$, $r \sqsubseteq_\mathcal{O} r'$ holds and by definition $r^M \subseteq r'^M$ must therefore be true in every model.

**Lemma:** For all $r' \in \mathrm{DownCover}_\mathcal{O}(r)$ and every model $M$ of $\mathcal{O}$, $r'^M \subseteq r^M$.

Proof: Following the definition of $\mathrm{DownCover}_\mathcal{O}(\cdot)$, $r' \sqsubseteq_\mathcal{O} r$ holds and by definition $r'^M \subseteq r^M$ must therefore be true in every model.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r' \in \mathrm{UpCover}_\mathcal{O}(r)$, is entailed by $\mathcal{R}$.

Proof:

1. Take an arbitrary model $M$ of $\mathcal{R}$.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are satisfied by $M$ because $M$ satisfies all axioms in $\mathcal{R}$.
3. We know using [**Lemma:** For all $r' \in \mathrm{UpCover}_\mathcal{O}(r)$ and every model $M$ of $\mathcal{O}$, $r^M \subseteq r'^M$.](Role%20Replacement%20in%20RIA.md) that $r^M \subseteq r'^M$.
4. Since $M$ satisfies all axioms in $\mathcal{R}$, it satisfies $s_1 \circ \cdots \circ s_n \sqsubseteq r$ meaning $s_1^M \circ \cdots \circ s_n^M \subseteq r^M$.
5. Using the transitivity of the subset relation on sets, we obtain $s_1^M \circ \cdots \circ s_n^M \subseteq r'^M$.
6. By definition, it follows that $M$ satisfies $s_1 \circ \cdots \circ s_n \sqsubseteq r'$.
7. Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, $M$ satisfies all axioms of $\mathcal{R}'$ and is therefore a model for $\mathcal{R}'$.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s' \in \mathrm{DownCover}_\mathcal{O}(s_i)$, is entailed by $\mathcal{R}$.

Proof:

1. Take an arbitrary model $M$ of $\mathcal{R}$.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are satisfied by $M$ because $M$ satisfies all axioms in $\mathcal{R}$.
3. We know using [**Lemma:** For all $r' \in \mathrm{DownCover}_\mathcal{O}(r)$ and every model $M$ of $\mathcal{O}$, $r'^M \subseteq r^M$.](Role%20Replacement%20in%20RIA.md) that $s_i'^M \subseteq s_i^M$.
4. Since $M$ satisfies all axioms in $\mathcal{R}$, it satisfies $s_1 \circ \cdots \circ s_i \circ \cdots \circ s_n \sqsubseteq r$ meaning $s_1^M \circ \cdots \circ s_i^M \circ \cdots \circ s_n^M \subseteq r^M$.
5. From $s_i'^M \subseteq s_i^M$ it follows that $s_1^M \circ \cdots \circ s_i'^M \circ \cdots \circ s_n^M \subseteq s_1^M \circ \cdots \circ s_i^M \circ \cdots \circ s_n^M$.
6. Using transitivity of the subset relation on sets, we obtain $s_1^M \circ \cdots \circ s_i'^M \circ \cdots \circ s_n^M \subseteq r^M$.
7. By definition, it follows that $M$ satisfies $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$.
8. Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, $M$ satisfies all axioms of $\mathcal{R}'$ and is therefore a model for $\mathcal{R}'$.

**Lemma:** There exists a consistent ontology $\mathcal{O}$ with a regular RBox $\mathcal{R}$ such that a non-regular RBox $\mathcal{R}'$ can be obtained by replacing some RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r' \in \mathrm{UpCover}_\mathcal{O}(r)$.

Proof:

1. For example, take the following ontology $\mathcal{O}$:
    - $a \circ b \circ a \sqsubseteq c$
    - $\top \sqsubseteq \forall c . \bot$
2. Note that the ontology is regular and consistent. Its RBox is equal to $\mathcal{R} = \{ \, a \circ b \circ a \sqsubseteq c \, \}$.
3. Notice further that for all models $M$ of $\mathcal{O}$, $c^M = \empty \subseteq b^M$ holds, i.e. $c \sqsubseteq_\mathcal{O} b$.
4. Since $a, b, a^-, b^- \not\sqsubset_\mathcal{O} b$ and $b$ is simple, we have $b \in \mathrm{UpCover}_\mathcal{O}(c)$.
5. We replace $\mathcal{R}$ with $\mathcal{R}' = \{ \, a \circ b \circ a \sqsubseteq b \, \}$.
6. Using the definition of regularity, there must be a strict pre-order (i.e. an irreflexive and transitive relation) $\prec$ over $\mathbf{R}$. Since $a \circ b \circ a \sqsubseteq b$ does not follow any of the other rules,  $b \prec b$ must hold. However, this contradicts our assumption that $\prec$ is irreflexive.
7. It follows that $\mathcal{R}'$ is not regular. Also note that $b$ is no longer simple in $\mathcal{R}'$.

**~~Lemma:** There exists a consistent ontology $\mathcal{O}$ with a regular RBox $\mathcal{R}$ such that a non-regular RBox $\mathcal{R}'$ can be obtained by replacing some RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with some RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s' \in \mathrm{DownCover}_\mathcal{O}(s_i)$.~~

~~Proof:~~

1. ~~For example, take the following ontology $\mathcal{O}$:~~
    - ~~$a \circ b \circ a \sqsubseteq c$~~
    - ~~$\top \sqsubseteq \{ i \}$~~
    - ~~$c (i, i)$~~
    - ~~$b(i, i)$~~
2. ~~Following the same reasoning as above, we obtain that $c \equiv_\mathcal{O} b$.~~
3. ~~Since $c \equiv_\mathcal{O} b$ we have $c \in \mathrm{DownCover}_\mathcal{O}(b)$.~~
4. ~~We replace $\mathcal{R}$ with $\mathcal{R}' = \{ \, a \circ c \circ a \sqsubseteq c \, \}$.~~
5. ~~Since this RBox is equivalent to the proof above, we conclude that $\mathcal{R}'$ is not regular.~~ 

The above example does not consider that $c$ must be simple.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s' \in \mathrm{DownCover}_\mathcal{O}(s_i)$, is regular.

Proof: This is not true for the definition of regular presented here, but it holds trivially for the definition in [Foundations of Description Logics]() since all $s'$ will be simple, and simple roles are not considered in the restriction.
