# For loop iterates over a collection of items
# e.g. strings, lists, dictionaries, files or tuple

for number in [1, 2, 3, 4, 5]:
    print(number, end=" ,")
print()

# shortcut version
for number in range(1, 6):
    print(number, end=" ,")
print()

# range(i, j, [,step]) function creates an object that represents a 
# range of integers with values from i up to j-1 (otherwords, not 
# including j)

for even_number in range(0, 10, 2):
    print(even_number, end=" ,")
print()

for reverse_number in range(10, 0, -1):
    print(reverse_number, end=" ,")
print()

# looping over string
message = "Hello World"
for character in message:
    print(character)

# looping over list
names = ["Deeraj", "Deepthi", "Revanth", "Shasra"]
for name in names:
    print(name)

# looping over dictionaries
shares = {
    "Appl": 35.05,
    "Goog": 25.10,
    "IBM": 10.01
}
for share in shares:
    print(f"Share: {share}") # prints dictionary keys

for share_value in shares.values():
    print(f"share value: {share_value}") # prints dictionary values

for share, value in shares.items():
    print(f"Share: {share}, Value: {value}") # prints both dict key & value

# looping tuples
weekdays = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)
for day in weekdays:
    print(f"Day => {day}")

# looping file
with open("1_hello_world.py") as file:
    for line in file:
        print(line, end="")
