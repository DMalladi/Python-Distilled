# stings, list and tuples are considered as sequence AKA iterable container.
# Iterable container has a size and allows items to be accessed by an integer
# index starting at 0.

"""
Operations on Sequences
-----------------------------------
Operation       Description
-----------------------------------
s + r           Concatenation
s * n, n * s    Makes n copies of s, where n is an integer
s[i]            Indexing
s[i:j]          Slicing
s[i:j:stride]   Extended slicing
len(s)          Length
"""

# list
s1 = [1, 2, 3, 4]
s2 = [5, 6]
s3 = s1 + s2 # [1, 2, 3, 4, 5, 6]
s4 = 2 * s2 # [5, 6, 5, 6]
s5 = s1[0] # 1
s6 = s1[1:3] # [2, 3]
s7 = s1[:2] # [1, 2]
s8 = s1[::-1] # [4, 3, 2, 1]
s9 = s1[::2] # [1, 3]

print(s5)
print(s6)
print(s7)
print(s8)
print(s9)
print(s4)

 
# string
first_name = "Deeraj"
last_name = "Malladi"
full_name = first_name + " " + last_name # "Deeraj Malladi"
repeat_first_name = 2 * first_name # "DeerajDeeraj"

# tuple
t1 = (1, 2, 3, 4)
t2 = (5, 6)
t3 = t1 + t2
t4 = 2 * t2 # (5, 6, 5, 6)
