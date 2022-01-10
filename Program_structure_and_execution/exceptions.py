# Exceptions can raised using raise statement
# e.g raise ValueError("Invalid input")
# use try-except to catch an exception
try:
    file = open("no-file.txt", 'rt')
except FileNotFoundError as err:
    err # [Errno 2] No such file or directory: 'no-file.txt'

# Exceptions have a few standard attributes that might be useful in code that
# needs to perform further actions in response to an error
# err.args 
# err.__cause__
# err.__context__
# err.__traceback__

# err.args -> tuple of arguments supplied when raising an exception, in most
# cases it is one-item tuple with a string describing the error.
# For OSError exceptions, that value is a 2-tuple or 3-tuple containing an 
# integer error number, string error message, and an optional filename.
try:
    file = open("no-file.txt", 'rt')
except FileNotFoundError as err:
    err.args # (2, 'No such file or directory')

# err.__cause__ -> __cause__ attribute of the resulting exception will contain
# the other exception
## Chained Exceptions
# A chained exception is considered as raising another exception as a response
# to the exception
class ApplicationError(Exception):
    pass

def convert_to_int(value:str) -> int:
    return int(value)

def calculations():
    value = input("Enter a number: ")
    try:
        convert_to_int(value)
    except Exception as err:
        raise ApplicationError("Bad value")
    # except ApplicationError as err:
        # err.__cause__ # prints Exception class 
    # except Exception as err: 
        # use None to not to include other exceptions
        # raise ApplicationError("Failed") from None # print only Application Err

# calculations()

# err.__context__ -> If an unexpected expection is raised while handling 
# another exception, the __context__ attribute holds information about the
# exception that was being handled when the error occured.
def calculations2():
    value = input("Enter a number: ")
    try:
        convert_to_int(value)
    except Exception as err:
        # print("Bad value", e) # NameError e is not defined
        if err.__context__:
            print(err.__context__)

# calculations2()

# err.__traceback__

# multiple exceptions
value = 1
try:
    int(value)
except TypeError as err:
    err
except ValueError as err:
    "Invalid Value", err.args
except Exception as err:
    err

# single handler clause can catch multiple exception types like this:
try:
    int(value)
except (TypeError, ValueError) as err:
    err

# To silently ignore the error, use pass statement
try:
    int(value)
except Exception as err:
    pass

# Silently ignoring errors is often dangerous and hard-to-find mistakes
# If you don't include any infformation about the exception value, it can make
# it difficult to debug code that is failin for reason you don't except

# try-except-else, else statement only executes if code in the try block 
# executes without raising an exception
try:
    file = open('no-file.txt', 'rt')
except FileNotFoundError as err:
    err
else:
    # file.close()
    pass

# try-except-else-finally, finally statement executes regardless of what happens
# in a try-except block
try:
    file = open("no-file.txt", "rt")
except FileNotFoundError as err:
    err
finally:
    # file.close()
    pass

# Exception Hierarchy
# In Python there are more than 60 built-in exceptions are there.
# Exceptions are organized into a hierarchy via inheritance. Instead of 
# targeting specific errors, it might be easier to fcus on more general 
# categories of errors.
# e.g. IndexError and KeyError are inherited from the Lookup Error
items = [1, 2, 3, 4]
try:
    items[6]
except LookupError as err: # instead of KeyError and IndexError
    err

"""
Common Categories of Built-In Exceptions
--------------------------------------------------------------------------------
Exception Class                     Description
--------------------------------------------------------------------------------
Base Exception          The root class for all exceptions
Exception               Base class for all program-related errors
ArithmeticError         Base class for al math-related errors
ImportError             Base class for all import-related errors
LookupError             Base class for all container lookup errors
OSError                 Base class for all system-related errors. 
                        IOErrors and EnvironmentError are aliases
ValueError              Base class for value-related errors, including Unicode
UnicodeError            Base class for a Unicode string encoding-related errors

Common built-in-exceptions that inherit directly from Exception but aren't part
of a larger exception group

--------------------------------------------------------------------------------
AssertionError          Failed assert statement
AttributeError          Bad attribute lookup on an object
EOFError                End of file
MemoryError             Recoverable out-of-memory error
NameError               Name not found in the local or global namespace
NotImplementedError     Unimplemented Feature
RuntimeError            A generic "something bad happened" error
TypeError               Operation applied to an object of the wrong type
UnboundedLocalError     Usage of a local variable before value is assigned

Exceptions that inherit from the Base Exceptions
--------------------------------------------------------------------------------
SystemExit              Raised to indicate program exit
KeyboardInterrupt       Raised when a program is interrupted via Control-C
StopIteration           Raised to signal the end of iteration
"""

# Defining custom exception
# All built-in exceptions are defined in terms of classes. To create a new 
# exception, create a new class definition that inherits from Exception.
class NetworkError(Exception):
    pass

# raise NetworkError 

# When raising an exception, the optional values supplied with the raise 
# statement are used as the arguments to the exception's class constructor.
class DeviceError(Exception):
    def __init__(self, error_number, error_message) -> None:
        self.args = (error_number, error_message)
        self.error_number = error_number
        self.error_message = error_message

# raise DeviceError("123", "Device Not Found")

# Exceptions can be organized into hierarchy using inheritance
class HostNameNotFound(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

# Exceptions have an associated stack traceback that provides information
# about where an error occured.
# The traceback is stored in the __traceback__ attribute of an exception.

import traceback

try:
    calculations()
except Exception as e:
    tblines = traceback.format_exception(type(e), e, e.__traceback__)
    tbmsg = ''.join(tblines)
    print('It failed: ')
    print(tbmsg)