#!/usr/bin/python3
"""1-rectangle, built for ALX Python project 0x08 task 1.
"""
class Rectangle:
    """The @property decorator is used to define a method as a "getter" for a class attribute, and the @[name].setter decorator is used to define a method as a "setter" for a class attribute. In this case, the width and height attributes are private, and are accessed and modified through the getter and setter methods defined with the @property and @[name].setter decorators.
    The __init__ method is a special method in Python classes that is called when an instance of the class is created. It is used to initialize the attributes of the instance. In this case, the __init__ method takes optional width and height arguments, and sets the values of the self.width and self.height attributes.
    The isinstance function is used to check if a value is an instance of a particular type. In this case, it is used to check if the value argument passed to the width and height setters is an integer. If it is not, a TypeError exception is raised. If the value is an integer but is less than 0, a ValueError exception is raised.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
