# import mod
from mod import *

# import arithmetic
# import arithmetic as a
# from arithmetic import add
# from arithmetic import add as a_add
from utils import arithmetic

from math import pi
# from math import pi as PI

# print(PI)
print(pi)

# when importing a module, 
# --> utils.arithmetic
print(arithmetic.__name__)




print("importing mod ----")
# print(_v) # Error
print(s)
# print(mod.s)
# print(mod.a)
# print(mod.foo('test'))
# print(mod.Foo())

def add(a, b):
    return "nothing"

print("importing arithmetic ----")
# result = arithmetic.add(5, 3)
# result = a.add(5, 3)
# result = add(5, 3)
# print(result)
# result = a_add(5, 3)
# print(result)


result = arithmetic.add(5, 3)
print(result)
