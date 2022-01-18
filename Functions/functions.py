# Default Arguments
def split(line, delimiter = ","):
    return line.split(delimiter)

# Default parameter values are evaluated when frist function is defined not
# when function is called. This often lead to surprising behavior if mutuable
# objects are used as default
def names(name, items=[]):
    items.append(name)
    return items

# To avoid this surprising behavior, use "None" keyword
def names(name, items=None):
    items = []
    items.append(name)
    return items

# Variadic Arguments
## A function can accepts number of arguments as a single parameter (variable)
## when it is pre-fixed with "*"
def total(initial_amount, *other_amounts):
    result = initial_amount
    for amount in other_amounts:
        result += amount
    return result

initial_amount = 100
total(initial_amount, 10, 20, 30, 40, 50)
# In this case, all other arguments (10, 20, 30, 40, 50) are placed into 
# other_amounts as a tuple. Later, by using any sequence operations like 
# iteration, silicing, unpacking and so on can perform.

## Keyword Argument
def print_message(message):
    print(message)

message = "Hello Python3"
print_message(message=message) # If possible, use keyword arguments.

# Variadic Keyword Arguments
# When a function receives a last argument that is pre-fixed with "**" then a 
# dictionary of key-value arguments are placed into function.
def user_details(name, age, **address):
    address.pop()
    return address

# A function will accepts all kinds of inputs when arguments are passed with
# "*" and "**". 
# Positional arguments are passed as tuple
# Keyword argument are passed as dictionary
def accept_all_kinds_arguments(*postional, **keyword):
    pass

# Naming convenction
# Use lowercase letter with an "_" as a word separator 
# For internal use only function, prepend the function name with underscore "_"
# e.g. _helper()

# Documentation Strings
def print_time():
    """
    Prints time on the console
    """
    pass

# Lambda Function
## An anonymous - unnamed functions can defined using lambda functions
## One of the main uses of lambda is to define a small callback functions
## syntax lamda args : expression
print_message = lambda message : print(message)
print_message("Hello")

# Higher Order Function
## A function can be passed as an argument to another function or
## A function can be used in the datastructure or
## A function can be returned as a result
### Functions are said to be first-class objects because there is no difference
### between how you treat data and function
from time import sleep

def delay_func_call(delay_time, func):
    sleep(delay_time)
    func()

def greeting(message):
    print(message)

## using lambda
# delay_func_call(5, lambda : greeting("Hello Deeraj!!!"))

## using partial
from functools import partial
# delay_func_call(5, partial(greeting, "Hello World!!!"))

# Decorators
## A function that wraps around another function
## The purpose of this wrapping is to alter or enhance the behavior the object
## (function) being wrapped.
## When writing a decorator, it's considered to be a best practise to use 
## @wraps() decorator

from functools import wraps

def print_log(func):
    @wraps(func)
    def call():
        print("Logging!!!, for ", func.__name__)
        return func()
    return call
    
@print_log
def hello_world() -> None:
    """
    Prints Hello World
    """
    print("Hello world!!!")

@print_log
def hello_python() -> None:
    """
    Prints Hello Python
    """
    print("Hello Python")


# Async and await Function
import asyncio

async def timer(timer):
    sleep(timer)
    print("Timer completed")
    return ""

async def delay_message(delay_time, message):
    await timer(delay_time)
    print(message)

asyncio.run(delay_message(5, "Hello!!!"))
print("World!!!")