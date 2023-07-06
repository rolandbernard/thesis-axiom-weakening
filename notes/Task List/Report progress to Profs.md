# Report progress to Profs

Date Created: April 23, 2023 5:05 AM
Status: Done
Tags: thesis, uni

I have implemented, in the prototype, the weakening of $\mathcal{SROIQ}$ as proposed in the KR and [CEUR-WS](https://ceur-ws.org/Vol-2663/paper-8.pdf) paper (with some minor modifications). Also, I added normalization to convert the most relevant axiom types (I ignored the data property ones, since I don't know that they do). I have further added weakening of the role hierarchy, in such a way that it works in full $\mathcal{SROIQ}$ as follows:

- The role covers $\mathrm{UpCover}$ and $\mathrm{DownCover}$ still contain only simple roles, but simple, not with respect to the reference ontology, but to the full ontology. (It must not be this strict, but considering only the reference ontology is insufficient.) This is required also for the scheme in the KR paper. I have not found it mentioned there explicitly, but the reference ontology must otherwise contain all axioms that make any role non-simple.
- A simple RIA $s \sqsubseteq r$ where $s$ is simple (again with respect to the full ontology) may be weakened to $s \sqsubseteq r'$ where $r' \in \mathrm{UpCover}_\mathcal{O^{ref}}(r)$.
- A (possibly complex) RIA $s_1 \circ \cdots \circ s_n \sqsubseteq r$ may be weakened to $s_1 \circ \cdots \circ s_i' \circ \cdots \circ s_n \sqsubseteq r$ where $s_i' \in \mathrm{DownCover}(s_i)$.
- A disjoint role axiom $\mathrm{Dis}(s_1, s_2)$ may be weakened to $\mathrm{Dis}(s_1, s_2')$ or $\mathrm{Dis}(s_1', s_2)$ where $s_i' \in \mathrm{DownCover}(s_i)$.

Also, unrelated to the weakening, I added an option to instead of computing all maximal consistent sets (because that is very slow sometimes) find only some of them using [this](https://link.springer.com/content/pdf/10.1007/978-3-642-39799-8_39.pdf?pdf=inline%20link) and [this algorithm](https://web-ainf.aau.at/pub/jannach/files/Conference_IJCAI_2015.pdf) I have seen referenced in the Protégé debugger plugins source code.

The restrictions are not strict enough to ensure regularity of the weakened ontology when using the definition in papers, but the one in booklet is nearly enough if we allow also inverse object properties on the right-hand side. The restrictions in OWL are permissive enough to make this weakening always preserve regulatory.
