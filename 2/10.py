try:
    a = float(0)
    b = float(0)
    if a != 0:
        x = (b-1) / (a - 1)
        print(f'Решение уравнения - {x}')

except:
    print(ValueError('Введено нулевое значение'))
