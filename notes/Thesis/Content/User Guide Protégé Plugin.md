# User Guide: Protégé Plugin

- [x]  Add info to repo readme

this section will cover how to install and use the protege plugin developed to allow using the teqniqus presented in the thesis.

installation 

The proege plugin can either be compiled form source, or is available at url(). If you desire to compile the plugin from source, you will need a java 11 jdk and the maven tool. If you have both of these, you can execute thw folowing command to generate the plugin and find the bundled jar file in target/…

verbaitim command to build

The jar file of the plugin must be put into the plugin folder of protege. the location of this folder will vary depending on the platform and configuration of protege. for a linix enviroment for example it woll most likely be lovated in home/.Protege/plugins. After copying the jar file of the plugin into this filder, the plugin will automatically be loaded and initialed the next time protege js started.

Using the Menu

figure: show repair menu

easiest way to use the plugin is by using the added menu items in the tools section of the top menu. There are three main menu items. The normalize sroiq entry will execute the normallizarion of the ontology that has also been used for the evaluation in the thesis. This will transform alll owl 2 acioms into axiosn that more directly correspond to sroiq. Note that doing this is not required before starting the repair, since the axiom weakening operator used in the plugin has been extended to handle all owl 2 axioms.

The following two menu izems are for applying twi different automatic repair algorithms. For each of them There is the option of select between making the ontology only consistent or making it also coherent. Note that when selecting coherence as the goal, the repairs will likely be.slower, also bwcjause computing coherencw is more expensive, at least in the way it is implementdwd for the plugin. the forst reiar method used by the item maximal consistent subset will select some randomly sampled maximal consistent subset. the swcond repair method on the other hand uses the axiom weakening based repair algorithm. Note that for wach of the algorithms there is aslo a choice between slow default or fast. These are some presets that make different choices of how to configure the repair algorithms. To have grather control over these parameters, use the automatic repair view.

Using the Automatic Repair View

figure show selection of algorithms

The automatic repair view can be accessed in window>views>onllogy view>Hshdbs. It allows the user to  select between a number kf different repair algorithms. The one using axioms weakening and the one using a maximal consistent subsest are the same as the ones accessible through the menu. the repair by removal is similar to the axiom weakening based repair, but the axioms are always removed instead oc weakened. the remaining three algorithms are all trying to optimize the IIC of the resulti gbrepairs. for best mcs and best of k this ks done by sampling repairs using ,respecivel6, maximal consistent subsets or axiom Weakening, and then selecting the lne that has the largest inferred call hierarchy. The algorithm used for the best by tree seaech selection on the other hand uses a monte carlo tree search baswd approach to find the ontology with the largest infered class hierachy.

figure show configuration 

For each of these repair algorithms a number of differentconfiguratins cna be made. explain each quickly

Using the Manual Weakening View

figure show list

The last view implemented by the plugisn, and accessible under windows>views>…, allows for manualy computing axiom refinemnts. The biew shows a list of  all acioms in the currently avtive ontology. the axioms are sortey by how frequently they appear in randomly sampled miminal inconsistent subsets. The axioms apperongbthe most often are shown at the top of the list. this means, that the axioms that would be choise for Weakening by the automatic repair algorithms are the onve appearing first in the list. Next to each axiom are tow buttons, with an upwards and downwards arrow. these can be used to, respectively , compute weakenings and streanthenings of the axiom. 

figure show replacement 

Pressing one of these buttons woll bring up a selection dialogue showing rhe results of the axiom weakening or strengthening operator. The user may then select form the presented choices one axiom and click ok. The original axiom will be remived from the ontology and replaced with the selected axioms.
