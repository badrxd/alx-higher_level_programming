#!/usr/bin/python3
"""Defines the Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize new square.

        Args:
            size (int): The size of new square.
        """
        super().__init__(size, size)
        self.__size = size
