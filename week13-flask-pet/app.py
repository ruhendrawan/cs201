from pet_manager.profiles.view import profile_view

from flask import Flask
# from package flask import class Flask

# If you don't have flask installed, you can install it by running the command below
# pip3 install flask


# create an app instance of the Flask class
app = Flask(__name__)

# define using decorator
# a route for the home page
@app.route('/home')
def home():
    return "Welcome to the Pet Management Application!"

@app.route('/profile')
def profile():
    return profile_view()

# run the app; if the script is executed directly using:
#   flask run
#   or
#   flask --app app --debug run
if __name__ == '__main__':
    app.run(debug=True)