# Python provides the "in-place" or "agumented" assignment operators
"""
---------------------------------
Operation       Description
---------------------------------
x += y          x = x + y
x -= y          x = x - y
x *= y          x = x * y
x /= y          x = x / y
x //=y          x = x // y
x **=y          x = x ** y
x %= y          x = x % y
x @= y          x = x @ y
x &= y          x = x & y
x |= y          x = x | y
x ^= y          x = x ^ y
x >>= y         x = x >> y
x <<= y         x = x << y
"""

# Mutable objects use these operators to perform an in-place mutation
# of the data as an optimization
numbers = [1, 2, 3, 4, 5]
numbers2 = numbers

# numbers & numbers2 refer to the same object (list) in the memory
# When numbers += [6, 7, 8] is performed, it updates the list object
# in place without creating a new list.
numbers += [6, 7, 8] # now numbers2 & numbers will be [1, 2, 3, 4, 5, 6, 7, 8]

