number = int(input('Введите Число блять'))
num = number // 2
k = 2
while k < num:
    if number % k == 0:
        print('Это число не является простым')
        break
    else:
        k = k+1

else:
    print("Это простое число")
print('Программа завершена')