from flask import render_template
from .action import create_health_record
from pet_manager.models.pets import Pet

def healthcare_view():
    pet = Pet("Buddy", "Dog", "Golden Retriever", 3)
    record = create_health_record(pet, "Vaccinated, Neutered")
    return render_template("healthcare.html", pet=pet, record=record)
