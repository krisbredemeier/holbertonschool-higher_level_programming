#!/usr/bin/python3
''' Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py) '''

class Rectangle():
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int)
            width < 0
            ValueError (width must be >= 0)
        TypeError(width must be an integer)
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int)
            heigth < 0
            ValueError(height must be >= 0)
        TypeError(height must be an integer)

def __init__(self, width=0, height=0):
    self.width = width
    self.height = height
