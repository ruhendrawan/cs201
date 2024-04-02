from pet_manager.profiles.controller import profile_view
from pet_manager.healthcare.controller import healthcare_view
from pet_manager.adoption.controller import adoption_view

from flask import Flask, render_template
# from package flask import class Flask

# If you don't have flask installed, you can install it by running the command below
# pip3 install flask


# create an app instance of the Flask class
app = Flask(__name__)

# define using decorator
# a route for the home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/profile')
def profile():
    return profile_view()

@app.route('/healthcare')
def healthcare():
    return healthcare_view()

@app.route('/adoption')
def adoption():
    return adoption_view()

# run the app; if the script is executed directly using:
#   flask run
#   or
#   flask --app app --debug run
if __name__ == '__main__':
    app.run(debug=True)