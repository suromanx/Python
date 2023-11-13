number = int(input('Введите число'))
print('Число делится на :'+str(1))
k = 1
while k < number//2:
    if number %k!=0:
        print('Делится на,', k)
    k = k+1
print('Число делится на :', number)
