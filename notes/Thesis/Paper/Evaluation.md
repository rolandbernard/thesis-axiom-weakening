# Evaluation

The evaluation of the proposed refinement and axiom weakening operator has been carried out using the implementation(footnote with link to repo and sha1 of commit) on different ontologies from BioPortal (cite bioportal). Additionally the pizza ontology (cite or footnote) was included in the testing. The chosen ontologies use a varying expressive features. On average they contain X axioms, Y concept names, Z role names, and subconcepts. Table (table with ontologies) shows the chosen ontologies and their characteristics.

Table: (ontology, full name, expressivity, axioms, classes, roles, subconcepts) Ontologies used for evaluation. Values have been taken after pre-processing.

Since the ontologies use OWL 2, the axioms and concepts do not map directly to SROIQ, in order to follow the definitions laid out in (section with definitions). During the preprocessing, we further removed axioms related to data properties and any axiom that caused any OWL 2 DL profile violation. Unless otherwise noted, the FaCT++ reasoner (cite FaCT++) was used for all the experiments presented in this paper.

## Evaluating quality of repairs

in order to evaluate the proposed approach of axiom weakening specifically for its the application in ontology repair, we need a way to compare different possible repairs 

as mentioned in (alc weakening) the problem of deciding which of two repairs is preferable is generally not wll defined. As such this thesis will, similar to what has been proposed in (alc weakening), use the inferred concept hierarchy to evaluate the repair. 

definition: of inffered concept hierarchy

To get a relative measure of quality between two ontologies, we compare them based on the differences in infereences. We use for this purpose the inferred information content defined in (alc weakening) as follows.

definition: iic

the intuition behind this choice of measure is the following. 0.5 they are equally good. > 0.5 O1 is better and < 0.5 O2 is better.

Note that if the cardinality of the inferred concept hierarchy is larger for one ontology, then it will also be preferred by the iic.

The main advantage of using iic to compare repairs as opposed to using the inferred concept hierarchy is that it removes the influence of entailments shared by both ontologies.

One possible criticism against this method of comparing repairs is that it does not consider subsumptions between complex concepts. This deficiency has already been noted by the authors of (alc weakening).

The evaluation precedes by first making the ontologies inconsistent. This was achieved by repeatedly adding axioms to the ontology until they became inconsistent. The newly added axioms were generated by strengthening randomly selected axioms of the original ontology. It was ensured that the added axioms on their own were not inconsistent. After making the ontology inconsistent, it was repaired using both a randomly sampled maximal consistent subset and the repair algorithm using axiom Weakening presented in section (repair using axiom weakening). This process, both making the ontology inconsistent and repairing it, was repeated one hundred times for each ontology, and the iic was computed between the repair by weakening and the maximal consistent subset. The evaluation was performed using a randomly selected maximal consistent subset as the reference ontology and by sampling 16 minimal inconsistent subsets during the selection of bad axioms.

While the utilized OWL 2 DL reasoners are all highly optimized, they exhibit undesirable performance in some edge cases. Mostly, they need only a few milliseconds to perform a entailment or consistency check task using the selected ontologies. However, when performance pitfalls are encountered, they make the repair unreasonably slow. For this reason a timeout of 5 minutes was placed on the repairs execution and the outputs of these runs where discarded and replaced by new runs. The results of these experiments are listed in table (table with results) and shown in figure (figure with results).

table: results of tables

figure: results of figures 

From these results it can be seem that the repair using weakening is not in general better than choosing a random maximal consistent subset. This is in contrast to the results previously shown for repairing ALC ontologies in (alc weakening) where repair by weakening was preferred over classical repairs for the majority of ontologies. We observe in figure (figure) that in some cases repair by weakening perfoms better, while in others the random maximal consistent subset provided perrwr results on general.

## Evaluating effectiveness of caching

As discussed in section (about implementation), to accelerate the computation of upward and downward covers, a cache was implemented to prevent repeated calls to the reasoner, when the necessary information has already been queried for previous computations. This section will discuss the experiments performed to evaluate the effectiveness of the cache implementation.

Three versions of the upward and downward cover have been considered, the uncached version that calls the reasoner for every subsumption query, a version that caches only the exact queries that were already made previously, and finally the version that additionally infers some additional information from the transitivity of subsumption.

The experiment uses the same ontologies as used for the previously discussed evaluation into the repair quality. The logical axioms of each ontology where selected uniformly at random to form one hundred groups with a fixed number of axioms. Each of the groups was than tested with a separate cache. The rationale behind testing with different group sizes is that the cache will obviously have a greater impact the more cover computations are performed with it.

In each test run, the axioms weakening operator was applied to each axiom and the number of reasoner calls and (real) time taken were measured. The weakening operator used the original ontology as the reference ontology. This test was carried out once with each version of the covers. The test has further been performed using different reasoners. The final results of the evaluation can be seen in table (table with results) and are visualized in figure (figure of results) using a violin plot.

Table: with results of evaluation. showing the average time per single weakening.

Figure: with results of evaluation. the datapoints represent the average time per single weakening for each group.

We can see clearly from the results that the cache is indeed effective at lowering both the number of reasoner calls and execution time. While the simple caching method provides a dramatic decrease in the number of reasoner calls, it provides only a rather modes increase in performance. This can likely be attributed largely to internal caching performed by the reasoners. The full cache using information extracted using transitivity again significantly reduces the number of reasoner call, but comes also with a noticeable decrease in reasoning times. It can be concluded that the addition of the cache greatly benefits computation of the axiom weakening operator.

## Evaluating performance

Performance of the repairs has also been evaluated. During each repair by maximally consistent subset or weakening, the time taken and the number of calls to the reasoner have been registered. This has also been done for the process of making the ontologies inconsistent. Additionally, the number of steps taken by the repair using axiom Weakening has been observed. Also, as mentioned in section (quality evaluation), the repair program was put under a timeout to prevent cases where the reasoning became unreasonably slow. The generation of inconsistent ontoloies used a similar timeout and the same procedure was used for reasoner errors. Timeout of the weakening procedure are shown separately from those latter cases in the results. The frequency of these cases is indicated as percentage of the overall tests performed. The results of this evaluation are presented in table (table with results) and figure (figure with results).

table: results for the evaluations. failed: 15% (21%). Failed comimn shows the percentage of Timeout triggered by the repair process, and in parenthesis the number of total failed runs includong timeout during generation of inconsistent ontoloies and reasoner errors.

figure: results for the evaluation

As is visible from the results, the number of reasoner calls and the execution time show a very high variance. The execution times were generally reasonable when a run was able to complete within the time limit. A significant number of runs, however, was affected by the timeout or other errors.
