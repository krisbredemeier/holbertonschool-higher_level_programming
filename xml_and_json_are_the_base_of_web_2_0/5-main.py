import json
from car import Car
import xml.dom.minidom
from xml.dom.minidom import Node, Document

with open("5-main.json") as json_file:
    json_data = json.load(json_file)
cars = []
brands = []
for car in json_data:
    name2 = car['name']
    brand2 = car['brand']
    nb_doors2 = car['nb_doors']
    cars.append(Car(name=str(name2), brand=str(brand2), nb_doors=int(nb_doors2)))
total_nb_doors = 0
for car in cars:
    if car.get_brand() not in brands:
        brands.append(car.get_brand())
    total_nb_doors += car.get_nb_doors()

print len(brands)
print total_nb_doors
print cars[3]

xmlstr = '<cars>\n</cars>\n'
doc = xml.dom.minidom.parseString(xmlstr)
for car in cars:
    doc.getElementsByTagName('cars')[0].appendChild(car.to_xml_node(doc))

print doc.toxml(encoding='utf-8')
