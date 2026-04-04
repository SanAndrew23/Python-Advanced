while True:
    try:
        num1 = float(input('X1: '))
        num2 = float(input('X2: '))
        print(num1 / num2)
        action = input('Продолжить (Y/N)?')
        if action.lower() != 'y':
            break
    except ZeroDivisionError:
        print('X2 не может равняться нулю!')
    except ValueError as e:
        print(f'Ошибка входных данных {e}')
    except Exception as e:
        print(f'Ошибка {e}')

