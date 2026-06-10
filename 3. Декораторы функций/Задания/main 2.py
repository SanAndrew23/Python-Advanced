def once(func):
    def wrapper(a):
        b = func(a)
        return b
    return wrapper

@once
def summarise(a):
    print('Вызов функции')
    return a + 1

print(summarise(1))
print(summarise(1))
print(summarise(1))
print(summarise(1))