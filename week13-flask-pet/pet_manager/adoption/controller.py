from flask import render_template
from .action import get_pets_for_adoption
from pet_manager.models.pets import Pet

def adoption_view():
    pets = [
        Pet("Buddy", "Dog", "Golden Retriever", 3), 
        Pet("Whiskers", "Cat", "Siamese", 6),
        Pet("Spike", "Dog", "Bulldog", 1),
        Pet("Fluffy", "Cat", "Persian", 4)
        ]
    adoptable_pets = get_pets_for_adoption(pets)
    return render_template("adoption.html", pets=adoptable_pets)