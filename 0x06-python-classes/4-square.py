#!/usr/bin/python3
"""Square class with constructor"""


class Square:

    """Class constructor."""
    def __init__(self, size=0):
        self.size = size

    """size property: returns the value of the __size attribute."""
    @property
    def size(self):
        return self.__size

    """size setter property: assign the __size attribute.
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If the size type is not an int
        ValueError: If size is less than 0
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    """Method to calculate the area of the square."""
    def area(self):
        return self.__size ** 2
