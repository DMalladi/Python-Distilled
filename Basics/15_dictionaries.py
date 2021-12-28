# A dictionary is a mapping between keys and values.
# A dictionary is useful to define an object that contains
# named fields
# A dictionary is also used for performing a fast lookups on 
# unordered data
# Different types of Python objects can be used as dictionary keys
# such as strings, numbers, and tuples but not mutuable objects
# like lists, sets and dictionaries
# Dictionary keys appear in the order how they were initally inserted

# To create a dictionary
webpage_details = {
    "protocal": "https",
    "domain": "google.com",
    "query_string": "q",
    "path": "/images"
}

# To access members in a dictionary
print(webpage_details["domain"]) # google.com

# To insert a member in a dictionary
webpage_details["host"] = "www.google.com"

# To modify a member in a dictionary
webpage_details["domain"] = "www.google.com"

# To lookup an item in a dictionary
print(webpage_details["query_string"]) # throws an exception if member not exists
print(webpage_details.get("query_string")) # doesn't throw an exception if member not exists
print(webpage_details.get("sub_domain", "Sub Domain Field Not Exists"))

# To delete an item
del webpage_details["domain"]

# Use 'in' operator to test if a member exists 
print("sub_domain" in webpage_details)

# To create empty dictionary
empty_dictionary = {} # it is more idiomatic to use {} for empty dict
empty_dictioary_2 = dict()

# dict() is commonly used to create a dictionary from key-value pairs
shares = [("APPL", 50), ("PHP", 100), ("IBM", 78)]
shares_dict = dict(shares) # {'APPL': 50, 'PHP': 100, 'IBM': 78}

# To obtain a list of dictionary keys use list() or dict.keys()
webpage_details_keys_1 = list(webpage_details) # ['protocal', 'query_string', 'path', 'host']
webpage_details_keys_2 = webpage_details.keys()

# The difference between dict.keys() & list(dict) is, keys() returns a 
# special "keys view" that is attached to the dictionary and actively 
# reflect changes made to the dictionary. 

# To obtain the values stored in a dictionary, use dict.values()
print(webpage_details.values())

# To obtain the key-values stored in a dictionary, use dict.items()
print(webpage_details.items())