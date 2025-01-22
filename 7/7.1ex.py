def num_convert(number, base):
    digits = []
    if number == 0:
        print('error')
    while number > 0:
        remainder = number % base
        if remainder > 10:
            digits.append(chr(remainder - 10 + ord('A')))
        else:
            digits.append(str(remainder))
        number //= base
    digits.reverse()
    return ''.join(digits)


def main():
    try:
        number = int(input("Введите число"))
        if number < 0:
            print('Число меньше 0')
        base = int(input("Введите основание"))
        if base not in [2, 8, 10, 16]:
            print('No BASE')
        print(f'Number{number} in base {base} equals {num_convert(number, base)}')

    except ValueError:
        print('Ввели неправильное значение')


if __name__ == '__main__':
    main()
