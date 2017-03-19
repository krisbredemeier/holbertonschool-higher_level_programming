#!/usr/bin/python3
''' Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py) '''

class Rectangle():
    @property
    def width(self):
        '''retrieve'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set'''
        if isinstance(value, int):
            if width < 0:
                raise ValueError ("width must be >= 0")
            self.__width = value
        else:
            raise TypeError ("width must be an integer")
    @property
    def height(self):
        '''retrieve'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set'''
        if isinstance(value, int):
            if heigth < 0:
                raise ValueError ("height must be >= 0")
            self.__height = value
        else:
            raise TypeError ("height must be an integer")

def __init__(self, width=0, height=0):
    '''Instantiation'''
    self.width = width
    self.height = height
