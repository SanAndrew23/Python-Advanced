from functools import wraps


def once(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            wrapper.result = func(*args, **kwargs)
        return wrapper.result
    wrapper.called = False
    wrapper.result = None
    return wrapper

@once
def summarise(a):
    print('called')
    return a + 1

print(summarise(1))
print(summarise(1))
print(summarise(1))
print(summarise(1))
print(summarise(1))