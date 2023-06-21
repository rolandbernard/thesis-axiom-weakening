# $\mathcal{SROIQ}$ Syntax

This section describes the syntax of the $\mathcal{SROIQ}$ description logic [The Even More Irresistible $\mathcal{SROIQ}$]().

The *vocabulary* $\mathrm{N} = \mathrm{N}_I \cup \mathrm{N}_C \cup \mathrm{N}_R$ of a $\mathcal{SROIQ}$ knowledge base is made up of three disjoint sets:

- The set of *individual names* $\mathrm{N}_I$ used to refer to single elements in the domain of discourse.
- The set of *concept names* $\mathrm{N}_C$ used to refer to classes that elements of the domain may be a part of.
- The set of *role names* $\mathrm{N}_R$ used to refer to binary relations that may hold between the elements of the domain.

A $\mathcal{SROIQ}$ knowledge base $\mathcal{KB} = \mathcal{A} \cup \mathcal{T} \cup \mathcal{R}$ is the union of an *ABox* $\mathcal{A}$, a *TBox* $\mathcal{T}$, and a regular *RBox* $\mathcal{R}$. The elements of $\mathcal{KB}$ are called axioms.

## RBox

The RBox $\mathcal{R}$ describes the relationship between different roles in the knowledge base. It consists of two disjoint parts, a role hierarchy $\mathcal{R}_h$ and a set of role assertions $\mathcal{R}_a$.

Given the set of role names $\mathrm{N}_R$, a *role* is either the *universal role* $u$ or of the form $r$ or $r^-$ for some role names $r \in \mathrm{N}_R$, where $r^-$ is called the *inverse role or* $r$. For convenience in the latter definitions, and to avoid roles like $r^{--}$, we define a function $\mathrm{Inv}$ such that $\mathrm{Inv}(r) = r^-$ and $\mathrm{Inv}(r^-) = r$. We denote the set of all roles as $\mathbf{R} = \mathrm{N}_R \cup \{ u \} \cup \{ r^- \mid r \in \mathrm{N}_R \}$.

A *role inclusion axiom* (RIA) is a statement of the form $r_1 \circ \cdots \circ r_n \sqsubseteq r$ where $r, r_1, \dots r_n \in \mathbf{R}$ are roles. For the case in which $n = 1$, we obtain a *simple role inclusion*, which has the form $r \sqsubseteq s$ where $s$ and $r$ are role names (the case where $n > 1$ is called a *complex role inclusion*). A finite set of RIAs is called a *role hierarchy*, denoted $\mathcal{R}_h$.

Roles can be partitioned into two disjoint sets, simple roles and non-simple roles. Intuitively, non-simple roles are those that are implied by the composition of two or more other roles. In order to preserve decidability, $\mathcal{SROIQ}$ requires that in parts of expressions only simple roles are used. We define the set of *non-simple roles* as the smallest set such that:

- the universal role $u$ is non-simple,
- any role $r$ that appears in a RIA of the form $r_1 \circ \cdots \circ r_n \sqsubseteq r$ where $n > 1$ is non-simple,
- any role $r$ that appears in a simple role inclusion $s \sqsubseteq r$ where $s$ is non-simple is itself non-simple, and
- if a role $r$ is non-simple, then $\mathrm{Inv}(r)$ is also non-simple.

All roles which are not non-simple are *simple roles*. We denote the set of all non-simple roles with $\mathbf{R}^N$ and the set of simple roles with $\mathbf{R}^S = \mathbf{R} \setminus \mathbf{R}^N$.

Example:

There is an additional restriction that is placed upon the role hierarchy in a $SROIQ$ knowledge base. The role hierarchy in $\mathcal{SROIQ}$ must be regular. A role hierarchy $\mathcal{R}_h$ is *regular* if there exists a strict partial order $\prec$ (that is, an irreflexive and transitive relation) on the set of roles $\mathbf{R}$, such that $s \prec r \iff \mathrm{Inv}(s) \prec r$ and $s \prec r \iff \mathrm{Inv}(s) \prec \mathrm{Inv}(r)$ for all roles $r$ and $s$, and all RIA in $\mathcal{R}_h$ are $\prec$-regular. A RIA is defined to be $\prec$*-regular* if it is of one of the following forms:

- $\mathrm{Inv}(r) \sqsubseteq r$,
- $r \circ r \sqsubseteq r$,
- $r \circ s_1 \circ \cdots \circ s_n \sqsubseteq r$,
- $s_1 \circ \cdots \circ s_n \circ r \sqsubseteq r$, or
- $s_1 \circ \cdots \circ s_n \sqsubseteq r$,

