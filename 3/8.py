from random import  *
matrix = [randint(0,10) for _ in range(10)]
print(matrix)
even=[]
uneven=[]
print()
for i in range(len(matrix)):
    if i %2 == 0:
        even.append(i)
    else:
        uneven.append(i)

even.sort()
uneven.sort(reverse=True)
print(even)
print(uneven)
for i in range(len(matrix)):
    if i %2 == 0:
        matrix[i] = even.pop(0)
    else:
        matrix[i] = uneven.pop(0)

print()
print(matrix)