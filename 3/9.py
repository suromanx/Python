from random import *
matrix = [randint(0,10) for _ in range(10)]
print(matrix)
new_matrix = []
for i in range(len(matrix)-1):
    new_matrix.append(matrix[i])
    sum_val = matrix[i] + matrix[i+1]
    new_matrix.append(sum_val)
new_matrix.append(matrix[-1])
print()
print(new_matrix)