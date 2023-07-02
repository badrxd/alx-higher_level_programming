#!/usr/bin/python3
"""performing mathematical calculations."""


def add_integer(a, b=98):
    """ return the addtion for a and b

    cast the the number to int if his type is float

    Raises:
        TypeError: If a or b is a non-integer and non-float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
