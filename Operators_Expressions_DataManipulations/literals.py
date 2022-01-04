# A literal is a value typed directly into a program
# e.g. 100, 25.50, "Texas"
# Integer literals represent a signed integer value of arbitary size.
rank = 1 # Integer literal
amount = 10.05 # Float literal
binary_integer = 0b101010 # Binary Integer -> 42
octal_integer = 0o52 # Octal Integer -> 42
hexadecimal_integer = 0x2a # Hexadecimal Integer -> 42
state = "Texas" # String literal
isValid = True # Boolean literal (either True or False)
ranks = (1, 2, 3) # Tuple literal
ranks = [1, 2, 3] # List literal
ranks = {1, 2, 3} # set literal
# dictionary literal
ranks = {
    "first": 1,
    "second": 2,
    "third": 3
} 

# Built in functions to convert the integer to string of different bases
# bin(value) to binary integer
# oct(value) to octal integer
# hex(value) to hexadecimal integer
binary_rank = bin(rank) # converts integer 1 to binary integer (Ob1)
octal_rank = oct(rank) # converts integer 1 to octal integer (0o1)
hexadecimal_rank = hex(rank) # converst integer 1 to hexadecimal integer (0x1)

# Floating point numbers can be written by adding a decimal point or using
# scientific notation, e.g. 1.0e+2
amount_scientific_notation = .105e+2 # 10.05

# Internally floating-point number are stored as IEEE 754 double-precision 
# (64-bit) 
# max size of float 1.7976931348623157e+308
# min size of float 2.2250738585072014e-308

# max size of int 9223372036854775807
# To get more details use sys module
import sys
float_info = sys.float_info
float_max = float_info.max # max value of float data type

int_max = sys.maxsize # max value of int data type that 

# Numeric literal, a single underscore (_) can be used as a visual separator 
# between digits, e.g. 105_000 instead of 105000
# digit separator is not stored as part of a number it's only used to make 
# large numeric literals easier to read
million_dollars = 1_000_000 

# String literals can be written using single, double, and triple quotes
message = 'Hello world!!!'
message = "Hello World!!!"
message = """Hello
                World"""
