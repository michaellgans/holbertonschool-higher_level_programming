# Python - Data Structures: Lists and Tuples
Hello Everyone! 😀 <br>
Here are the notes I took durring this project. <br>
If you have questions, don't hesitate to reach out via slack. <br>

## Lists

#### Printing a List
- If you include the `=[]` in the for loop, you create a new list instead of using the current one.  
- If you want to print the list in reverse, you can use the `reversed()` function.  
	- It's important to note that using the `reversed()` function works with sequences and not ranges.
```
for VAR in range(len(LIST)):
  print("{:d}".format(LIST[x]))
```

## Tuples
- A tuple with a single item inside it needs to have a , after the first entry.  Otherwise it's just a string.

## Tuples vs List
Concept | Tupple | List
:---|:---|:---|:---
Synax | `name()` | `name[]`
Can you change them? | immutable | mutable

## In vs Not In
-`if x in range(a, b)` - Is x in the range of a through b?
-`if x not in range(a, b)` - Is x not in the range of a through b?

## FYSK (Functions You Should Know)

Name | Syntax | Use Case | Resource
:---|:---|:---|:---
String Format Method | `print("{:d}".format(VAR))` | printing integers in string format | [Link](https://www.geeksforgeeks.org/python-string-format-method/)
Range | `range(start, stop, step)` | define a range of numbers | [Link](https://www.geeksforgeeks.org/python-range-function/)
Reverse | `reversed(sequence)` | reverse a list | [Link](https://www.geeksforgeeks.org/python-reversed-function/)
Copy | copy(sequence)` or `sequence.copy()` | copies a list | [Link](https://www.w3schools.com/python/python_lists_copy.asp)
List | 'list(sequence)` or `sequence.list()` | copies a list | [Link](https://www.w3schools.com/python/python_lists_copy.asp)
Translate | `translation = {ASCII: new ASCII}\n string.translate(translation)` | translates and ASCII character into a new ASCII character | [Link](https://www.geeksforgeeks.org/python-string-translate/)
