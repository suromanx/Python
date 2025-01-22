num_1 = input()
num_2 = input()
a = set()
b = set()
for i in num_1:
    a.add(i)
for i in num_2:
    b.add(i)

common_digits = a.intersection(b)

print(a)
print(b)
print(common_digits)