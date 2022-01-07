"""
A set is a unordered collections of unique vlaues
-------------------------------------------------
Operations                  Description
-------------------------------------------------
s | t                       Union of s and t
s & t                       Intersection of s and t
s - t                       Set difference (items in s, not in t)
s ^ t                       Symmetric difference (items not in both s or t)
len(s)                      Number of items in the set
item in s, item not in s    Membership test
s.add(item)                 Add an item to set s
s.remove(item)              Remove an items from s if it exists (otherwise an error)
s.discard(item)             Discard an item from s if it exists
"""

s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}

s1 | s2 # {'b', 'c', 'a', 'd'}
s1 & s2 # {'c'}
s1 - s2 # {'a', 'b'}
s1 ^ s2 # {'a', 'd', 'b'}
len(s1) # 3
'a' in s1 # True
s1.add('d') 
s1.remove('a')
s1.discard('e')