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
