

try:
    x =float(d)
    y = float(3**3)

    result = f'{x} > {y}' if x > y else f'{x} < {y}' if x < y else x == y

    print(result)
except:
    print('ValueError : Введите числовые значения!')
