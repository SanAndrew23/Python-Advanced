from functools import wraps
import inspect

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        args_string = [f'{k} = {v}' for k, v in bound.arguments.items()]
        bound.apply_defaults()
        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join(args_string)}) -> {result}')
        return result
    return wrapper

@trace
def summ(a, b):
    return a + b

summ(3, 4)