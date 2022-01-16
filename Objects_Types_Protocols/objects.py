## Important Concepts
# Python Built-in-types
## for e.g. numbers (integers, float), strings, lists, dictionary, sets,
## and tuple. In addition to that we can create our own type using classes

# When an object of a particular type is created, it is called as instance of
# that type.

# Objects are characterized by their attribute (value or function (method))

# Object Identity 
## An identity is an integer that connected to the object's location in memory.
# To find an object identity, use id()
numbers = [1, 2, 3, 4]
id(numbers) # e.g. 4301100224

# Object Type
## To find the type (class) of an object, use type()
type(numbers) # <class 'list'>

# Comparision between objects
## 'is' and 'is not' operator
## '==' operator

def compare(obj1:object, obj2:object) -> None:
    if obj1 is obj2:
        print("Same object")
    
    if obj1 == obj2:
        print("Same value")

    if type(obj1) == type(obj2):
        print("Same type")

compare(numbers, numbers) # same object, same value, same type
compare(numbers, [1, 2, 3]) # same value and same type
compare(numbers, [4, 5, 6]) # same type

# To know if an object is a instance of a specific type, use isinstance()
isinstance(numbers, list)
isinstance(numbers, (list, tuple, str, dict))

# Subtype is a type defined by inheritance. It carries all features of the 
# original type plus additional and/or redefined methods.
class CustomList(list):
    def removeLast(self):
        value = self.pop()
        print(f"Deleted last item in the container: {value}")

cl = CustomList([1, 2, 3, 4, 5])
cl.removeLast()

# Garabage collection
## Python manages objects through automatic garbage collections. 
## All objects are referenced counted

# To know the reference count of an object, use sys.getrefcount()
## sys.getrefcount() will always be much higher then one might expect
import sys
sys.getrefcount(numbers)

# References
numbers = [1, 2, 3]
new_numbers = numbers # new_numbers is a reference to numbers
new_numbers is numbers # True

# numbers and new_numbers refer to the same object, a change made to new_number
# also reflected on the other. To avoid this, we need to create a copy of an 
# object instead of a reference
new_numbers.append(4) # numbers -> [1, 2, 3, 4], notice how a also changed

# Two types of copies we can have when copies an object to another
## Shallow copy -> creates a new object, but populates it with references to the
## items contained in the original object.
names = ["Deeraj", ["Revanth", "Deepthi"]]
new_names = list(names)
new_names[1].append("Sahasra") 
print(names) # ['Deeraj', ['Revanth', 'Deepthi', 'Sahasra']]

## Deep copy -> creates a new object and recursively copies all the object it 
# contains.
# From copy lib, use copy for Shallow copy and deepcopy for Deep copy functions
from copy import copy, deepcopy
dc_names = deepcopy(names)
dc_names[1].append("Renduchintalas")
print(names) # ['Deeraj', ['Revanth', 'Deepthi', 'Sahasra']]

# In Python all objects are said to be First-Class objects
# This means that all objects that can be assigned to a name can be treated as a
# data, e.g.
items = {
    "number" : 42,
    "text" : "Hello World" 
}

# First-class nature of objects can be seen by adding some unusual
# items to this dictionary

items["abs"] = abs
import math
items["math"] = math
items["error"] = ValueError
nums = [1, 2, 3, 4]
items['append'] = nums.append

print(items["abs"](-50)) # 50
print(items["math"].sqrt(4)) # 16

# Use None for optional or missing data
# Comman ways to test the None is to use "is" Operator,
# e.g. if value is None: 
# Testing None using the "==" operator will also works, but not recommended
# and might be flagged as a style error by code-checking tools
