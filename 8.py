li_st = list(input('Введите список чисел через пробел: ').split())
max_value = int(input('Введите максимальное значение: '))

# Преобразовать элементы списка в целые числа
li_st = [int(x) for x in li_st]

# Вычислить сумму чисел в диапазоне, исключая числа из списка
sum_result = 0
for k in range(1, max_value + 1):
    if k not in li_st:
        sum_result += k

print(f'Сумма чисел от 1 до {max_value}, исключая числа из списка: {sum_result}')
