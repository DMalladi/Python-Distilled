# To force quit a program use SystemExit() exception
name = 1
if not isinstance(name, str):
    raise SystemExit("Program Exception Stopped \n" 
                      "Something is wrong with the Input")

# If we need to perform a specific clean up activities
# like remove files, close network connections then 
# we can register it with the atexit module as follows:
import atexit

def open_connection(website:str):
    """
    open a connection to connect with the given website
    """
    pass

def close_connection():
    """
    closed open connection
    """
    pass

def cleanup():
    """
    clean up activities
    """
    print("Going away")
    close_connection()


connection = open_connection("google.com")
atexit.register(cleanup)