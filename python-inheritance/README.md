# Inheritance

-  The subclass inherits methods from the superclass, but it doesn't automatically execute that method when an instance of the subclass is created. If you want to use the logic from a method in the subclass's __init__ method, you need to call it explicitly.


## FYSK

Syntax | Description
---|---
`dir()` | Lists the available attributes and methods of an object.
`my_data.sort()` | Sorts in ascending order automatically
`my_data.sort(reverse=True)` | Sorts in decending order
`type()` | checks for an exact class match
`isinstance()` | checks for inheritance relationships