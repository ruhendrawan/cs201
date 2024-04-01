from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello all!</p>"

@app.route("/spaceship")
# this is the controller action function
def spaceship():
    return "<p>Spaceship</p>"

@app.route("/spaceship_home")
# this is the controller action function
def spaceship_home():
    home = "Earth"
    return spaceship_home_view(home)

def spaceship_home_view(home):
    return f"<p>Spaceship {home}</p>"