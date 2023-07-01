# User Guide: Prototype Implementation

- [x]  Rename to prototype implementation since both are on java
- [x]  Update the readme with this info

This section will explain how to use the prototype implemented for the evaluation. There are two main ways in which someone may want to use the implementation. First, as a java library for axiom weakening. This use case will only be discussed briefly. Second, the prototype may be used to apply the weakening based repair to owl ontogeny files using the implemented apps.

Building the Software 

The prototype is implemented in Java, and will require at least java version 17. The Maven tool is used for dependency management. To download and build the project, the following code can be executed.

verbaitim copy from readme.

If you would rather use the pre-packaged jar file, those are also available on the GitHub repository. Note that the releases may be out of date with the master branch of the repository.

Use as a Library

Since the project is implemented as a maven project it is possible to use it as a dependency for another maven project. Of you have build the project yourself and ran mavem install, it is enough to add the following to your pom.xml file.

verbaitim of pom

There is also the possibility to let maven handle the install form the repository by adding zhe folowin configuration to the pom.xml.

verbaitim of pom

Javadoc comments are included for most classes and methods, so it should be rather easy to understand the structure of the project.

Useing the Applications

To simply use the applications used for the evaluation in ghis thesis, use the jar fule produced during building. The roduced output at shaded-ontology.jar will included all the necessary depencies. From there it js enough to run the jar file using the command ofnthe form … Where aap.jdhdjd. is replaced with one of the following.

- all apps.

To get specific information about how to use a app, simply use the --help option. For wxample the following isbthe help output for the RepairWeakening application.

verbatim help output

To repair the ontology … amd write the repaird ontology to …, for example, using the configuration used for the evaluaton, one would execute thebfollowing command.

verbaitim example command
