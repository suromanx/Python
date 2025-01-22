x = [2, 23, 4, 3424, 52, 45]
y = [2, 23, 4, 3424, 52, 45]
if len(x) == len(y):
    for i in range(len(x)):
        if x[i] != y[i]:
            print('Списки не равны поэлементно')
            break
    else:
        print('Списки Равны')

else:
    print('Длины списков не равны')