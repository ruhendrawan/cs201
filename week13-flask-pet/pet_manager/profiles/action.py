from pet_manager.models.pets import Pet

def create_pet_profile(name, type, breed, age):
    return Pet(name, type, breed, age)