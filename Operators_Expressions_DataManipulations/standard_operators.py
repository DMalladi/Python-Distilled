"""
Python objects can be made to work with the below list of Operators

----------------------------------------------
Operation               Description
-----------------------------------------------
+                       Addition
-                       Subtraction
*                       Multiplication
/                       Division
//                      Truncating Division
@                       Matrix Multiplication
**                      Power
%                       Modulo
<<                      Left Shift
>>                      Right Shift
&                       Bitwise and
|                       Bitwise or
^                       Bitwise xor (exclusive or)
~                       Bitwise negation
-x                      Unary minus
+x                      Unary plus
abs(x)                  Absolute value
divmod(x, y)            Returns (x // y, x % y)
pow(x, y [,modulo])     Returns (x ** y)
round(x, [n])           Rounds to the nearest multiple of 10-n
"""

# "+" Operator is used to concatenate the sequences
concatenate_sequences = [1, 2, 3] + [4, 5] # [1, 2, 3, 4, 5]

# "*" Operator is used to replicate the sequences
replicate_sequences = [1, 2, 3] * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# "%" Operator is used for string formatting
string_formatter = "%s salary is %dk per annum" %("Deeraj", 85)

class CustomMath:
    """
    Provides basic math functions to the client
    e.g. Addition (+)
    """

    def __init__(self, num: int) -> None:
        self.num = num
    
    def __add__(self, other: object) -> object:
        return CustomMath(self.num + other.num)

    def __eq__(self, other: object) -> bool:
        return self.num == other.num

    def __sub__(self, other: object) -> object:
        return CustomMath(self.num - other.num)

    def __mul__(self, other: object) -> object:
        return CustomMath(self.num * other.num)

    def __truediv__(self, other: object) -> object:
      return CustomMath(self.num / other.num)

    def __floordiv__(self, other: object) -> object:
        return CustomMath(self.num // other.num)

    def __mod__(self, other: object) -> object:
        return CustomMath(self.num % other.num)

    def __divmod__(self, other: object) -> object:
        return (self.num / other.num, self.num % other.num)

    def __pow__(self, other: object) -> object:
        return CustomMath(self.num ** other.num)

    def __abs__(self) -> object:
        return CustomMath(abs(self.num))

    def __repr__(self) -> str:
        return str(self.num)



num1 = -5
num2 = 10
cm1 = CustomMath(num=num1)
cm2 = CustomMath(num=num2)
cm3 = abs(cm1)


