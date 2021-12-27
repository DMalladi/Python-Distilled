single_quote_message = "Hello World!!!"
print(single_quote_message)

Double_quote_message = "Hello World!!!"
print(Double_quote_message)


# triple quote strings are useful when the content of a string literal span
# multiple lines
triple_single_quote_message = """Hello
                                        World!!!"""
print(triple_single_quote_message)

triple_double_quote_message = """
                                    Hello
                                    world
                                        """
print(triple_double_quote_message)


# Format Strings
name = "Python"
print(f"Hello {name}")
print("Hello {0}".format(name))
print("Hello %s" % (name))


# String methods
# To get length of the string
print(len(name))

# Extact a single character from string
print(name[0])  # print 'P' in python

# substring
print(name[:2])  # print 'py' in python
print(name[2:])  # print 'thon' in python
print(name[-1])  # print 'n' in python
print(name[:-3])  # print 'pyt' in python
print(name[-4:])  # print 'thon' in python
print(name[::-1])  # print 'nohtyp' in python

# replace a string
print(name.replace("Python", "Python Programming Language"))

# startswith
print(name)
print(name.startswith("Py"))
print(name.startswith("Py", 0, 5))

# endswith
print(name)
print(name.endswith("on"))
print(name.endswith("on", 0, 5))

# find
print(name.find("on"))
print(name.find("on", 3, 6))

# convert case
# to lower
print(name.lower())

# to upper
print(name.upper())

# to capitalize
print(name.capitalize())

# split
print(name.split("o"))
value = "Hi Hi Hi Hi Hi"
print(value.split(" ", 3))

# strip
extra_white_spaces = "         Hello             "
print(extra_white_spaces)
print(extra_white_spaces.strip())
print(extra_white_spaces.lstrip())
print(extra_white_spaces.rstrip())


# String concatenation
first_name = "Deeraj"
last_name = "Malladi"
print(first_name + " " + last_name)


# type conversion
int_to_string = 1
print(type(str(int_to_string)))

# type conversions
# to string => str()
# to int => int()
# to float => float()


# repr() vs str()
message = "Hello \n world"
print(str(message))
print(repr(message))

# format string, specially decimals
x = 12.35521512
print(format(x, "0.2f"))
