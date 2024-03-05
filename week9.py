class Car:
   def __init__(self, make, model, year, color):
       self.make = make
       self.model = model
       self.year = year
       self.color = color
       self.started = False
       self.speed = 0
       self.max_speed = 200

   def __str__(self):
       return f"{self.make}, {self.model}, {self.color}: ({self.year})"

   def __repr__(self):
       return (
           f"{type(self).__name__}"
           f'(make="{self.make}", '
           f'model="{self.model}", '
           f"year={self.year}, "
           f'color="{self.color}")'
       )

c = Car("Toyota", "Corolla", 2015, "Red")

# informal representation
# a convenient way to display the object
print(c)

# formal representation
# a string that can be used to recreate the object
# call the constructor with the string
print(repr(c))


exit()




class Circle:
   def __init__(self, radius):
       self._radius = radius

   @property
   def radius(self):
       return self._radius

   @radius.setter
   def radius(self, value): # Polymorphism, same name, different parameters
       if not isinstance(value, (int, float)) or value <= 0:
           raise ValueError("positive number expected")
       self._radius = value

c = Circle(-5)
# setter method is called when we set/assign the value
c.radius = -5
print(c.radius)



exit()



class Circle:
    def __init__(self, radius):
        self._radius = radius
        # to prevent negative radius
        # self.set_radius(radius)

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value


c = Circle(-5)

# don't do this
# c._radius = 5
print(c.get_radius())
print(c.set_radius(-5))


exit()

# Dynamic Typing


class User:
    pass


guest = User()
# add variables to the object at any time
guest.first_name = "Guest 1"
guest.first_name = 1  # Duck Typing, changing the type as we go
print(guest.first_name)

print(guest)
print(guest.__dict__)
