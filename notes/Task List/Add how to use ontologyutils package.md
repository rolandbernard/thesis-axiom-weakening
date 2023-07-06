# Add how to use ontologyutils package

Date Created: April 24, 2023 6:24 PM
Status: Done
Tags: thesis, uni

Add the following to the pam.xml:

```xml
<repositories>
    <repository>
        <id>github</id>
        <url>https://maven.pkg.github.com/rolandbernard/*</url>
    </repository>
</repositories>
```

And then add the following dependency:

```xml
<dependency>
  <groupId>ontologyutils</groupId>
  <artifactId>ontologyutils</artifactId>
  <version>0.0.1</version>
</dependency>
```
