#!/usr/bin/python3
"""Defines a Rectangle"""
class Rectangle:
    """Represent a rectangle""" 
    def __init__(self, width=0, height=0):
        """
        This Rectangle class has private instance attributes _width and _height, and defines properties width and height to access and set these attributes. The __init__ method is the constructor for the class and is called when you create a new Rectangle object. The area and perimeter methods return the area and perimeter of the rectangle, respectively.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
