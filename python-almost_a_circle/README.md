# Almost a Circle

## Getter Setter Syntax
```
    @property
    def x(self):
        """ Retrieves x of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x of rectangle """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value
```

What are args and kwargs?
- 
How do you use each?
What container types work nicely with args and kwargs (think unpacking)
Discuss how you decided what to test with unittests.
What were some important test cases you thought of?
Discuss serialization and deserialization of objects.
1. dump(): This method is used to serialize to an open file object
2. dumps(): This method is used for serializing to a string
3. load(): This method deserializes from an open-like object.
4. loads(): This does deserialization from a string.
