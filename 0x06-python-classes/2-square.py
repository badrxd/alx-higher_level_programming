#!/usr/bin/python3
""" define a class Square"""


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Initialize class """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else if size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
