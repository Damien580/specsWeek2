from flask import Flask
app = Flask(__name__)



@app.route('/')  #127.0.0.1:5000 - landing page
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route('/information') #127.0.0.1:5000/information - information page
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')    #127.0.0.1/puppy/<enter a name here> will display the page for that puppy name.
def puppy(name):
    return "<h1>100th letter: {}</h1>".format(name[100])





if __name__ == "__main__":
    app.run(debug=True)