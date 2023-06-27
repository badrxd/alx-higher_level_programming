#!/usr/bin/python3
""" define a class Square"""


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        x = self.__size ** 2
        return x

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        self.position

    @position.setter
    def position(self, value):
        if ((value is None) or (value[0] < 0) or (value[0] < 0)
                or not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            print("#"*self.__size)
