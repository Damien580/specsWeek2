def read_csv(file):
    from pprint import pprint
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            pprint(row)         
read_csv("sample.csv")

class Cupcake:
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
        
cupcake1 = Cupcake("Triple Chocolate", 2.99, "chocolate", "chocolate", "chocolate")

cupcake1.add_sprinkles("Oreo crumbs", "chocolate", "vanilla")

print(cupcake1.sprinkles)