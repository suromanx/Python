a, b = eval(input("Введите (через запятую) два числа"))
if (type(b)==int or type(b)==float and type(a)==float or type(a)==int):
    print("Уравнение "+str(a)+"x="+str(b))
    if a!= 0:
        print('Решение уравнения x=:'+str(b/a))
    else:
        if b!= 0:
            print('Решений нет')
        else:
            print('Решение - любое число')
else:
    print('Введены некоректные значения')
    raise SystemExit(0)

print('Решение Завершено')
