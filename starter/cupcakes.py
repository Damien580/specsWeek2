import csv
from pprint import pprint
from abc import ABC, abstractmethod





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
    cupcake5,
    cupcake6
]



def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
           writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles}) 
        
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

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
        
    return None
        
def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
        
def del_cupcake_dictionary(file, name):
    del_cupcake=find_cupcake(file, name) #creates dictionary
    del_list = get_cupcakes(file) #creates list
    
    del_list.remove(del_cupcake) #removes dictionary from list
    
    with open(file, "w", newline="\n") as csvfile: #write a new file
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        writer.writeheader()
        
        for cupcake in del_list: #writes each dict from the list to a row
            writer.writerow({"size": cupcake['size'], "name": cupcake['name'], "price": cupcake['price'], "flavor": cupcake['flavor'], "frosting": cupcake['frosting'], "sprinkles": cupcake['sprinkles'], "filling": cupcake['filling']})        
            
        
def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pprint(row)


