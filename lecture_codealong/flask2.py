from flask import Flask, render_template #importing from the templates folder

app = Flask(__name__)

@app.route("/")
def index():
    name = "Damien"
    letters = list(name)
    pup_dict = {'pup_name':'Sammy'}
    return render_template('flask_templates1.html', name=name,letters=letters, 
                           pup_dict=pup_dict) #this is calling the template i want to import, and any variables I may need to call as well.

if __name__ == "__main__":
    app.run(debug=True, port=7000)