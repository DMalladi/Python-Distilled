# raise statement is used to signal an exception
# You need to give the name of an exception
# e.g. raise RuntimeError("Message")
number = "1"
if not isinstance(number, int):
    raise ValueError("Bad Input")