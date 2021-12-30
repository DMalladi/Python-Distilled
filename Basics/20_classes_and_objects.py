# All values are used in the Program are Python objects
# A class is a blue print of an object
# An object is an instance of an class, which consists of internal data
# and methods that performs various kinds of operation involving that data

names = ["Deeraj", "Revanth"] # creates a list object
names.append("Deepthi") # call the append() method
print(names)

# Helpful function
available_functions = dir(names) # dir function lists the methods available on an object
print(available_functions)