# inside the class, the methods are defined using def statement
# The first argument (self) is always refers to the object itself, 
# by convenction it is called self.
# __init__ is used to initialize an object
# Python don't have any mechanism to hide or protect the data.
# However there is a programing convenction whereas names preceded by a 
# single underscore are taken to be private.
# dunder methods or double underscore methods works as a built-in features
from typing import Type


class Stack:
    def __init__(self) -> None:
        self._items = []
    
    def push(self, item) -> None:
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __repr__(self) -> str:
        return (f"{type(self).__name__} at Ox{id(self):x} "
                    f"size={len(self._items)}.")
              
# Inheritance => can be useful to add or redefine the capabilities of 
# existing class

class MyStack(Stack):
    def swap(self) -> None:
        current = self.pop()
        previous = self.pop()
        self.push(current)
        self.push(previous)

    def __repr__(self) -> str:
        return str(self._items)

# Inheritance is also used to change the existing class method behavior
class NumericStack(Stack):
    def push(self, item):
        if not isinstance(item, int):
            raise TypeError("Expected int")
        super().push(item) # calls the parent class push method
    
    def __repr__(self) -> str:
        return str(self._items)
        
# Composition 
# Often inheritance is not the best solution to use

# Implementing a Calculator class using inheritance
class Calculator(Stack):
    def add(self):
        """
        Adds last two items in the stack
        """
        current = super().pop()
        previous = super().pop()
        return current + previous

    def multiply(self):
        """
        Multiplies last two items in the stack
        """
        current = super().pop()
        previous = super().pop()
        return current * previous

# Implementing Same Calculator class using Composition Technique
# In this implmentation, Calculator contains stack as a internal implementation
# The main reason for taking this approach is that you don't really think 
# of the calculator as a Stack. It is a separate concept, a different kind of
# object. 
class CalculatorUsingComposition():
    def __init__(self) -> None:
        self._stack = Stack()
    
    def push(self, item):
        self._stack.push(item)
    
    def pop(self):
        return self._stack.pop()

    def add(self):
        current = self.pop()
        previous = self.pop()
        return current + previous

    def multiply(self):
        current = self.pop()
        previous = self.pop()
        return current * previous
    


browser = MyStack()
browser.push("google.com")
browser.push("python.org")
browser.push("python.org/documentation")
print(browser)
browser.swap()
print(browser)

number = NumericStack()
number.push(1)
print(number)

cal = CalculatorUsingComposition()
cal.push(5)
cal.push(10)
cal.push(15)
cal.push(20)
print(cal.add()) # 35
print(cal.multiply()) # 50