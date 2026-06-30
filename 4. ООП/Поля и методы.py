class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} говорит: Гав!"

    def info(self):
        return f"{self.name} ({self.breed}), {self.age} лет"


rex = Dog("Рекс", "Немецкая овчарка", 3)
buddy = Dog("Бадди", "Лабрадор", 5)

print(rex.bark())   # Рекс говорит: Гав!
print(buddy.info()) # Бадди (Лабрадор), 5 лет