#!/usr/bin/python3
"""Defines a Rectangle class."""
class Rectangle:
    """Represent the Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize width and height."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Width getter."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Widith setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """height getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculates and returns the area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """calculates and returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
