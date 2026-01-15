#!/usr/bin/python3
"""Defines a Square class with validated size property and area method."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size=0):
        self.size = size  # go through setter validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
