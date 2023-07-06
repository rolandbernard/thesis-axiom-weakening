# The Even More Irresistible $\mathcal{SROIQ}$

Link: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=18043d97ef80871b1e0de63368e3a0b5c53a6d03
Status: Finished
Tags: logic, thesis
Type: Paper

### Summary

- Extension to $\mathcal{SHOIN}$ that is more expressive but remains decidable.
- Also inspired by the description logic $\mathcal{RIQ}$
- The RBox contains a regular role hierarchy and role assertions
- A role hierarchy is regular if there exists some strict partial ordering $\prec$
    - This is to avoid cyclic dependencies, which lead to undecidability
- For some uses, roles must be simple
- In $\mathcal{SROIQ}$ concept satisfiability with respect to a ABox, RBox, and TBox can be reduced to concept satisfiability with respect to an RBox that contains only $\mathrm{Dis}(R, S)$, $\mathrm{Ref}(R)$, and $\mathrm{Asy}(R)$ assertions and the universal role $U$ does not appear.
- $\mathcal{SROIQ}$ is decidable, and the paper presents a tableau algorithm

### Questions

- [x]  Why is this paper using different notation?
    
    It is much older than the others and also written by different people.
    
- [x]  Must the domain be non-empty?
    
    The domain $\Delta^I$ of an interpretation must be non-empty.
    
- [x]  Does the simplicity of roles depend only on the RBox?
    
    Yes
    
- [x]  Why can $\mathrm{Irr}(R)$ be reduced but $\mathrm{Ref}(R)$ can not?
    
    Because $\mathrm{Irr}(R)$ must be simple already.
    
- [x]  Why do some role have to be simple?
    
    I think it has to do with the construction of the NFA. And it is also used in the soundness proof of the tableau.
    
- [x]  Why does the role hierarchy have to be regular?
    
    I think this might also be related to the construction of the NFA.
    
- [ ]  What is the purpose of the NN-rule?

[TheEvenMoreIrresistibleSROIQ.pdf](The%20Even%20More%20Irresistible%20$%20mathcal%7BSROIQ%7D$/TheEvenMoreIrresistibleSROIQ.pdf)
