# Role hierarchy weakening

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

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any RIA $\phi = s_1 \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $\phi' = s_1 \circ \cdots \circ s_n \sqsubseteq r'$ where $r \sqsubseteq_\mathcal{O} r'$, is entailed by $\mathcal{R}$.

Proof:

1. Take an arbitrary model $M$ of $\mathcal{R}$.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are satisfied by $M$ because $M$ satisfies all axioms in $\mathcal{R}$.
3. We know that $r^M \subseteq r'^M$.
4. Since $M$ satisfies all axioms in $\mathcal{R}$, it satisfies $\phi$ meaning $s_1^M \circ \cdots \circ s_n^M \subseteq r^M$.
5. Using the transitivity of the subset relation on sets, we obtain $s_1^M \circ \cdots \circ s_n^M \subseteq r'^M$.
6. By definition, it follows that $M$ satisfies $\phi'$.
7. Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, $M$ satisfies all axioms of $\mathcal{R}'$ and is therefore a model for $\mathcal{R}'$.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any RIA $\phi = s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $\phi' = s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s_i' \sqsubseteq_\mathcal{O} s_i$, is entailed by $\mathcal{R}$.

Proof:

1. Take an arbitrary model $M$ of $\mathcal{R}$.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are satisfied by $M$ because $M$ satisfies all axioms in $\mathcal{R}$.
3. We know that $s_i'^M \subseteq s_i^M$.
4. Since $M$ satisfies all axioms in $\mathcal{R}$, it satisfies $\phi$ meaning $s_1^M \circ \cdots \circ s_i^M \circ \cdots \circ s_n^M \subseteq r^M$.
5. From $s_i'^M \subseteq s_i^M$ it follows that $s_1^M \circ \cdots \circ s_i'^M \circ \cdots \circ s_n^M \subseteq s_1^M \circ \cdots \circ s_i^M \circ \cdots \circ s_n^M$.
6. Using transitivity of the subset relation on sets, we obtain $s_1^M \circ \cdots \circ s_i'^M \circ \cdots \circ s_n^M \subseteq r^M$.
7. By definition, it follows that $M$ satisfies $\phi'$.
8. Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, $M$ satisfies all axioms of $\mathcal{R}'$ and is therefore a model for $\mathcal{R}'$.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any role assertion $\phi = \mathrm{Dis}(s_1, s_2)$ in $\mathcal{R}$ with a RIA $\phi' = \mathrm{Dis}(s_1', s_2')$ where $s_1' \sqsubseteq_\mathcal{O} s_1$ and $s_2' \sqsubseteq_\mathcal{O} s_2$, is entailed by $\mathcal{R}$.

Proof:

1. Take an arbitrary model $M$ of $\mathcal{R}$.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are satisfied by $M$ because $M$ satisfies all axioms in $\mathcal{R}$.
3. We know that $s_1'^M \subseteq s_1^M$ and $s_2'^M \subseteq s_2^M$.
4. Since $M$ satisfies all axioms in $\mathcal{R}$, it satisfies $\phi$ meaning $s_1^M \cap s_2^M = \empty$.
5. We know that $s_1'^M \cap s_2'^M \subseteq s_1^M \cap s_2^M = \empty$.
6. By definition, it follows that $M$ satisfies $\phi'$.
7. Since all other axioms of $\mathcal{R}'$ are also in $\mathcal{R}$, $M$ satisfies all axioms of $\mathcal{R}'$ and is therefore a model for $\mathcal{R}'$.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any simple RIA $\phi = s \sqsubseteq r$ in $\mathcal{R}$ for which $s$ is simple with a RIA $\phi' = s \sqsubseteq r'$ where $r' \in \mathbf{R}$, is regular.

Proof:

1. Since $\mathcal{R}$ is regular, there exist a relation $\prec$ that satisfies the necessary conditions.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are $\prec$-regular.
3. It follows that since $s$ is simple, the new RIA is $\prec$-regular.
4. Since $\mathcal{R}'$ contains no other axioms, all axioms in $\mathcal{R}'$ are $\prec$-regular.
5. $\mathcal{R}'$ is regular since $\prec$ is an admissible regular order.

**Lemma:** The RBox $\mathcal{R}'$, obtained by replacing any RIA $\phi = s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $\phi' = s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \sqsubseteq r$ where $s'$ is simple, is regular.

Proof:

