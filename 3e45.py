number = input('Введите число: ')
num_dict = {'9': '0', '8': '1', '7': '2', '6': '3', '5': '4', '4': '5', '3': '6', '2': '7', '1': '8', '0': '9'}
num = list(number)

for i in range(len(num)):
    if num[i] in num_dict:
        num[i] = num_dict[num[i]]

# Вывод результата после завершения цикла
print("".join(num))
