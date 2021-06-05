# java-entity-generator

Generates a Java entity class from the list of columns provided using JPA specification.

Run `python generate.py`

Provide class name and column names 
```
Enter class name : test
Enter columns as comma separated values (eg column1, column2) : a, b , c
```

Generates Test.java file as below

```
public class Test {

@Column(name="a")
private String a;

@Column(name="b")
private String b;

@Column(name="c")
private String c;

}
```
