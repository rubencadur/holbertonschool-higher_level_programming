#!/usr/bin/python3
"""Square class with constructor, property, setter and print method"""


class Square:
    """Class constructor."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Size property: returns the value of the __size attribute."""
    @property
    def size(self):
        """size: property to modify private __size attr"""
        return self.__size

    """Size setter property: assign the __size attribute.
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
        else:
            rang = range(self.__size)
            print('\n' * self.__position[1], end="")
            for _ in rang:
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)

    """Position property: returns the value of the __position attribute"""
    @property
    def position(self):
        return self.__position

    """Position setter property: assign the __position attribute"""
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
          or type(value[0]) is not int or value[0] < 0 \
          or type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
