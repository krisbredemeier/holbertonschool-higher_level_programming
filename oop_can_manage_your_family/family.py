class Person():
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        if id < 0 or not int:
            raise Exception("id is not an integer")
        self.__id = id
        if first_name == None or not str:
            raise Exception("string is not a string")
        self.__first_name = first_name
        if len(date_of_birth) != 3 and all(isinstance(n, int) for n in date_of_birth):
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth
        if genre not in Person.GENRES or not str:
            raise Exception("genre is not valid")
        self.__genre = genre
        if eyes_color not in Person.EYES_COLORS or not str:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

    def __del__(self):
        pass

    def get_id(self):
        return self.__id

    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_first_name(self):
        return self.__first_name

    def las_name(self):
        return self.last_name
