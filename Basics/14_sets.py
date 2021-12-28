# A set is a unordered collection of unique objects and cannot
# be indexed by numbers
# Sets are used to find distinct values (otherwords no duplicate 
# values), e.g. managing membership
# Elements of sets are restricted to the immutable objects

# To create a set
method_1 = {
    "Deeraj",
    "Revanth"
}

method_2= set([
    "Deeraj",
    "Malladi"
])

# Set comprehension
numbers = { number for number in range(1, 10) }

# To create a empty set
empty_set = set()

# Sets support a standard collection of operations including 
# unions, intersection, difference, and symmetric difference
ps4_games = {
    "God Of War 4",
    "Last of US 2",
    "Uncharted 4",
    "Spyderman"
}

ps5_games = {
    "Death Souls",
    "Spyderman"
}

# Union 
# {'God Of War 4', 'Last of US 2', 'Death Souls', 'Uncharted 4', 'Spyderman'}
print(ps4_games | ps5_games)

# Intersection
# {'Spyderman'}
print(ps4_games & ps5_games)

# Difference
print(ps4_games - ps5_games) # {'God Of War 4', 'Last of US 2', 'Uncharted 4'}
print(ps5_games - ps4_games) # {'Death Souls'}

# Symmetric Difference
print(ps4_games ^ ps5_games) # {'God Of War 4', 'Death Souls', 'Last of US 2', 'Uncharted 4'}

# To add an item
ps4_games.add("Sekiro")
print(ps4_games)

# To Update an Item => Adds multiple items to the set
updated_set = {
    "Blood Borne",
    "God of War 3"
}
ps4_games.update(updated_set)

# To Remove an Item 
ps4_games.remove("God of War 3") 

# To Discard an Item
ps4_games.discard("Death Souls")

# Differences between remove & discard is that discard doesn't 
# raise an exception if the item isn't present


