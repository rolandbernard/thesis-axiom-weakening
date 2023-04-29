# $\mathcal{SROIQ}$ Semantics

## Interpretations

The semantics of $\mathcal{SROIQ}$, similar to other description logics, are defined in a model-theoretic way. Therefore, a central notion in that of the interpretations. And *interpretation* $\mathcal{I} = \lang \Delta^\mathcal{I}, \cdot^\mathcal{I} \rang$ consists of a set $\Delta^\mathcal{I}$ called the *domain* of $\mathcal{I}$, and an *interpretation function* $\cdot^\mathcal{I}$. The interpretation function maps the vocabulary elements as follows:

- for each individual name $a \in \mathrm{N}_I$ to an element $a^\mathcal{I} \in \Delta^\mathcal{I}$ in the domain,
- for each concept name $C \in \mathrm{N}_C$ to a subset $C^\mathcal{I} \subseteq \Delta^\mathcal{I}$ of the domain, and
- for each role name $r \in \mathrm{N}_R$ to a relation $r^\mathcal{I} \subseteq \Delta^\mathcal{I} \times \Delta^\mathcal{I}$ over the domain.

An interpretation maps the universal role $u$ to $u^\mathcal{I} = \Delta^\mathcal{I} \times \Delta^\mathcal{I}$.  We extend the interpretation function to operate over inverse roles such that  $\left(r^-\right)^\mathcal{I}$ contains exactly those elements $\lang \delta_1, \delta_2 \rang$ for which $\lang \delta_2, \delta_1 \rang$ is contained in $r^\mathcal{I}$, that is  $\left(r^-\right)^\mathcal{I} = \{ \lang \delta_1, \delta_2 \rang \mid \lang \delta_2, \delta_1 \rang \in r^\mathcal{I} \}$. Further, we define the extension of the interpretation function to complex concepts inductively as follows:

- The top concept is true for every individual in the domain, therefore $\top^\mathcal{I} = \Delta^\mathcal{I}$.
- The bottom concept is true for no individual, hence $\bot^\mathcal{I} = \empty$ where $\empty$ represents the empty set.
- Nominal concepts contain exactly the specified individuals, that is $\{ a_1, \dots, a_n \}^\mathcal{I} = \{ a_1^\mathcal{I}, \dots, a_n^\mathcal{I} \}$.
- $\lnot C$ yields the complement of the extension of $C$, thus $(\lnot C)^\mathcal{I} = \Delta^\mathcal{I} \setminus C^\mathcal{I}$.
- $C \sqcup D$ denotes all individuals that are in either the extension of $C$ or in that of $D$, hence $(C \sqcup D)^\mathcal{I} = C^\mathcal{I} \cup D^\mathcal{I}$.
- $C \sqcap D$ on the other hand, denotes all elements of the domain that are in the extension of both $C$ and $D$, which can be expressed as $(C \sqcap D)^\mathcal{I} = C^\mathcal{I} \cap D^\mathcal{I}$.
- $\exists r . C$ holds for all individuals that are connected by some element in the extension of $r$ to an individual in the extension of $C$, formally $(\exists r . C)^\mathcal{I} = \{ \delta_1 \in \Delta^\mathcal{I} \mid \exists \delta_2 \in \Delta^\mathcal{I} \, . \; \lang \delta_1, \delta_2 \rang \in r^\mathcal{I} \, \land \, \delta_2 \in C^\mathcal{I}  \}$ .
- $\forall r . C$ refers to all domain elements for which all elements in the extension of $r$ connect them to elements in the extension of $C$, that is $(\forall r . C)^\mathcal{I} = \{ \delta_1 \in \Delta^\mathcal{I} \mid \forall \delta_2 \in \Delta^\mathcal{I} \, . \; \lang \delta_1, \delta_2 \rang \in r^\mathcal{I} \to \delta_2 \in C^\mathcal{I} \}$ .
- $\exists r . \mathrm{Self}$ indicates all individuals that the extension of $r$ connects to themselves, hence we let $(\exists r . \mathrm{Self})^\mathcal{I} = \{ \delta \in \Delta^\mathcal{I} \mid \lang \delta, \delta \rang \in r^\mathcal{I}\}$.
- $\leq n r . C$ represents those individuals that have at most $n$ other individuals they are $r$-related to in the concept extension of $C$, that is  $(\leq n r . C)^\mathcal{I} = \{ \delta_1 \in \Delta^\mathcal{I} \mid \left| \{ \delta_2 \in \Delta^\mathcal{I} \mid \lang \delta_1, \delta_2 \rang \in r^\mathcal{I} \, \land \; \delta_2 \in C^\mathcal{I} \} \right| \leq n \}$ where $|S|$ denotes the cardinality of a set $S$.
- $\geq n r.C$ corollary to the case above indicates those domain elements that have at least $N$ such $r$-related elements, $(\geq n r . C)^\mathcal{I} = \{ \delta_1 \in \Delta^\mathcal{I} \mid \left| \{ \delta_2 \in \Delta^\mathcal{I} \mid \lang \delta_1, \delta_2 \rang \in r^\mathcal{I} \, \land \; \delta_2 \in C^\mathcal{I} \} \right| \geq n \}$.

