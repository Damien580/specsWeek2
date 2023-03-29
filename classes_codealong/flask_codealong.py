from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    animals = ["Snake", "Eagle", "Hippo"]
    return render_template("home.html", animals=animals)

@app.route("/animal/<animal_name>")
def animal_func(animal):
    for animal in animals:
        if animal["name"] == animal_name
        chosen_animal = animal
    return render_template("animal.html", animal=animal)


if __name__ == "__main__":
    app.run(debug=True)