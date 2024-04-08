import sqlite3

from pet_manager.profiles.controller import profile_view
from pet_manager.healthcare.controller import healthcare_view
from pet_manager.adoption.controller import adoption_view

from pet_manager.models.pets import Pet
from pet_manager.models.treatments import Treatment

from flask import Flask, render_template, g
# from package flask import class Flask

# If you don't have flask installed, you can install it by running the command below
# pip3 install flask


# create an app instance of the Flask class
app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('pets.db')
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


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
    return adoption_view(get_db())


@app.route('/treatment/<dogname>')
def treatment_view(dogname):
    # For modularity, we can also move the content of this function 
    # to a separate function in the pet_manager/treatment/controller.py file
    # So that app.py only contains the route definitions
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, type, breed, age FROM pets WHERE name = ?", (dogname,))
    pet_data = cursor.fetchone()

    if not pet_data:
        abort(404)  # Aborts the request with a 404 error if the dog is not found

    pet = Pet(*pet_data) 
    # * is used to unpack the tuple pet_data into its individual elements
    # *pet_data is equivalent to pet_data[0], pet_data[1], pet_data[2], pet_data[3]

    # We could optimize this query by joining the tables and fetching the data in a single query
    # This is only for demonstration purposes
    cursor.execute("SELECT date, type, treatment FROM treatments WHERE pet_name = ?", (dogname,))
    treatment_rows = cursor.fetchall()
    for date, type, treatment in treatment_rows:
        pet.add_treatment(Treatment(pet, date, type, treatment))

    return render_template("treatment.html", pet=pet)


# run the app; if the script is executed directly using:
#   flask run
#   or
#   flask --app app --debug run
if __name__ == '__main__':
    app.run(debug=True)