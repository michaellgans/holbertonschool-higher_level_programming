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