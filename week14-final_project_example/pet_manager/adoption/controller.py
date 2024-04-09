import sqlite3
from flask import render_template
from .action import get_pets_for_adoption
from pet_manager.models.pets import Pet


def fetch_pets_from_db(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, type, breed, age FROM pets")
    pet_rows = cursor.fetchall()
    pets = [Pet(name, type, breed, age) for name, type, breed, age in pet_rows]
    return pets


def adoption_view(conn):
    # Data access
    pets = fetch_pets_from_db(conn)
    
    # Business logic
    adoptable_pets = get_pets_for_adoption(pets)
    
    # Presentation: Passing the data (as Model objects) to the template
    return render_template("adoption.html", pets=adoptable_pets)