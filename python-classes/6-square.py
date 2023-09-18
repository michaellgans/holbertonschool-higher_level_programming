#!/usr/bin/python3
""" Defines a class """


class Square:
    """ Names the class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initiazlies the data """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[1], int) or not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Retrieves position of the square """
        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value  # resets position to value

    def my_print(self):
        """ Prints the square relative to the position """
        if self.__size == 0:
            print("")
            return

        if self.__position[1] != 0:
            for x in range(self.__position[1]):
                print("")

        for y in range(self.__size):
            if self.__position[0] > 0:
                for z in range(self.__position[0]):
                    print(" ", end="")
            for b in range(self.__size):
                print("#", end="")
            print("")
