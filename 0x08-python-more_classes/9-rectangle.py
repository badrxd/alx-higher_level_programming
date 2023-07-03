#!/usr/bin/python3

""" define a class Rectangle"""


class Rectangle():
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): symbole that will be use to draw Rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ the class Rectangle
        Args:
                width: The width of Rectangle.
                height: The height of Rectangle.
        Raise:
                TypeError : raise error if width / height not int
                ValueError : raise error if width/height >= 0
        """
        Rectangle.number_of_instances += 1
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
        """Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        area = 0
        area = (self.__height * self.__width)
        return area

    def perimeter(self):
        """Calculate the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        perimeter = 0
        if (self.__height == 0 or self.__width == 0):
            return perimeter
        perimeter = ((self.__height + self.__width) * 2)
        return perimeter

    def __str__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        strr = ""
        if (self.__height == 0 or self.__width == 0):
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                strr += str(self.print_symbol)
            strr += '\n'
        return strr[:-1]

    def __repr__(self):
        """
        Return a string representation of how to recreate a new instance.
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    @classmethod
    def __del__(cls):
        """
        print message when evry object was deleted
        """
        cls.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with a greater area.

        Args:
            rect_1 (object): The first object.
            rect_2 (object): The second object.
        Raises:
            TypeError: If one of rect_1 or rect_2 is not a obj of Rectangle.
        """
        if (type(rect_1) != Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) != Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        return (rect_2)

    @classmethod
    """Returns a new Rectangle instance with width == height == size

        Args:
            size (int): The first object.
    """
    def square(cls, size=0):
        width = height = size
        return cls(width, height)
