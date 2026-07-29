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
from enum import unique

#1.2 Lambda с несколькими аргументами
'''
add = lambda a, b: a + b
multiply = lambda a, b, c: a * b * c
print(add(3,4))
print(multiply(2, 3, 4))
'''

#1.3 lamba в сортировке
'''students = [
    {'name': 'Alice', 'grade': 88},
    {'name': 'Bob', 'grade': 95},
    {'name': 'Charlie', 'grade': 72},
]

sorted_students = sorted(students, key=lambda s: s['grade'], reverse=True)
for s in sorted_students:
    print(s['name'], s['grade'])
'''

#1.4 Ограничения lambda
'''Lambda может содержать только одно выражение. В ней нельзя использовать
инструкции: if/else в виде блоков, циклы, присваивания и т.д. 
Для сложной логики следует использовать обычные функции через def'''


#2 map, filter, reduce
'''map применяет функцию каждому элементу итерируемого объекта и возвращает итератор с результатами.'''
'''Примеры'''
'''numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))
print(squares)

words = ['hello', 'world', 'python']
upper_words = list(map(str.upper, words))
print(upper_words)

a = [1, 2, 3]
b = [10, 20, 30]

sums = list(map(lambda x, y: x + y, a, b))
print(sums)'''

'''filter фильтрует элементы итерируемого объекта, оставляя только те, для которых функция возвращает True'''
'''numbers_str = ['1', '-2', '3', '-4', '0', '-6']
numbers = map(int, numbers_str)

positives = list(filter(lambda x: x > 0, numbers))
print(positives)

evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(evens)

mixed = [0, 1, "", "hello", None, [], [1, 2], False, True]
truthy = list(filter(None, mixed))
print(truthy)'''
'''reduce(). Последовательно применяет функцию к элементам, «сворачивая» последовательность в одно значение.
Функция принимает два аргумента: накопленный результат и текущий элемент. Находится в модуле functools'''
'''
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)
print(total)

product = reduce(lambda acc, x: acc * x, numbers)
print(product)

max_val = reduce(lambda a, b: a if a > b else b, numbers)
print(max_val)

total_with_start = reduce(lambda acc, x: acc + x, numbers, 100)
print(total_with_start)
'''

#3 Генераторы словарей и множеств(Comprehensions)
#3.1 Генератор списков
'''
squares = [x ** 2 for x in range(1, 8)]
print(squares)

evens = [x for x in range(0, 20) if x % 2 == 0]
print(evens)

words = ['hello', 'world', 'python']
upper = [x.upper() for x in words if len(x) > 4]
print(upper)

pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(pairs)
'''

#3.2 Генератор словарей
'''
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)

words = ['apple', 'banana', 'cherry']
lengths = {word: len(word) for word in words}
print(lengths)

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v > 2}
print(filtered)
'''

#3.3 Генератор множеств
'''
numbers = {1, 2, 2, 2, 3, 3, 4, 5, 5}
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)

words = ["hello", "world", "hi", "python", "py"]
short_upper = {x.upper() for x in words if len(x) <= 3}
print(short_upper)

sentence = "the quick brown fox jumps over the lazy dog"
unique_chars = {letter for letter in sentence if letter != ' '}
print(len(unique_chars))
'''

#3.4 Вложенные comprehensions

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
transposed = [[row[element] for row in matrix] for element in range(3)]
print(transposed)