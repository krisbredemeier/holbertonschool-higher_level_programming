#!/usr/bin/python3
''' Write a class Rectangle that defines a rectangle '''

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

    def area(self):
        '''returns the rectangle area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the rectangle perimeter'''
        if self.__width = 0 or self.__height = 0:
            return 0
        return (self.__width * 2) + (self.height * 2)
