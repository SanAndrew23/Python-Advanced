def once(func):
    def wrapper(a):
        b = func(a)
        func(a)
    return wrapper

@once
def summarise(a):
    return a + 1

print(summarise(1))