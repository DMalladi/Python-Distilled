# Generators
## The primary use of generators is to produce values for use in iteration.
## The generator object executes when you start iterating on it
## If a function uses "yield" keyword, it defines an object known as generator.
## next() or __next__() is used to execute generator statement until it reaches
## yeild statement. The yeild statement returns the result and at this point
## the function execution is suspended until next() or __next__() is invoked
## again
from tracemalloc import start


def countdown(max_count):
    count = 0
    while count < max_count:
        yield count 
        count += 1
 
cd = countdown(10)
# cd.__next__() or next(c) 
for c in cd:
    print(c)

## Generator function can use both yeild and return 
def two_numbers():
    yield 0
    return 1

# Restartable Generators
## Normally generators are executed only once, not in 3.9.5
## If your using python < 3.9.5, then use classes for a repeated iterations.
class Countdown:
    def __init__(self, start:int) -> None:
        self.start = start
    
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

cd = Countdown(10)

# A function that is using "yield" statement always depended on the some other
# code to execute, explicity a for loop or next() statement.
