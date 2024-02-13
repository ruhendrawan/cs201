x = "my string"
print(dir(x))
print(len(x))
print(x.upper())

exit()


class Counter:
    def __init__(self):
        # setting default value -- the only place where we can set the default value
        self.__max_count = 3
        self.__count = 0
        
    # setter
    def increment(self):
        if self.__count < self.__max_count:
            self.__count += 1
    
    # another setter
    def decrement(self):
        self.__count -= 1
    
    # getter
    def get_count(self):
        return self.__count

    # getter without setter
    def get_max_count(self):
        return self.__max_count


tally = Counter()
tally.increment()
tally.increment()
tally.increment()
tally.increment()
tally.increment()

print(tally.get_count())
print(tally.get_max_count())





exit()


class Box:
    # class-level attribute
    # shared by all objects of the class
    size = 10
    # color = 'red'
    # material = 'wood'
    # imagine we have 100 attributes
    
    # constructor will be called when the object is created
    def __init__(self, size, the_serial_number=1234):

        # private attribute
        self.__brand = "Ford"
        self.__serial_number = the_serial_number

        # object attribute
        self.size = size
        self.color = 'red'
        self.material = 'wood'
        # self.change_size(100)
        print('Box is created')

    def change_size(self, new_size):
        self.size = new_size

    def change_brand(self, new_brand):
        self.__brand = new_brand
        

    def get_brand(self):
        return self.__brand




my_box = Box(20)
# object attribute and class attribute has the same name
print(my_box.size)
print(my_box.__class__.size)
print(Box.size)

my_box.change_brand('Toyota')
print(my_box.get_brand())

my_box.serial_number = 5678
print(my_box.serial_number)


exit()



my_other_box = Box(50)
# object attribute and class attribute has the same name
print(my_other_box.size)

print(my_other_box.__class__.size)
print(Box.size)


# self is the object itself
# self is the first parameter
# class is an object 
# dir function returns all the attributes and methods of the object

print(dir(my_box))
my_box.change_size(100)

# short way of getting the attribute
print(my_box.size)
# or calling the method
my_box.change_size(200)

# verbose way of calling the method
# self server as parameter to pass the object to the method that exists in the class
Box.change_size(my_box, 200)
print(my_box.size)

# __init__ is a special method (constructor)
# it is not a function
# can't be called 
#   Box.__init__(third_box, 3000)
third_box = Box(3000)
print(third_box.size)




# # Object oriented way

# # The blueprint of the object
# class Guitar:
#     color = 'white'
#     # is_broken = False

#     # constructor
#     # executed once, when the object is first created
#     def __init__(self):
#         self.object_color = 'white'
#         self.is_broken = False
#         print('Guitar is created')

    
#     def broken(self):
#         self.is_broken = True


# class Car:
#     color = 'black'
#     is_sold = False
    


# # instantiate an object from the class Guitar
# # 1. declaration of the object
# # 2. instantiation of the object -- memory allocation
# # 3. initialization -- setting the initial values
# my_guitar = Guitar()
# print(type(my_guitar))

# print('My guitar color is: ' + my_guitar.color)
# print(my_guitar)
# print(my_guitar.is_broken)

# print(my_guitar.__class__.__name__)
# print(my_guitar.__class__.color)

# print(my_guitar.object_color)

# # my_guitar.is_broken = True
# my_guitar.broken()
# print(my_guitar.is_broken)


# my_second_guitar = Guitar()
# my_second_guitar.color = 'blue'
# print(my_guitar.__class__.color)
# print('My second guitar color is: ' + my_second_guitar.color)
# print(my_second_guitar)


# # object is like a variable
# guitars = []
# guitars.append(Guitar())
# print('Guitar collection size: ' + str(len(guitars)))
# print('Guitar at index 0 color: ' + guitars[0].color)

# my_guitar_collection = {}
# my_guitar_collection["favorite"] = Guitar()
# my_guitar_collection["favorite"].color = 'red'
# my_guitar_collection["favorite"].broken()
# print('My favorite guitar color is: ' + my_guitar_collection["favorite"].color)



# # # procedural way
# # cars_color = ['blue', 'green']
# # cars_is_sold = [False, False]

# # def sell_car(car_index):
# #     cars_is_sold[car_index] = True

# # print('First car color is: ' + cars_color[0])
# # print('First car is sold: ' + str(cars_is_sold[0]))

# # print(cars_color[1])
# # print(cars_is_sold[1])

# # sell_car(0)

# # print('First car color is: ' + cars_color[0])
# # print('First car is sold: ' + str(cars_is_sold[0]))

# # print(cars_color[1])
# # print(cars_is_sold[1])
