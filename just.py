#Ordinary number
number = int(input('VV'))
num = number // 2
k = 2
while k <= num:
   if number % k == 0:
       print ('не простое')
       break
   k =+ 1
else:
    print('простое')

print('the end')