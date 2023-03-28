import csv
from pprint import pprint
from abc import ABC, abstractmethod


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pprint(row)
# read_csv("sample.csv")


class Cupcake():
    def __init__ (self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    
         
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "Mini"
    
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        

# my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")
# print(my_cupcake_mini.name)
# print(my_cupcake_mini.price)
# print(my_cupcake_mini.size)
        
class Regular(Cupcake):
    size = "Regular"
    
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.filling = filling
    
        
class Large(Cupcake):
    size = "Large"
    
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.filling = filling
        


     
cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Chocolate", None)
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)
cupcake3.add_sprinkles("White")
cupcake4 = Large("Strawberries and Creme", 3.99, "Vanilla", "Strawberry", "Strawberry")
cupcake4.add_sprinkles("Red", "White")
cupcake5 = Mini("Peanut Butter Fudge", 1.99, "Chocolate", "Peanut Butter")
cupcake6 = Regular("Orange Creme", 2.99, "Vanilla", "Orange", "Orange")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5
]
new_cupcake_list = [
    cupcake6
]


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
               writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
# write_new_csv("sample.csv", cupcake_list)

def app_csv(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
app_csv("sample.csv", new_cupcake_list)