# if, else, and elif statements are control the conditional execution flow.

def convert_to_int(value: str) -> int:
    """
    converts given value data type to integer
    """
    try:
        return int(value)
    except ValueError as err:
        print("Please provide integer only")
        raise SystemExit("Program Stopped!!!")

value = input("Please enter a number: ")
num = convert_to_int(value)

if num < 0:
    print("Please provide positive value")
elif num > 10:
    print("Please provide integers between 0 and 10")
else:
    print(f"Square of a given number: {num * num}")