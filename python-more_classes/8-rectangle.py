#!/usr/bin/python3
""" Creates a class named Rectangle """


class Rectangle:
    """ Initializes the Data for Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ For printing """
        if self.height == 0 or self.width == 0:
            return ""
        else:
            result = ""
            if self.width > 0 and self.height > 0:
                for x in range(self.height):
                    result += str(self.print_symbol) * self.width
                    if x < self.height - 1:
                        result += "\n"
            return result

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def my_print(self):
        if self.height == 0 or self.width == 0:
            return ("")
        else:
            for x in range(self.height):
                for y in range(self.width):
                    print("#", end="")
                print("")

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of Rectangle """
        if self.__width == 0 or self.__height == 0:
            return int(0)
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2
