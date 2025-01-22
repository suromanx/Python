num = int(input("Введите число"))
if num >= 0:
    my_list = [i for i in range(1,num+1)]
    list_reversed = my_list[::-1]
    my_dict = {my_list[i]: list_reversed[i] for i in range(len(my_list))}



else:
    print("ввели отрицательное число или равное нулю")

print('Вот что было орк')
print(my_list)
print('Вот что стало орк')
print(my_dict)

