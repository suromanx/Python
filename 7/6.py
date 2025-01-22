complex1 = complex(input('Введите первое комплексное число (в формате a+bj): '))
complex2 = complex(input('Введите второе комплексное число (в формате a+bj): '))

sum_complex = complex1 + complex2
diff_complex = complex1 - complex2
prod_complex = complex1 * complex2
div_complex = complex1 / complex2

results = [sum_complex, diff_complex, prod_complex, div_complex]

moduli = [abs(result) for result in results]
print(moduli)


