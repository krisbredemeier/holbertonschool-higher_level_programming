import math
class Square():

    def __init__(self, side_length):
        self.__side_length = side_length
    def __del__(self):
        pass
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    def get_name(self):
        return self.__name
    def set_namer(self, name):
        self.__name = name
    def get_center(self):
        return self.__center
    def set_center(self, center):
        self.__center = center
    def area(self):
        return self.__side_length*self.__side_length
