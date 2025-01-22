a, b = eval(input("Введите два значения через запятую"))
if (type(a)==float or type(a)==int and type(b)==float or type(b)==int):
    print('Решаем уравнение '+str(a)+'x='+str(b))
    if a!=0:
        print("Решение Уравнения x=:"+str(b/a))
    else:
        if b!=0:
            print('Решений Нет!')
        else:
             print('Решение-любое число!')
else:
    print('Error!')
    raise SystemExit(0)
print("Поиск решения завершён!")
