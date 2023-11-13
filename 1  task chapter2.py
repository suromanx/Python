number =int(input('Введите Число блять'))
num = number // 2
k = 1
while k < num:
    if number // k == 0:
        print('Это ахуеть какое простое число')
    else:
        print('Это не очень то и простое число')
        break
print('Программа завершена')f