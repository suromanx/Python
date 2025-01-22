number  = input('Введите число')

if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):
    print(f'Вы ввели число : {number}')

    tuple_number = tuple(str(number))
    print(f'Создан кортеж {tuple_number}')

    rev_tuple = tuple(reversed(tuple_number))
    print(f'Кортеж в обратном порядке {rev_tuple}')

else:
    print('Пожалуйста введите число, это не число')