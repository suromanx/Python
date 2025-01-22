from fractions import Fraction
def main():
    try:
        # Ввод двух дробей от пользователя
        fraction1 = input('Введите первую дробь (в формате числитель/знаменатель): ')
        fraction2 = input('Введите вторую дробь (в формате числитель/знаменатель): ')

        # Преобразование строкового ввода в дроби
        frac1 = Fraction(fraction1)
        frac2 = Fraction(fraction2)

