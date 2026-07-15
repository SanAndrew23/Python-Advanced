from functools import wraps


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            lst = []
            for i in range(n):
                lst.append(func(*args, **kwargs))
            return lst
        return wrapper
    return decorator


@repeat(3)
def roll_dice():
    import random
    return random.randint(1, 6)

print(roll_dice())