#!/usr/bin/python3
''' Write a class Rectangle that defines a rectangle '''


class Rectangle():

    number_of_instances = 0
    print_symbol = '#'

    @property
    def width(self):
        '''retrieve'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set'''
        if isinstance(value, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        '''retrieve'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set'''
        if isinstance(value, int):
            if heigth < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        ''''returns the rectangle area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.height * 2)

    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        '''Instantiation'''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        '''print() and str() should print the rectangle with the character #'''
        if self.__width == 0 or self.__height == 0:
            raise ValueError("width and height cannot equal 0")
            return ''
        rectangle_representation = ('#' * self.__width + '\n') * self.__height
        return (rectangle_representation)

    def __repr__(self):
        '''return a string representation of the rectangle to
        be able to recreate a new instance by using eval()'''
        return("Rectangle(%d, %d)" % (self.__width, self.__height))

    def __del__(self):
        '''instance of Rectangle is deleted'''
        return ("Bye rectangle...")
        type(self).number_of_instances -= 1
