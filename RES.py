res = 'Это число '
txt = input('Введите название числа')
txt = txt.lower()
if txt == 'один' or txt == 'единица':
    res += str (1)
elif txt == 'два' or txt == 'двойка':
    res += '2'
elif txt == 'три' or txt == 'тройка':
    res += '3'
else:
    res+='ERROR'

print(res)
