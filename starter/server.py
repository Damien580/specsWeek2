from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    pass










if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")