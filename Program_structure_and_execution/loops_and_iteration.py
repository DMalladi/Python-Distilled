# Python has only for & while loops
# while statement executes statements untill the associated expression evaluates
# to false
num = 10
while num > 0:
    num -= 1

# To break out of loop, use break
# To continue the loop (skip the next statements), use continue()
# break and continue apply only to the one of the innermost loop being executed.
# If we need to break out of a deeply nester loop structure, use execution

# for statement iterates over all the elements in a object until no more 
# elements are available.
# for statement works with any object that supports iteration
# e.g. lists, tuple, sets, dictionary, strings and any object that implements
# the iterator protocol

# if the elements produced by iteration are iterables of identical size,
# you cn unpack their values into separate iteration variables
ids = [('111A', '111B', '111C'), ('222A', '222B', '222C')]
for idA, idB, idC in ids:
    idA # ('111A')
    idB # ('111B')
    idC # ('111C')

# sometimes to throw away a variable, use '_'
for _, _, idC in ids:
    idC # ('111C')

# if the elements produced by an interable have varying sizes, you can use 
# wildcard unpacking to place multiple values into a variable
ids = [('111A', '111B'), ('222A', '222B', '222C')]
for idA, idB, *extra in ids:
    extra # ['222C']

for *extra, last in ids:
    extra # ['222A', '222B']
    last # ['222C']

for idA, *extra, last in ids:
    extra # ['222B']
    last # ['222C'] 

# To keep track of numerical index when looping a iteration, use enumerate()
for index, id in enumerate(ids):
    index, id # 0 ('111A', '111B') & 1 ('222A', '222B', '222C')

# To start numerical index with a different value, 
# use enumerate(iteration, start=integer)
for index, id in enumerate(ids, start=10):
    index, id # 10 ('111A', '111B') & 11 ('222A', '222B', '222C')

# To iterate two or more iterations in parallel, use zip()
names = ["Deeraj", "Revanth"]
ids = [1, 2]
for name, id in zip(names, ids):
    name, id # Deeraj, 1 & Revanth, 2

# for-else statement
# else statement of a loop executes only if the loop runs to completion. This
# either occurs immediately (if the loop wouldn't execute at all) or after the
# last execution. If the loop is terminated early using the break statement, 
# the else clause is skipped.