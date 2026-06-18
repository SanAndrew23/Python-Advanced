from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@count_calls
def greet(name):
    return f'Привет, {name}!'

print(greet('Boris'))
print(greet('Anna'))
print(greet.count)