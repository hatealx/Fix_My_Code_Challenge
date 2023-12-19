#!/usr/bin/env python3
"""A class representing a square."""
class Square:
    """A class representing a square."""

    def __init__(self, width=0, height=0):
        """
        Initialize a square with given width and height.

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
            int: The calculated area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The calculated perimeter of the square.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        String representation of the square.

        Returns:
            str: Details about the width and height of the square.
        """
        return f"Width: {self.width}, Height: {self.height}"

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())