1. Since $\mathcal{R}$ is regular, there exist a relation $\prec$ that satisfies the necessary conditions.
2. All axioms in $\mathcal{R}'$ that are also in $\mathcal{R}$ are $\prec$-regular.
3. We handle each case of $\phi$ separately:
    1. $\phi = r \circ r \sqsubseteq r$: $r \circ s' \sqsubseteq r$ ($s' \circ r \sqsubseteq r$) is $\prec$-regular because the first (last) roles in the left-hand side are equal to the right-hand side and $s'$ is simple.
    2. $\phi = \mathrm{Inv}(r) \sqsubseteq r$: $s' \sqsubseteq r$ is $\prec$-regular because $s'$ is simple.
    3. $\phi = r \circ s_1 \circ \cdots \circ s \circ \cdots \circ s_n \sqsubseteq r$ ($\phi = s_1 \circ \cdots \circ s \circ \cdots \circ s_n \circ r \sqsubseteq r$): $r \circ s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \sqsubseteq r$ ($s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \circ r \sqsubseteq r$) is $\prec$-regular because since the original axiom is $\prec$-regular, we know that $s_i$ is simple or $s_i \prec r$ for all $i = 1, \dots, n$. Additionally, the first (last) role on the left-hand side is equal to the right-hand side and $s'$ is simple.
    4. $\phi = s_1 \circ \cdots \circ s \circ \cdots \circ s_n \sqsubseteq r$: $s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \sqsubseteq r$ is $\prec$-regular because $s'$ is simple and since the original axiom is $\prec$-regular, we know that $s_i$ is simple or $s_i \prec r$ for all $i = 1, \dots, n$.
4. We conclude that the new axiom is $\prec$-regular.
5. Since $\mathcal{R}'$ contains no other axioms, all axioms in $\mathcal{R}'$ are $\prec$-regular.
6. $\mathcal{R}'$ is regular since $\prec$ is an admissible regular order.

**Lemma:** The RBox $\mathcal{R}'$ is obtained by replacing any simple RIA $\phi = s \sqsubseteq r$ in $\mathcal{R}$ for which $s$ is simple with a RIA $\phi' = s \sqsubseteq r'$ where $r' \in \mathbf{R}$. All roles that are simple in $\mathcal{R}$ are also simple in $\mathcal{R}'$.

Proof:

1. Let $t$ be an arbitrary role that is simple in $\mathcal{R}$.
2. $t$ is simple in $\mathcal{R}'$ because:
    1.  $t \not= u$, otherwise $t$ would not be simple in $\mathcal{R}$.
    2. $t$ does not appear on the right-hand side of a complex RIA. The only new axiom in $\mathcal{R}'$ is $\phi'$.  $\phi'$ is a simple RIA.
    3. $t$ does not appear in a simple RIA where the left-hand side is non-simple. The only new axiom in $\mathcal{R}'$ is $\phi'$. The left-hand side of $\phi'$, $s$, is simple.
    4. $\mathrm{Inv}(t)$ is simple because it is simple in $\mathcal{R}$ and the above three points hold also for $\mathrm{Inv}(t)$.
3. Since $t$ is an arbitrary simple role from $\mathcal{R}$, all simple roles in $\mathcal{R}$ are simple in $\mathcal{R}'$.

**Lemma:** The RBox $\mathcal{R}'$ is obtained by replacing any RIA $\phi = s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \sqsubseteq r$ in $\mathcal{R}$ with a RIA $\phi' = s_1 \circ \cdots \circ s' \circ \cdots \circ s_n \sqsubseteq r$ where $s'$ is simple. All roles that are simple in $\mathcal{R}$ are also simple in $\mathcal{R}'$.

Proof:

1. Let $t$ be an arbitrary role that is simple in $\mathcal{R}$.
2. $t$ is simple in $\mathcal{R}'$ because:
    1.  $t \not= u$, otherwise $t$ would not be simple in $\mathcal{R}$.
    2. $t$ does not appear on the right-hand side of a complex RIA. The only new axiom in $\mathcal{R}'$ is $\phi'$. If $\phi'$ is a complex RIA and $t = r$, then $t$ would not be simple in $\mathcal{R}$ because it is on the right-hand side of the complex RIA $\phi$. This contradicts our assumption that $t$ is simple.
    3. $t$ does not appear in a simple RIA where the left-hand side is non-simple. The only new axiom in $\mathcal{R}'$ is $\phi'$. The left-hand side of $\phi'$, $s'$, is simple.
    4. $\mathrm{Inv}(t)$ is simple because it is simple in $\mathcal{R}$ and the above three points hold also for $\mathrm{Inv}(t)$.
3. Since $t$ is an arbitrary simple role from $\mathcal{R}$, all simple roles in $\mathcal{R}$ are simple in $\mathcal{R}'$.
