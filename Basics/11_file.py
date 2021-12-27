"""
    Open() function returns a new file object.
    The with statement that precedes it declares a block of statement 
    (or context) where the file (file) is going to be user. 
    Once control leaves this block, the file is automatically closed. If you 
    don't use the with statement, the file object should close using 
    file.close();
"""

# with statement uses context where file will be automatically closed after
# the control leaves
with open("1_hello_world.py") as file:
    for line in file:
        print(line, end="")  # end="" omits the extra newline

# Manually closing file object
file = open("1_hello_world.py")
for line in file:
    print(line, end="")
file.close()


# It is always bette to use with statement

# for loop reads the file line by line, if we want to read the entire file
# as a string use read()
with open("1_hello_world.py") as file:
    data = file.read()
print(data, end="")

# if we want to read a large file in chunks, give a size hint to the read()
# method as follows:
# := operator assigns to a variable with the value
with open("1_hello_world.py") as file:
    while chunk := file.read(10000):
        print(chunk, end="")


# write to a file
message = "print('hello world')"
with open("log.py", "wt") as file:
    file.write(message)


# Read console input
name = input("Enter your name: ")
print(f"Hello {name}")
