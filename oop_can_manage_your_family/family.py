
# creates a family
from datetime import date
import time
import json
import os.path

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

        self.last_name = " "
        self.is_married_to = 0

    def __str__(self):
        return self.__first_name + "," + self.last_name

    def is_male(self):
        if genre in Person.GENRES is not Female:
            return True

    def age(self):
        today = [05/20/2016]
        age = today[2] - self.__date_of_birth[2]
        return today[2] - self.__date_of_birth[2] - ((today[1], today[0]) < (self.__date_of_birth[1], self.__date_of_birth[0]))


    def __lt__(self, other):
        return (self.age < other.age())

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        elif isinstance(other, (int, float)):
            return self.age <= other
        else:
            return NotImplemented

    def __eq__(self, other):
        return (self.age() == other.age())

    def __ne__(self, other):
        return (self.age() != other.age())

    def __gt__(self, other):
        return (self.age() > other.age ())

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        elif isinstance(other, (int, float)):
            return self.age >= other.age
        else:
            return NotImplemented

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

    def last_name(self):
        return self.last_name

    def getname(self):
        return self.__class__.__name__


    def json(self):
        dict = {
        'id':self.__id,
        'eyes_color' :self.__eyes_color,
        'genre' :self.__genre,
        'date_of_birth' :self.__date_of_birth,
        'first_name' :self.__first_name,
        'kind' :self.getname(),
        'last_name' :self.last_name,
        'is_married_to' :self.is_married_to,
        'children' :self.children,

        }
        return dict

    def load_from_json(self, json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.kind = str(json['kind'])
        self.__id = json['id']
        self.__eyes_color = str(json['eyes_color'])
        self.__genre = str(json['genre'])
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = str(json['first_name'])
        self.last_name = str(json['last_name'])
        self.is_married_to = json['is_married_to']
        self.children =  json['children']


# not part of any class
def save_to_file(list, filename):
    with open(filename, 'w') as filename:
        list_of_people = []
        for i in list:
            list_of_people.append(i.json())
        filename.write(json.dumps(list_of_people))

def load_from_file(filename):
    if type(filename) is not str or (not os.path.isfile(filename)):
        raise Exception("filename is not valid or doesn't exist")
    else:
        with open(filename) as data_file:
            data = json.load(data_file)
        People = []
        for n in data:
            if n['kind'] == 'Adult':
                p = Adult(0, " ", [12, 24, 1970], "Female", "Blue")
            if n['kind'] == 'Baby':
                p = Baby(0, " ", [12, 24, 2015], "Female", "Blue")
            if n['kind'] == 'Senior':
                p = Senior(0, " ", [12, 24, 1900], "Female", "Blue")
            if n['kind'] == 'Teenager':
                p = Teenager(0, " ", [12, 24, 2000], "Female", "Blue")
            p.load_from_json(n)
            People.append(p)
        return People


# new classes

#Baby
class Baby(Person):
    def ___int__(self, id, first_name, date_of_birth, genre, eyes_color):
        person.__int__(self, id, first_name, date_of_birth, genre, eyes_color)

    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        return True if self.is_married_to != 0 else False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if (self.is_married_to != 0) or (p.is_married_to != 0):
            raise Exception ("Already married")
        if (not self.can_be_married()) or (not p.can_be_married()):
            raise Exception ("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if (self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind != 'Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or (not self.can_have_child()):
            raise Exception("Can't have baby")
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue':
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green':
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green':
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown':
            eyes_color = 'Brown'
        b = Baby(d,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)

        return b

    def adopt_child(self, c):
        if not self.can_have_child():
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

#Teenager
class Teenager(Person):
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        return True if self.is_married_to != 0 else False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if (self.is_married_to != 0) or (p.is_married_to != 0):
            raise Exception ("Already married")
        if (not self.can_be_married()) or (not p.can_be_married()):
            raise Exception ("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if (self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind != 'Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or (not self.can_have_child()):
            raise Exception("Can't have baby")
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue':
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green':
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green':
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown':
            eyes_color = 'Brown'
        b = Baby(d,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)

        return b

    def adopt_child(self, c):
        if (not self.can_have_child()):
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

#Adult
class Adult(Person):
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        return True if self.is_married_to != 0 else False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if (self.is_married_to != 0) or (p.is_married_to != 0):
            raise Exception ("Already married")
        #if ((not self.can_be_married()) or (not p.can_be_married())):
            #raise Exception ("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if (self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind != 'Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or (not self.can_have_child()):
            raise Exception("Can't have baby")
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue':
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green':
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green':
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown':
            eyes_color = 'Brown'
        b = Baby(d,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)

        return b

    def adopt_child(self, c):
        if not self.can_have_child():
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

#Senior
class Senior(Person):
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        return True if self.is_married_to != 0 else False

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if (self.is_married_to != 0) or (p.is_married_to != 0):
            raise Exception ("Already married")
        if (not self.can_be_married()) or (not p.can_be_married()):
            raise Exception ("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if (self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

        def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
            if (p is None) or ((p.kind != 'Adult') and (p.kind != 'Senior')):
                raise Exception("p is not an Adult of Senior")
            if (not p.can_have_child()) or (not self.can_have_child()):
                raise Exception("Can't have baby")
            if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue':
                eyes_color = 'Blue'
            if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green':
                eyes_color = 'Green'
            if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green':
                eyes_color = 'Blue'
            if p.get_eyes_color() == 'Brown':
                eyes_color = 'Brown'
            b = Baby(d,first_name,date_of_birth,genre,eyes_color)
            if id not in p.children:
                p.children.append(id)
            if id not in self.children:
                self.children.append(id)

            return b
