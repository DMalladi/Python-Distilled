# Lists
## Lists are an ordered collections of arbitrary objects

names = [
    "Deeraj",
    "Deepthi",
    "Revanth",
    "Sahasra"
]

# List are indexed by integer, starting from zero
print(names[0]) # prints Deeraj
print(names[-1]) # prints Sahasra

# To append an item to the list, use append() method
names.append("Prasanth") # adds Prasanth to the names list
names.append("Vani") # adds Vani to the names list

# To pop or remove last item in the list, use pop() method
names.pop() # removes last item in the list

# To insert an item at a specific position, use insert() method
names.insert(0, "Sahasra") # inserts Sahasra at index 0

# To remove an first occurence of an item with a specific value, 
# use remove() method
names.remove("John")

# Iterating over items in the list
for name in names:
    print(name) # prints each item in the list

# To extract or reassign a portion of an item in the list,
# use slicing operator
print(names[1:3]) # prints names[1] till names[3] but not names[3]

# To concatenate two or more lists, use + operator
new_names = [
    "Murthy",
    "Meena"
]

full_family_names = names + new_names
print(full_family_names) # prints names & new_names together

# To create an empty list use either [] or list()
# Specifying [] for an empty list is more idiomatic
empty_list = []
another_empty_list = list()

letters = list("Dave") # letters = ["D", "a", "v", "e"]

# List can hold different types of data objects 
# e.g. ["str", 1, 10.5, ["names"], {}]

# Use multiple indexing to access an item that is contained in
# the nested list 
a = [[0, 1], [0, 2], [0, 3]]
print(a[0][1]) # prints 1