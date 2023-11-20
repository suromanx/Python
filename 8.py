number = input('Введите число')
day = {1:'Понедельник',2:'Вторник',3:'Среда',4:'Четверг', 5:'Пятница', 6:'Суббота', 7:'Воскресенье'}
result = ''
for i in number:
    if i.isdigit():
        digit = int(i)
        if 1 <= digit <= 7:
            result += day[digit] + ' '
        else:
            result += 'unknown'

print(result)