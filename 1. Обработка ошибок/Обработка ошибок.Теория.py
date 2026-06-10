#Иерархия исключений
'''BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ValueError
      ├── TypeError
      ├── KeyError
      │    └── IndexError (косвенно через LookupError)
      ├── ZeroDivisionError
      └── ... (и многие другие)
except - встроенные исключения
raise - генерация исключений
'''

#1.

'''try:
    код, который может вызвать исключение
except:
    код, выполняемый при возниконовении исключения
else:
    код, выполняемый если исключений не было
finally:
    код, выполняемый всегда'''

#2. Пример. Обработка ввода пользователя

'''
try:
    number = int(input('Введите число'))
    result = 100 / number
except ValueError:
    print('Ошибка: введите целое число')
except ZeroDivisionError:
    print('Ошибка: на нуль делить нельзя')
else:
    print(result)
finally:
    print('Конец программы')
'''

#3. Получение информации об исключении и перехват исключений
#3.1
'''
try:
    data = {'name': 'Alice'}
    print(data['age'])
except KeyError as e:
    print(f'Ключ не найден: {e}')
'''
#3.2
'''
try:
    result = 10 / 0
except Exception as e:
    print(f'Произошла ошибка: {type(e).__name__} - {e}')

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f'Файл "{filename}" не найден.')
        content = None
    else:
        print('Файл успешно прочитан.')
        file.close()
    finally:
        print("Операция завершена.")
    return content

read_file('data.txt')
'''

#4. Несколько блоков except

'''
def safe_divide(a, b):
    try:
        result = a / b
    except TypeError:
        print('Ошибка: оба аргумента должны быть числами.')
    except ZeroDivisionError:
        print('Ошибка: делитель не может быть равен нулю.')
    else:
        return result

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide('10', 2))
'''

#5. Перехват нескольких исключений в одном блоке
'''
try:
    value = int(input('Введите число: '))
    result = 100 / value
except (ValueError, ZeroDivisionError) as e:
    print(f'Ошибка {type(e).__name__}: {e}')
'''

#6. raise - генерация исключений
#raise ТипИсключения('Сообщение')
#Пример: валидация данных
'''
def set_age(age):
    if not isinstance(age, int):
        raise TypeError('Возраст должен быть целым числом.')
    if not(0 < age < 150):
        raise ValueError('Возраст должен быть в диапазоне от 0 до 150')
    return age

try:
    set_age(-4)
except ValueError as e:
    print(f'Ошибка: {e}')
'''
#6.1. Повторная генерация исключений re-raise: Внутри блока except можно использовать
#raise без аргументов, чтобы пробросить текущее исключение дальше — после его частичной обработки:
'''
def process_data(data):
    try:
        result = 100 / data
    except ZeroDivisionError:
        print('Логируем ошибку деления на нуль...')
        raise

try:
    process_data(0)
except ZeroDivisionError:
    print('Исключение поймано в вызывающем коде')
'''

#6.2. raise... from...

'''
try:
    int('abc')
except ValueError as e:
    raise RuntimeError('Не удалось преобразовать данные.') from e
'''


#7 Exception - собственные исключения
#7.1
'''
class NegativeValueError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeValueError('Нельзя извлечь корень из отрицательного числа')
    return n ** 0.5

try:
    print(square_root(-4))
except NegativeValueError as e:
    print(f'Ошибка: {e}')
'''
#7.2 Расширенный вариант