## Satisfaction of Axioms

The purpose of the (extended) interpretation function is mainly to determine satisfaction of axioms. We define in the following when an axiom $\alpha$ is true, or holds, in a specific interpretation $\mathcal{I}$. If this is the case, the interpretation $\mathcal{I}$ satisfies $\alpha$, written $\mathcal{I} \vDash \alpha$. If an interpretation $\mathcal{I}$ satisfies an axiom $\alpha$, we also say that $\mathcal{I}$ is a model of $\alpha$.

- A role inclusion axiom $s_1 \circ \cdots \circ s_n \sqsubseteq r$ holds in $\mathcal{I}$ if and only if for each sequence $\delta_1, \dots, \delta_{n + 1} \in \Delta^\mathcal{I}$ for which $\lang \delta_i , \delta_{i + 1} \rang \in s_i^\mathcal{I}$ for all $i = 1, \cdots, n$, also $\lang \delta_1 , \delta_n \rang \in r^\mathcal{i}$ is satisfied. Equivalently, we can write $\mathcal{I} \vDash s_1 \circ \cdots \circ s_n \sqsubseteq r \iff s_1^\mathcal{I} \circ \cdots \circ s_n^\mathcal{I} \subseteq r^\mathcal{I}$ where $\circ$ denotes the composition of the relations.
- A role reflexivity axiom $\mathrm{Ref}(r)$ hold iff for each element of the domain $\delta \in \Delta^\mathcal{I}$ the condition $\lang \delta , \delta \rang \in r^\mathcal{I}$ is satisfied. In other words, $\mathcal{I} \vDash \mathrm{Ref}(r) \iff \{ \lang \delta, \delta \rang \mid \delta \in \Delta^\mathcal{I} \} \subseteq r^\mathcal{I}$.
- A role asymmetry axioms $\mathrm{Asy}(r)$ is holds $\mathcal{I} \vDash \mathrm{Asy}(r)$ iff $\lang \delta_1 , \delta_2 \rang \in r^\mathcal{I}$ implies that $\lang \delta_2, \delta_1 \rang \not\in r^\mathcal{I}$.
- A role disjointness axiom $\mathrm{Dis}(s, r)$ hold iff the extensions of $r$ and $s$ are disjoint, formally $\mathcal{I} \vDash \mathrm{Dis}(s, r) \iff s^\mathrm{I} \cap r^\mathrm{I} = \empty$.
- A general concept inclusion axiom $C \sqsubseteq D$ is true iff the extension of $C$ is fully contained in the extension of $D$, hence $\mathcal{I} \vDash C \sqsubseteq D \iff C^\mathcal{I} \subseteq D^\mathcal{I}$.
- A concept assertion $C(a)$ holds iff the individual that $a$ is mapped to by $\cdot^\mathcal{I}$ is in the concept extension of $C$, therefore $\mathcal{I} \vDash C (a) \iff a^\mathcal{I} \in C^\mathcal{I}$.
- A role assertion $r(a, b)$ holds iff the individuals denoted by the name $a$ and $b$ are connected in the extension of $r$, thus $\mathcal{I} \vDash r (a, b) \iff \lang a^\mathcal{I}, b^\mathcal{I} \rang \in r^\mathcal{I}$.
- A negative role assertion $\lnot r (a, b)$ is true exactly than when the corresponding role assertion $r (a, b)$ is false. Equivalently,  $\mathcal{I} \vDash \lnot r (a, b) \iff \lang a^\mathcal{I}, b^\mathcal{I} \rang \not\in r^\mathcal{I}$.
- An equality assertion $a = b$ holds iff the individuals identified by $a$ and $b$ are the same element of the domain, alternatively written $\mathcal{I} \vDash a = b \iff a^\mathcal{I} = b^\mathcal{I}$.
- Dual to the above, $a \not = b$ holds iff the names $a$ and $b$ denote different elements, accordingly $\mathcal{I} \vDash a \not= b \iff a^\mathcal{I} \not= b^\mathcal{I}$.

We say a set of axioms holds in an interpretation $\mathcal{I}$ iff every axiom of the set hold in $\mathcal{I}$. Accordingly, $\mathcal{I}$ satisfies a knowledge base $\mathcal{KB}$, written $\mathcal{I} \vDash \mathcal{KB}$, iff $\mathcal{I}$ satisfies every axiom $\alpha \in \mathcal{KB}$ of the knowledgeable, i.e. $\mathcal{I} \vDash \mathcal{KB} \iff \forall \alpha \in \mathcal{KB} \, . \; \mathcal{I} \vDash \alpha$. If $\mathcal{I}$ satisfies $\mathcal{KB}$ we say $\mathcal{I}$ is a model of $\mathcal{KB}$.

