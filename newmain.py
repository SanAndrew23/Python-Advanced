from functools import reduce
import itertools

numbers = [0, 1, 2, 11, 123, 1, 5]
total = reduce(lambda a, b: a if a > b else b, numbers)
print(total)

c = itertools.repeat([1, 2, 3])
for i in range(3):
    print(next(c))