x = 1
y = 2
z = 4

c = 0
b = 0

list_numbers = [x, y, z]
for i in range(x,y):
    c += 1
for j in range(y,z ):
    b += 1
if c == b:
    print('Это числовая последовательность')

else:
    print("Это не числовая последовательность")
