"""
Equality operator tests the values of x & y for equality and return True if,
for List, Tuples
    -> size (# of items) must be equal 
    -> have equal elements (same value)
    -> be in the same order
for dictionaries
    -> two dictionaries should have same set of keys
    -> two dictionaries with same key should have same value 
    -> two dictionaries should have same elements
"""

# Equality comparision between objects of incompatible types, such as
# file and floatin-point integer will not throw an error, instead returns False.

# Sometimes comparision between two different objects will return True.
# e.g. 2 : int == 2.0 : float -> True

class CustomInt(int):
    """
    CustomInt class inherits from the int class
    It holds all the functionality what int provides to the client,
    however, the equality operation is modified, in this version
    we also checks if the data type of the other object is also integer.
    e.g. 2 == 2.0 -> False
    e.g. 2 == 2 -> True
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, __other: object) -> bool:
        if isinstance(__other, int) and self.value == __other:
            return True
        return False


integer = CustomInt(2)
floating_point = 2
print(integer == floating_point)

# Identity Operator "is" is also used to check the equality of the objects,
# however is operator also check whether both objects refer to the same memory
# location

obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
# False, because the memory location of the objects is different
print(obj1 is obj2) 

print(obj1 == obj2) # True

"""
Key Note:
    Never use "is" Operator to check the equality of the objects, unless if you
expect to check the two objects to have the same identity (refer to same object
in memory)
"""

# Use id function to know the object memory location
obj1_memory_location = id(obj1) # e.g. 4334241344
obj2_memory_location = id(obj2) # e.g. 4334556288

print(f"Obj1 memory location {obj1_memory_location}")
print(f"Obj2 memory location {obj2_memory_location}")