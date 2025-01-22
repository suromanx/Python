def get_bit(bit,num_bit):
    return (bit >> num_bit) & 1


def main():
    try:
        num = int(input('Введите целое число: '))
        bit_num = int(input('Введите номер бита (0 - младший бит): '))

        # Проверяем, что номер бита не отрицательный
        if bit_num < 0:
            print("Ошибка: Номер бита не может быть отрицательным.")
            return

        # Получаем значение бита
        bit_value = get_bit(num, bit_num)
        print(f'Бит номер {bit_num} в числе {num} это {bit_value}')

    except ValueError:
        print('Ошибка: Пожалуйста, введите целое число.')

if __name__ == "__main__":
    main()