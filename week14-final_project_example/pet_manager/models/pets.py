class Pet:
    def __init__(self, name, type, breed, age):
        self.name = name
        self.type = type
        self.breed = breed
        self.age = age
        self.treatments = []
    
    def add_treatment(self, treatment):
        self.treatments.append(treatment)
    
    def set_treatments(self, treatments):
        self.treatments = treatments