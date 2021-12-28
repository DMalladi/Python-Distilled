# To create a simple data structure, you can
# pack a collection of values into an immutable 
# object known as tuple

python_web_address = ("https://www.python.org", 8080)

# Empty tuple
empty_tuple = ()

# single item tuple
single_item_tuple = ("one", ) # note the trailing comma

# The values in the tuple can be extracted by numerical
# index just like a list
python_web_address[1] # 8080

# Unpack tuple into set of variables
web_address, http_port = python_web_address

# tuples support most of the same operations as lists
# (such as indexing, slicing, and concatenation)
# the elements of tuples cannot be changes after creation

# Iterate over items in the tuples
weekdays = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)

for weekday in weekdays:
    print("Day: {0} ".format(weekday))

# Alternative version of Iterating/looping
print("""
Alternative way to iterate items in the tuple using
List comprehension
""")
[print(f"Day: {weekday}") for weekday in weekdays]


