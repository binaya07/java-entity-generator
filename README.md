# java-entity-generator

Generates a Java entity class from the list of columns provided using JPA specification.

Run `python generate.py`

Provide class name and column names

```
Enter class name : test
Enter columns as comma separated values (eg column1, column2) : "CLONE" VARCHAR2(4000 BYTE), "PROTEIN" VARCHAR2(4000 BYTE), "TARGET_GENE" VARCHAR2(4000 BYTE)
Generates Test.java file as below

```

public class Test {

@Column(name="CLONE")
private String clone;

@Column(name="PROTEIN")
private String protein;

@Column(name="TARGET_GENE")
private String targetgene;

}

```

```
