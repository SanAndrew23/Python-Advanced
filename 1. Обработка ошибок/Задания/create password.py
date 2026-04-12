def create_password(password):
    if len(password) < 8:
        raise ValueError('Длина пароля должна быть больше 8 символов')
    elif password.isdigit():
        raise TypeError('Пароль должен быть в str')
try:
    password = input()
    create_password(password)
except ValueError as e:
    print(f'Ошибка: {e}')
except TypeError as e:
    print(f'Ошибка: {e}')