from random import randint
n = 6
list = [randint(0,10) for _ in range (n)]
print(list)
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
print(list)