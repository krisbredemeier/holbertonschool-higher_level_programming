import Tkinter as tk

class TaskView(tk.Toplevel):
    def __init__(self, master=None):
        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        self.master = master

        tk.Frame.__init__(self, master)

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(master, textvariable=self.__title_var)

        self.toggle_button = tk.Button(self, text="Reverse")
        self.toggle_button.pack(side = 'left')

    def update_title(self, title):
        if not title or not isinstance(title, str):
            raise Exception("title is not a string")
        self.__title_var.set(title)
        self.__title_label.pack(side = 'right')
