class Dog:
    name = None
    breed = None
    age = -float('inf')

rex = Dog()
rex.name = "Рекс"
rex.breed = "Немецкая овчарка"
rex.age = 3

print(f'Кличка: {rex.name}, Порода: {rex.breed}, Возраст: {rex.age}')