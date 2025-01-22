def convert_to_base(number, base):
    if number == 0:
        return '0'

    digits = []
    while number > 0:
        remainder = number % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('A')))
        number //= base

    digits.reverse()
    return ''.join(digits)


def main():
    try:
        base = int(input('Введите основание'))
        if base not in [2, 8, 10, 16]:
            print('Ошибка')
            return
        decimal_number = int(input('Введите число в дес системе'))
        if decimal_number < 0:
            print('ОШибка')
            return

        converted_number = convert_to_base(decimal_number, base)
        print(f'number {decimal_number} in base {base} equals {converted_number}')

    except ValueError:
        print("Ошибка: введены некорректные данные. Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()