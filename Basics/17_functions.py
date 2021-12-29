# use def statement to define a function
# we can annotate the inputs with the types
# e.g. number:int or square() -> int
# annotating the arguments are merely for informational and are not
# actually enforced at runtime, in otherwords, someone could still
# call this function with non-integer values.  
def square(number:int) -> int:
    """
    Computes and returns the square of a given number
    """
    if isinstance(number, int):
        return number * number
    raise ValueError("Please provide integer value")

print(square(4))

# use tuple to return multiple value
def divison_modules(number:int, division_number:int) -> tuple:
    """
    Computes and returns division & remainder of given numbers
    """
    if (isinstance(number, int) and isinstance(division_number, int)):
        division = number // division_number
        modules = number % division_number
        return (division, modules)
    raise ValueError("Please provide integer values")

# unpacking a tuple value into separate variables 
division, modules = divison_modules(10, 3)
print(division, modules)

# To assign a default value to the parameters
# Default values are always used for optional features if there are
# many such arguments, readability will suffer. 
def greeting(username:str=None) -> str:
    """
    Greets the username with the message if username is given,
    otherwise just greets with a message
    """
    if username:
        print(f"Hello {username}")
    else:
        print("Hello amigo")

greeting("Deeraj")

# When default values are given in a function definition, they can be
# omitted when a function is called. An omitted argument will take on
# the supplied default value
greeting() 

# When variables are created or assigned inside a function, their scope is
# local. That is the variable is only accessible inside a function and it
# is destroyed when a function is returns.
# Functions can access variables defined outside a function as long as
# they are defined in a same file

name = "Deeraj" # global variable

def message() -> None:
    """
    Displays a message (is Learning Python3) with a username,
    e.g. Deeraj is Learning Python3
    """
    message = "is Learning Python3!!!" # local variable
    print(f"{name} {message}")

message()