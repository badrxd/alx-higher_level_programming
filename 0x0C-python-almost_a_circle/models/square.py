#!/usr/bin/python3
""" Module represent class Square,
inheritance from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class of square """
    def __init__(self, size, x=0, y=0, id=None):
        """ """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string of Square class
        Returns:
            string representation
        """
        return ("[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ size getter
        Returns:
            size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter
        Args:
            value(int): size (width / height)
        """
        self.width = value
        self.height = value
