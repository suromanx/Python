def main():
    try:
        # Ввод целого числа от пользователя
        num = int(input('Введите целое число: '))
        octal_num = oct(num)
        reversed_octal_num = octal_num[::-1]

        # Вывод результата
        print(f'Число {num} в восьмеричной системе: {octal_num}')
        print(f'Перевернутое восьмеричное представление: {reversed_octal_num}')

    except ValueError:
        print('Ошибка: Пожалуйста, введите целое число.')


if __name__ == "__main__":
    main()