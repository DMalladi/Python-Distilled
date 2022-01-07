# A genertor expression is an object that carries out the same computation as
# a list comprehension but produces the result iteratively.
import sys

nums = list(range(100000000)) 
nums_generator = (num for num in nums) 

# To get the memory size of the object use sys.getsizeof()
sys.getsizeof(nums) # 800000056
sys.getsizeof(nums_generator) # 112

# generator object cannot be indexed to access an element in the object
# to convert a generator object to list use list()
nums_list = list(nums_generator)
sys.getsizeof(nums_list) # 835128600