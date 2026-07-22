#1.1 Lambda-функции
# Синтаксис lambda аргументы: Выражение
#Сравнение lambda-функции с обычной
'''
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2
print(square(5))
print(square(5))
'''

#1.2 Lambda с несколькими аргументами
'''
add = lambda a, b: a + b
multiply = lambda a, b, c: a * b * c
print(add(3,4))
print(multiply(2, 3, 4))
'''

#lamba в сортировке