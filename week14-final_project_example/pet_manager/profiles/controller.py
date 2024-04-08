from flask import render_template
from .action import create_pet_profile

def profile_view():
    pet = create_pet_profile("Buddy", "Dog", "Golden Retriever", 3)
    return render_template("profile.html", pet=pet)