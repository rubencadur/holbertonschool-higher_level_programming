#!/usr/bin/python3
"""Square class with constructor, property, setter and print method"""


class Square:
    """Class constructor."""
    def __init__(self, size=0):
        self.size = size

    """size property: returns the value of the __size attribute."""
    @property
    def size(self):
        """size: property to modify private __size attr"""
        return self.__size

    """size setter property: assign the __size attribute.
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If the size type is not an int
        ValueError: If size is less than 0
    """
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    """Method to calculate the area of the square."""
    def area(self):
        return self.__size ** 2

    """Method to print the square with '#'"""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print('#' * self.__size)
