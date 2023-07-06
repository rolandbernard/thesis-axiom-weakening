# Try to make the prototype faster

Date Created: March 23, 2023 12:04 PM
Description: The prototype can probably be made more efficient, that would allow running more experiments
Status: Done
Tags: thesis, uni

- [x]  Remove the ontology form manager after use
- [x]  Cache the ontology and reasoner for multiple queries
- [x]  Compute only some maximal and minimal subsets
- [x]  Try porting FaCT++ as it seems to be faster
- [x]  Do more benchmarking
- [x]  Can we apply some useful caching to the covers?
    - [x]  Could be good to cache the subclass/superclass relations
    - [x]  Would be nice to avoid computing all every time
- [x]  Profile the repair of a large ontology and find the bottlenecks.
