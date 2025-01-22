from random import *
a = [randint(0,10) for _ in range(10)]
b = [randint(0,10) for _ in range(10)]
new = []
print(a)
print(b)
print()
for i in range(len(a)):
    new.append(a[i])
    new.append(b[i])

print()
print(new)