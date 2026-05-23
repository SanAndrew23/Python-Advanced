def trace(func):
    def wrapper(*args):
        print(func.__name__)
        print(args)
        result = func(*args)
        return result
    return wrapper

@trace
def summ(a, b):
    return a + b

print(summ(3, 4))