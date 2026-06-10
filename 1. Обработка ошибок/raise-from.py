def f():
    try:
        # int("abc")
        11 - 'a'
    except ValueError as v:
        raise RuntimeError("Не удалось преобразовать данные.") from v
    except TypeError as t:
        raise RuntimeError("Невозможно выполнить операцию") from t

try :
    f()
except Exception as e:
    # С помощью __cause__ можно получить базовое исключение
    print(e.__cause__)
    print(e)
