# pet_manager/profiles/view.py
from flask import render_template
from .controller import create_pet_profile

def profile_view():
    pet = create_pet_profile("Buddy", "Dog", "Golden Retriever", 3)
    return render_template("profill", pet=pet)e.htm