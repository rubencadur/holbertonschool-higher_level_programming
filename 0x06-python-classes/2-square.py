#!/usr/bin/python3
"""Square class with constructor"""


class Square:

    """Class constructor.
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If the size type is not an int
        ValueError: If size is less than 0
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