such that $s_1, \dots, s_n, r \in \mathbf{R}$ are roles, and $s_i$ is simple or $s_i \prec r$ for all $i = 1, \dots, n$.

This condition on the role hierarchy prevents cyclic definitions with role inclusion axioms that include role chains. These types of cyclic definition could otherwise lead to undecidability of the logic.

Example:

Example:

To make axiom weakening simpler, this definition is slightly more general than necessary. The definition of regularity presented here is more permissive than the one in [The Even More Irresistible $\mathcal{SROIQ}$]() in that it always allows simple roles on the left-hand side. Additionally, it is more permissive than stated in [Foundations of Description Logics]() in that it allows for inverse roles on the right-hand side. 

The set of *role assertions* $\mathcal{R}_a$ is a finite set of statements with the form $\mathrm{Dis}(s_1, s_2)$ (*disjointness*) where $s_1$, and $s_2$ are simple roles in $\mathcal{R}_h$. In [The Even More Irresistible $\mathcal{SROIQ}$]() the authors define additionally the role assertions $\mathrm{Sym}(r)$ (*symmetry*), $\mathrm{Asy}(s)$ (*asymmetry*), $\mathrm{Tra}(r)$ (*transitivity*), $\mathrm{Ref}(r)$ (*reflexivity*), and $\mathrm{Irr}(r)$ (*irreflexivity*). These additional assertions can, however, be written using the alternative sets of axioms $\{ r^- \sqsubseteq r \}$, $\{ \mathrm{Dis}(r, r^-) \}$, $\{ r \circ r \sqsubseteq r \}$, $\{ r' \sqsubseteq r , \top \sqsubseteq \exists r'. \mathrm{Self} \}$, and $\{ \top \sqsubseteq \lnot \exists r . \mathrm{Self} \}$ respectively. Note that the asymmetry assertion requires a simple role, and that $r'$ in the case of reflexivity must be a role name not otherwise used in the ontology.

## TBox

The TBox $\mathcal{T}$ describes the relationship between different concepts. In $\mathcal{SROIQ}$, the set of *concept expressions* (or simply *concepts*) given an RBox $\mathcal{R}$ is inductively defined as the smallest set such that:

- $\top$ and $\bot$ are concepts, respectively called *top concept* and *bottom concept*,
- all concept names $C \in \mathrm{N}_C$ are concept, called *atomic concepts*,
- all finite subsets of individual names $\{ a_1, \dots, a_n \} \subseteq \mathrm{N}_I$ are concepts, called *nominal concepts,*
- if $C$ and $D$ are concepts, the $\lnot C$ (*negation*), $C \sqcup D$ (*union*), and $C \sqcap D$ (*intersection*) are also concepts,
- if $C$ is a concept and $r \in \mathbf{R}$ a (possible non-simple) role, then $\exists r . C$ (*existential quantification*) and $\forall r . C$ (*universal quantification*) are also concepts, and
- if $C$ is a concept, $s \in \mathbf{R}^S$ a simple role and $n \in \mathbb{N}_0$ a non-negative number, then $\exists r . \mathrm{Self}$ (*self restriction*), $\leq n s . C$ (*at-most restriction*), and $\geq n s. C$ (*at-least restriction*) are concepts, the last two may together be referred to as *qualified number restrictions.*

Given two concepts $C$ and $D$, a *general concept inclusion axiom* (GCI) **is a statement of the form $C \sqsubseteq D$. The TBox $\mathcal{T}$ is a finite set of general concept inclusion axioms.

## ABox

The ABox $\mathcal{A}$ contains statements about single individuals called individual assertions. An *individual assertion* has one of the following forms:

- $C(a)$ (*concept assertion*) for some concept $C$ and individual name $a \in \mathrm{N}_I$,
- $r(a, b)$ (*role assertion*) or $\lnot r (a, b)$ (*negative role assertion*) for some role $r \in \mathbf{R}$ and individual names $a, b \in \mathrm{N}_I$, or
- $a = b$ (*equality*) or $a \not = b$ (*inequality*) for some individual names $a \in \mathrm{N}_I$.

An ABox $\mathcal{A}$ is a finite set of individual assertions. In $\mathcal{SROIQ}$ due to the inclusion of nominal concepts, all ABox axioms can be rewritten into TBox axioms.
