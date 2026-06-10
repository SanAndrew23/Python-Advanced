from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_string = [f'{k} = {str(v)}' for k, v in kwargs.items()]
        print(f'{func.__name__}({", ".join(args_string)}) = {result}')
    return wrapper

@trace
def summ(a, b):
    return a + b

print(summ(3, 4))