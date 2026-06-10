def once(func):
    def wrapper(a):
        b = func(a)
        wrapper.count += 1
        if wrapper.count <= 1:
            return func(a)
        else:
            return b
    wrapper.count = 0
    return wrapper

@once
def summarise(a):
    return a + 1

print(summarise(1))
print(summarise(1))
print(summarise(1))
print(summarise(1))
print(summarise(1))