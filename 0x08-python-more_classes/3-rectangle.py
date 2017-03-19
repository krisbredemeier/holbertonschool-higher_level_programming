#!/usr/bin/python3
''' Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py) '''

class Rectangle():
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if width < 0:
                raise ValueError ("width must be >= 0")
            self.__width = value
        else:
            raise TypeError ("width must be an integer")
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if heigth < 0:
                raise ValueError ("height must be >= 0")
            self.__height = value
        else:
            raise TypeError ("height must be an integer")

def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

def area(self):
    return (self.__width * self.__height)

def perimeter(self):
    if self.__width == 0 or self.__height == 0:
        return 0
    return (self.__width * 2) + (self.height * 2)


def __str__(self):
    if self.__width == 0 or self.__height == 0:
        raise ValueError ("width and height cannot equal 0")
        return ''
    rectangle_representation = ('#' * self.__width + '\n') * self.__height
    return (rectangle_representation.strip('\n'))
