def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Возраст должен быть целым числом.")
    if age < 0 or age > 150:
        raise ValueError("Возраст должен быть в диапазоне от 0 до 150.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Ошибка: {e}")