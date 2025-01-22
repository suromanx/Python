cols = 5
rows = 3
z = 0
matrix = [[0 for i in range(cols)] for j in range(rows)]
up = 0
down = 0    
for i in range(rows):
    for j in range(cols):
        z += 1
        matrix[i][j]+=z
        if z == cols:
            for j in range(-1, rows, 4):
                for i in range(1,rows):
                    z += 1
                    matrix[i][j] += z




def print_matrix(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))  # Преобразуем элементы в строки для корректного вывода


print_matrix(matrix)
