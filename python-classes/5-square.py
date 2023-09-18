#!/usr/bin/python3
""" Defines a class """


class Square:
    """ Names the class Square """
    def __init__(self, size=0):
        """ Initiazlies the data """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the area of the square
        Returns:
            The area of a rectangle

        """
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        """ Retrieves size of square """
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # resets size to value

    def my_print(self):
        """ Prints the square """
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print("")
