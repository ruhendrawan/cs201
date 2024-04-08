import sqlite3
import csv

from pet_manager.models.pets import Pet
from pet_manager.models.treatments import Treatment

def create_tables(cursor):
    cursor.execute('''CREATE TABLE pets (name TEXT, type TEXT, breed TEXT, age INTEGER)''')
    cursor.execute('''CREATE TABLE treatments (pet_name TEXT, date TEXT, type TEXT, treatment TEXT)''')

def insert_pet_data(cursor, pets):
    for pet in pets:
        cursor.execute("INSERT INTO pets VALUES (?, ?, ?, ?)", (pet.name, pet.type, pet.breed, pet.age))

def insert_treatment_data(cursor, treatments):
    for treatment in treatments:
        cursor.execute("INSERT INTO treatments VALUES (?, ?, ?, ?)", (treatment.pet.name, treatment.date, treatment.type, treatment.treatment))

def load_pets_from_csv(filename):
    pets = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pet = Pet(row['name'], row['type'], row['breed'], int(row['age']))
            pets.append(pet)
    return pets

def main():
    pets = load_pets_from_csv('pets.csv')

    treatments = [
        Treatment(pets[0], "2024-01-10", "Vaccination", "Rabies Vaccine"),
        Treatment(pets[0], "2024-02-15", "Checkup", "General Health Check"),
        Treatment(pets[0], "2024-03-05", "Grooming", "Nail Trimming"),

        Treatment(pets[1], "2024-01-20", "Grooming", "Fur Trimming"),
        Treatment(pets[1], "2024-02-25", "Vaccination", "Feline Distemper Vaccine"),
        Treatment(pets[1], "2024-03-15", "Dental", "Teeth Cleaning"),

        Treatment(pets[2], "2024-01-30", "Vaccination", "Kennel Cough Vaccine"),
        Treatment(pets[2], "2024-02-20", "Checkup", "Allergy Assessment"),
        Treatment(pets[2], "2024-03-10", "Grooming", "Ear Cleaning"),

        Treatment(pets[3], "2024-01-05", "Grooming", "Hair Brushing"),
        Treatment(pets[3], "2024-02-10", "Vaccination", "Rabies Vaccine"),
        Treatment(pets[3], "2024-03-20", "Checkup", "Eye Exam")
    ]

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    create_tables(cursor)
    insert_pet_data(cursor, pets)
    insert_treatment_data(cursor, treatments)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
