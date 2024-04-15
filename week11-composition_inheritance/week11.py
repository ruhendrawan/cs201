class Animal:
    def __init__(self):
        self.nest = Nest() # This is composition (has-a relationship)
        pass

    def speak(self):
        print("I am an animal")


# mixin
class DomesticBehaviour:
    def sleep(self):
        print("I am sleeping")


class Dog(Animal, DomesticBehaviour): # Inheritance (is-a relationship): Dog is an Animal
    pass

    # Overriding the speak method
    def speak(self):
        # Extend the functionality of the parent class
        # super().speak() # call the parent class method
        print("I am a dog. Woof! Woof!")


class Nest:
    pass

fluffy = Dog()
fluffy.speak()
fluffy.sleep()
