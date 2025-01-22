height = 7
width = height * 2 - 1
middle = width // 2

for i in range(height):
    for j in range(width):
        if i == 0 and j == middle:
            print("*", end= " ")
        elif i > 0 and (j == middle - i or j == middle + i):
            print("*", end=" ")
        elif i == height//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

