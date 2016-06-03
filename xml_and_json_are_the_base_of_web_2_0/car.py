import json
import xml.dom.minidom
from xml.dom.minidom import Node, Document

class Car():

    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            inithash = args[0]

            name = inithash.get('name')
            brand = inithash.get('brand')
            nb_doors = inithash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not str:
            raise Exception("name is not a string")
        if brand == None or not str:
            raise Exception("brand is not a string")
        if nb_doors <= 0 or not int:
            raise Exception("nb_doors is not > 0")

        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    def __str__(self):
        return self.__name + " " + self.__brand + " (" + str(self.__nb_doors)+ ")"

    def get_name(self):
        return self.__name
    def get_brand(self):
        return self.__brand
    def get_nb_doors(self):
        return self.__nb_doors

    def to_hash(self):
        return {'nb_doors': self.__nb_doors, 'brand': self.__brand, 'name': self.__name}

    def set_nb_doors(self, nb_doors):
        self.__nb_doors = nb_doors

    def to_json_string(self):
       return json.dumps(self.to_hash())

    def to_xml_node(self, doc):

        car = doc.createElement('Car')
        car.setAttribute('nb_doors', str(self.__nb_doors))
        # doc.appendChild(car)

        name = doc.createElement('name')
        name_content = doc.createCDATASection(self.__name)
        name.appendChild(name_content)
        car.appendChild(name)

        brand = doc.createElement('brand')
        brand_content = doc.createTextNode(self.__brand)
        brand.appendChild(brand_content)
        car.appendChild(brand)
        return car
