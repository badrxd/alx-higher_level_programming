#!/usr/bin/python3

""" define a class Rectangle"""


class Rectangle():
    """ the class Rectangle
    Args:
            width: The width of Rectangle.
            height: The height of Rectangle.
    Raise:
            raise error if width / height not int
            raise error if width/height >= 0
    Return:
            return a Rectangle shape desinged by "#" symbole
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        area = 0
        area = (self.__height * self.__width)
        return area

    def perimeter(self):
        perimeter = 0
        if (self.__height == 0 or self.__width == 0):
            return perimeter
        perimeter = ((self.__height + self.__width) * 2)
        return perimeter

    def __str__(self):
        """Define the print() representation of a Rectangle."""
        strr = ""
        if (self.__height == 0 or self.__width == 0):
            return("")
        for i in range(self.__height):
            for j in range(self.__width):
                strr += '#'
            strr += '\n'
        return strr[:-1]
