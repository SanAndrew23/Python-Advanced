from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

print(factorial(5))