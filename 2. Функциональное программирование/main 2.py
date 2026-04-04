def f():
    yield 1
    yield 2

obj = f()
print(next(obj))
print(next(obj))
