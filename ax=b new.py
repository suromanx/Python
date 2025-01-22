a,b = eval(input('Введите два числа через запятую'))
if (type(a)!=int and type (a)!=float or type(b)!=int and type(b)!=float):
    print('Введены некорректные значения')
    raise SystemExit(0)
elif a != 0:
    txt = 'x='+str(b/a)
elif b != 0:
    txt = 'Решений нет!'
else:
    txt = 'Решение - любое число'
print('Решение Уравнения'+str(a)+'x='+str(b))
print(txt)
print("Поиск решения завершён")
