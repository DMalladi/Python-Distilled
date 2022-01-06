"""
Operations on Iterables
---------------------------------------------------------------------
Operation                              Description
---------------------------------------------------------------------
for variables in sequence:             Iteration
v1, v2, ... = sequence                 Variable unpacking
x in sequence, x not in seq            Membership 
[a, *seq, b], (a, *seq, b), {a, *s, b} Expansion in list, tuple or set literals
"""

# For strings, "in" & "not in" operator accepts substring
# e.g. "hello" in "hello world" produces True

# Any object that supports iteration can have its values unpacked into variables
# e.g. x, y, z = [1, 2, 3] or x, y, z = "abc"
# list
items = [1, 2, 3]
x, y, z = items # x = 1, y = 2, z = 3

# string
letters = "abc"
x, y, z = letters # x = a, y = b, z = c

# tuple
student_ids = ("1A", "1B", "1C")
id1, id2, id3 = student_ids # id1 = 1A, id2 = 1B, id3 = 1C

# dictionary
# {'x': 1, 'y': 2, 'z': 3}
dictionary_items = { }
dictionary_items["x"], dictionary_items["y"], dictionary_items["z"] = items

# tuple
datetime = (("01", "05", "2022"), (9, 30, "pm"))
(month, date, year) = datetime[0]
(hour, minute, am_pm) = datetime[1] 
(month, date, year), (hour, minute, am_pm) = datetime

# "_" variable is used to indicate a throw-away value
(_, day, _) = datetime[0]

# "*" variable is used to unpack number of items
# in the following examples, *extra receives all the extra elements
first, *extra = items # first = 1, extra = [2, 3]
*extra, last = items # extra = [1, 2], last = 3

items += [4, 5]
first, *extra, last = items # first = 1, extra = [2, 3, 4], last = 5

# Any iterable can be expanded with "*" variable
l = [0, *items, 6] # [0, 1, 2, 3, 4, 5, 6] -> list
t = (0, *items, 6) # (0, 1, 2, 3, 4, 5, 6) -> tuple
s = {0, *items, 6} # {0, 1, 2, 3, 4, 5, 6} -> set


# Build-In functions that accept any iterables (list, tuple, set) as input
items_copy = list(items) # [0, 1, 2, 3, 4, 5, 6]
tuple_copy = tuple(t) # (0, 1, 2, 3, 4, 5, 6)
set_copy = set(s) # {0, 1, 2, 3, 4, 5, 6}

# min(iterable) returns the minimum value in the list
least_value_in_items = min(items) # 1

# max(iterable) returns the maximum value
highest_value_in_items = max(items) # 5

# any(iterable) return True if any item in the iterable is True
any([]) # returns False
any(items) # retruns True

# all(iterable) returns True if only all items in the iterable is True
all(items) # return True
all([True, True, False]) # return False

# sum(iterable) sum of items in the iterable
sum(items) # 15

# sorted(iterable) Created a sorted list
unsorted_numbers = [100, 9, 103, 1, 3, -1, 0]
sorted_numbers = sorted(unsorted_numbers) # [-1, 0, 1, 3, 9, 100, 103]