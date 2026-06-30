def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Аргументы должны быть положительными, получено: {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def sqrt(x):
    return x ** 0.5

print(sqrt(9))    # 3.0
print(sqrt(-4))   # ValueError: Аргументы должны быть положительными, получено: -4
