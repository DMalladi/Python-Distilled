"""
Unlike a compiler for a static language, Python does not verify correct program
behavior in advance. Instead, the behavior of an object is determined by a 
dynamic process that involves the dispatch of so-called "special" or "magic"
methods.

Methods are automatically triggered by the intepreter as a program executes.
e.g. operation x * y is carried out by a method x.__mul__(y).

The names of these methods and their corresponding operators are hard-wired.
"""

class CustomMath:
    """
    Custom Math class provides basic math functionality
    """
    def __init__(self, num):
        self.num = num
    
    def __repr__(self):
        return "Value -> {self.num}."
    
    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num
    
    def __abs__(self):
        return abs(self.num)

    def __eq__(self, other):
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num
    
    def __lt__(self, other):
        return self.num < other.num

    def __le__(self, other):
        return self.num <= other.num

    def __gt__(self, other):
        return self.num > other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __hash__(self):
        return NotImplemented

    
class Container:
    def __init__(self):
        self.items = {}
    
    def _get_key(self, key):
        return self.items[key]

    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, key):
        value = self._get_key(key)
        return value if value else "Key Not Found!"

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del(self.items[key])

    def __contains__(self, key):
        value = self._get_key(key)
        return True if value else False

c = Container()
c["name"] = "Deeraj"
print(len(c))