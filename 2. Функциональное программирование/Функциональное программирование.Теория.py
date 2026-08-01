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

#3.4 Вложенные comprehension
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
transposed = [[row[element] for row in matrix] for element in range(3)]
print(transposed)
'''

#4.1 Генераторы и yield
#Пример простого генератора
'''
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up(5)
print(next(gen))
print(next(gen))
print(next(gen))

for i in count_up(5):
    print(i, end = ' ')
'''

#Обычная функция хранит все в памяти, а генератор вычисляет по одному
#4.2 Генераторное выражение
'''
list_comp = [x ** 2 for x in range(10)]
gen_comp = (x ** 2 for x in range(10))

print(type(list_comp))
print(type(gen_comp))
'''

#4.3 yield from
'''
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2, 3], 'abs', range(4, 7)))
print(result)
'''

#4.4 Бесконечные генераторы
'''
#Бесконечная последовательность Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for i in range(10)]
print(first_10)

#Конвейер из генераторов
def read_numbers(data):
    for n in data:
        yield n

def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square(numbers):
    for n in numbers:
        yield n ** 2

data = range(1, 11)
pipeline = square(filter_even(read_numbers(data)))
print(list(pipeline))
'''

#4.5* Протокол итератора
'''
def simple():
    yield 1
    yield 2

gen = simple()
print(next(gen))
print(next(gen))
print(next(gen))
'''

#5.1 Итераторы