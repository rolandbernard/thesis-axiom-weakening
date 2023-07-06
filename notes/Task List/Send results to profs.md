# Send results to profs

Date Created: May 15, 2023 12:17 AM
Status: Done
Tags: thesis, uni

Inspired by our discussion last week, I implemented some caching for the subclass queries in the cover computation, that derives also some information by using the transitivity of the subsumption.

Also, I did some simple testing using the pizza ontology (which is using SHOIN). Before normalization there are 322 axioms (with 218 subconcepts), while after normalization there are 1132 axioms (with 310 subconcepts). I did the test by first making the ontology inconsistent by replacing random axioms by random stronger versions (that are by themselves not inconsistent). Then I made it consistent again, using the repair via weakening. I did 200 such runs, first making it inconsistent and then repairing, with a timeout of 5 minutes per repair. Only 100 runs (50%) completed the repair within the 5 minutes. Of these 100, the mean time required for the repair was 24.7s (std 45.4s; min 1.4s; 25% 3.6s; 50% 6.1s; 75% 18.9s; max 212.8s). I also recorded the number of reasoner calls made, which was a mean of 4922 calls (std 6065; min 52; 25% 1767; 50% 2730; 75% 4334; max 27685).

Running the whole thing without the normalization only 5 out of 100 timed out, and the rest were, compared to the normalized version, faster (mean 3.1s; std 1.7s; min 1.1s; 25% 1.9s; 50% 2.4s; 75% 3.9s; max 10.8s) and used slightly fewer calls to the reasoner (mean 3643; std 3177; min 495; 25% 1621; 50% 2269; 75% 4455; max 12917). I am not sure how much of that is because of the lower number of subconcepts to consider, the number of axioms for finding minimal subsets, or the reasoner being faster on the ontology without normalization.

Also, I made a simple Protégé plugin that adds a simple menu item in “Tools” > “Automatic Repair” and a view in “Window” > “Views” > “Ontology views” > “Manual Axiom Weakening”. The menu item simply applies the automatic repair using weakening and the view shows all axioms, with buttons to compute weakening and strengthening of the axioms.
