import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(n):
    i = 0
    while i != n:
        if is_prime(i):
            yield i
        i += 1


for i in prime_generator(50):
    print(i)