# Reasoning tasks

In general, logic-based knowledge representation is useful for the ability to perform reasoning task on knowledge bases. There are a number of reasoning tasks that can be performed by a reasoner in description logics. In this section, we will take a look at three basic reasoning tasks, and how they can be reduced to each other. While there exists other reasoning task, this section will focus on *knowledge base satisfiability,* *axiom entailment, and concept satisfiability*.

## Knowledge base satisfiability

A knowledge $\mathcal{KB}$ base is satisfiable iff there exists a model $\mathcal{I} \vDash \mathcal{KB}$ for $\mathcal{KB}$. Otherwise, the knowledge base is called unsatisfiable, inconsistent, or contradictory. As discussed in [Software Bugs vs Ontology Bugs](Software%20Bugs%20vs%20Ontology%20Bugs.md) an inconsistent knowledge base can be a sign of modelling errors. An inconsistent knowledge base entailed every statement, and as such all information extracted from it is useless. Therefore, an unsatisfiable knowledge base is generally undesirable. Furthermore, both the task of deciding concept satisfiability and axiom entailment can be reduced to deciding knowledge base consistency.

## Axiom entailment

An axiom $\alpha$ is entailed by $\mathcal{KB}$ if every model $\mathcal{I} \vDash \mathcal{KB}$ of the knowledge base also satisfies the axiom $\mathcal{I} \vDash \alpha$. We also write this as $\mathcal{KB} \vDash \alpha$ and say that $\alpha$ is a consequence of $\mathcal{KB}$. Deciding axiom entailment is an important task in order to derive new information from the collected knowledge.

The problem of axiom entailment can be reduced to determining for the satisfiability of a modified knowledge base. This is achieved by using an axiom $\beta$ that imposes the opposite restriction to $\alpha$, to be more precise, for all interpretations $\mathcal{I} \vDash \alpha \iff \mathcal{I} \not\vDash \beta$. If $\alpha$ is entailed by $\mathcal{KB}$, it must hold in every model of $\mathcal{KB}$, hence $\beta$ must not hold in any model. It follows that the extended knowledge base $\mathcal{KB} \cup \{ \, \beta \, \}$ has no new model, and is therefore unsatisfiable. We can consequently solve the axiom entailment problem by testing for satisfiability of a modified knowledge base, if we can find such an opposing axiom for $\alpha$. For some cases in $\mathcal{SROIQ}$ finding such an opposite is obvious, for others the desired behaviour must be emulated with a set of axioms. []($%20mathcal%7BSROIQ%7D$%20Semantics.md) shows the correspondence for every type of $\mathcal{SROIQ}$ axiom.

| $\alpha$ | $\Beta$ |
| --- | --- |
| $s_1 \circ \cdots \circ s_n \sqsubseteq r$ | $s_1(a_1, a_2)$, $\dots$, $s_n(a_n, a_{n + 1})$, and $\lnot r(a_1, a_{n + 1})$ |
| $\mathrm{Dis}(s, r)$ | $s(a, b)$ and $r(a, b)$ |
| $C \sqsubseteq D$ | $(C \sqcap \lnot D)(a)$ |
| $C (a)$ | $\lnot C (a)$ |
| $r (a, b)$ | $\lnot r(a, b)$ |
| $\lnot r (a, b)$ | $r (a, b)$ |
| $a = b$ | $a \not= b$ |
| $a \not= b$ | $a = b$ |

## Concept satisfiability

A concept $C$ is satisfiable with respect to $\mathcal{KB}$ iff there exists a model of the knowledge base $\mathcal{I} \vDash \mathcal{KB}$ such that the extension of $C$ is not empty, i.e. $C^\mathcal{I} \not= \empty$. A concept which is not satisfiable is called unsatisfiable. Clearly, some concepts are unsatisfiable with respect to every knowledge base, for example $\bot$ or $A \sqcap \lnot A$. However, similar to an unsatisfiable knowledge base, an unsatisfiable atomic concept may be an indication of a modelling mistake.

Like axiom entailment, concept satisfiability can be reduced to knowledge base satisfiability. If a concept is unsatisfiable, every model $\mathcal{I} \vDash \mathcal{KB}$ maps the concept to the empty set, that is $C^\mathcal{I} = \empty$. Since the other direction is trivial, we can rewrite this as $C^\mathcal{I} \subseteq \empty$. It follows that since $\bot^\mathcal{I} = \empty$ the every such model satisfies $\mathcal{I} \vDash C \sqsubseteq \bot$, meaning $\mathcal{KB} \vDash C \sqsubseteq \bot$. We conclude that we can test for unsatisfiability of a concept $C$ by checking for entailment of $C \sqsubseteq \bot$.
