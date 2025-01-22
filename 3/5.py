from random import *
rows = 4
cols = 5
matrix = [[randint(0,10) for _ in range (cols)] for _ in range(rows)]


for row in matrix:
    print(' '.join(map(str,row)))


#удалить строку и столбец
print()
matrix.pop(0)
for i in range(len(matrix)):
    matrix[i]=matrix[i][1:]


for row in matrix:
    print(' '.join(map(str,row)))
