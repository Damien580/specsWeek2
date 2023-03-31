import csv
from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, del_cupcake_dictionary

app = Flask(__name__)



@app.route("/")
def home():
    cupcakes = get_cupcakes("sample.csv")
    order = get_cupcakes("order.csv")
    order_total = round(sum([float(x["price"]) for x in order]), 2)
    return render_template("index.html", cupcakes=cupcakes, items_num=len(order), order_total=order_total)



@app.route("/add/<name>")
def add(name):
    cupcake = find_cupcake("sample.csv", name)
   
    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake=cupcake)
        return redirect (url_for("home"))
    else:
        return "Sorry, we do not have that!"

@app.route("/each/<name>")
def each(name):
    cupcake=find_cupcake("sample.csv", name)
    print(cupcake)
    
    if cupcake:
        return render_template("each.html", cupcake=cupcake)
    else:
        return "Sorry cupcake not found."

@app.route("/cart")
def cart():
    cupcakes=get_cupcakes("order.csv")
    
    cupcakes_counted = []
    cupcake_set = set()
    
    for cupcake in cupcakes:
        cupcake_set.add((cupcake["name"], cupcake["price"], cupcakes.count(cupcake)))
        
    return render_template("cart.html", cupcakes=cupcake_set)
    
@app.route("/delete/<name>")
def delete(name):
   
    del_cupcake_dictionary("order.csv", name)
    return redirect(url_for("cart"))
    
        




if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")