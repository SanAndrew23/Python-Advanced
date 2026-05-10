def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        yield y
        x, y = y, x + y

for i in fibonacci(10):
    print(i)