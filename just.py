#Ordinary number
number = int(input('VV'))
num = number // 2
k = 2
while k < num:
    for k in range (k,num):
        if number % k == 0:
            print ('не простое')
            raise SystemExit(0)
        else:
            print('простое')
            raise SystemExit(0)

print('the end')