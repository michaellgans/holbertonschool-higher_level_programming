# Classes

## Object Oriented Programming
- Procedure-oriented - a program designed around functions.  
- Object Oriented - combine data and functionality and wrap it into an "object"
- Class - creates a new "type"
    - Just like how int is a data type of a variable
- Objects - creates a new instance of a class
    - Just like how x is a variable
    - Stores data using varaibles that "belong" to the object.
    - Attribute of a class.
- Instance - Aka a variable.
- Fields - data inside the variable is called a "field"
    - Attribute of a class.
    - Can belong to the object or the class itself.
        - Instance Variables - belong to object
        - Class Variables - belong to class
- Methods - functions of a class vs functions that are independent.
    - Attribute of a class.
    - Functions always get Python's variable of `self`, and is written `def my_func(self, other vars):`
- Namespaces - Variables that are valid ONLY within the context of the class or object that owns them.

## The `Self`
- Class methods have the class before the function, like `class.function()` and there is always a variable added by Python called `self`.

## `__init__ Method`
- Run automatically when an object of a class is created.  To use that object, you don't call `__init__` specifically.

## Class Syntax
```
""" Documentation """


class my_class
""" Documentation """
    fields and methods of classes are indented
```
### Robot Example
```
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
```
#### Output:
```
$ python oop_objvar.py
(Initializing R2-D2)
Greetings, my masters call me R2-D2.
We have 1 robots.
(Initializing C-3PO)
Greetings, my masters call me C-3PO.
We have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.
R2-D2 is being destroyed!
There are still 1 robots working.
C-3PO is being destroyed!
C-3PO was the last one.
We have 0 robots.
```

## FYSK

Name | Syntax | Notes
---|---|---
class | `class` | Creates a class
