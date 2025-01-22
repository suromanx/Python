x = int(input('Введите целое число'))
num = [9,8,7,6,5,4,3,2,1,0]
r = []
for i in str(x):
    digit = int(i)
    if digit in num:
        r.append(num[digit])
print(r)
