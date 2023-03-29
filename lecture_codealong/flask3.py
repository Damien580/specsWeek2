from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = False
    return render_template('flask_templates2.html', user_logged_in=user_logged_in)

if __name__ == "__main__":
    app.run(debug=True, port=8000)