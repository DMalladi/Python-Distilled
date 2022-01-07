"""
A mapping is an association between keys and values
---------------------------------------------------
Operation       Description
---------------------------------------------------
x = m[k]        indexing by key
m[k] = x        Assignment by key
del m[k]        Deletes an item by key
k in m          Membership testing
len(m)          Number of items in the mapping
m.keys()        Returns the keys
m.values()      Returns the values
m.items()       Returns keys & value pairs
"""

# Key values can be any immutable object, such as string, numbers, and tuples
# When using tuples as keys, you can omit the parenthesis 

d = { }
d[1, 2, 3] = "foo" # {(1, 2, 3): 'foo'}