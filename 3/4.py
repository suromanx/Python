rows = 4  # количество строк
cols = 5  # количество столбцов
matrix = [[0 for _ in range(cols)] for _ in range(rows)]  # создаем пустую матрицу
z = 0  # начальное значение для заполнения

# Определяем начальные границы
top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = z
        z += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = z
        z += 1
    right-=1
    if top <= bottom:
        for j in range(right, left-1,-1):
            matrix[bottom][j] = z
            z += 1
        bottom -= 1
        for i in range(bottom, top-1,-1):
            matrix[i][left] = z
            z += 1
        left += 1

for row in matrix:
    print(row)
