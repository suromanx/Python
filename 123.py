number = int(input('Input the number'))
number_tuple = tuple(map(int,str(number)))

print('Number Tuple:', number_tuple)
print('Convert Tuple', number_tuple[::-1])