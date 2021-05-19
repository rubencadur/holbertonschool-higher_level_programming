#!/usr/bin/python3
"""Square class with constructor"""


class Square:

    """Class constructor."""
    def __init__(self):
        pass

    """Setter method for the size property.
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If the size type is not an int
        ValueError: If size is less than 0
    """
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    """Method to calculate the area of the square."""
    def area(self):
        return self.__size ** 2
