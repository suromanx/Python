def main():
    try:
        # Ввод целого числа от пользователя
        num = int(input('Введите целое число: '))
        bin_num = bin(num)[2:]

        answer = sum(int(i) for i in bin_num)
        # Вывод результата
        print(f'суммa значений всех битов в бинарном представлении этого числа: {answer}')
    except ValueError:
        print('Ошибка: Пожалуйста, введите целое число.')


if __name__ == "__main__":
    main()