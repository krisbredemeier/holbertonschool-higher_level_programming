import Tkinter as tk

class TaskModel():
    def __init__(self, title):
        if not title or type(title) is not str:
            raise Exception("title is not a string")
        self.__title = title
        self.__callback_title = None

    def __str(self):
        return str(self.__title)

    def get_title(self):
        return self.__title

    def set_callback_title(self, callback_title):
        self.__callback_title = callback_title

    def toggle(self):
        self.__title = self.__title[::-1]
        if self.__callback_title:
            self.__callback_title(self.__title)
