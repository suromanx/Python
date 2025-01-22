my_text = input('текст введи  ')

my_dick = {}

for i in my_text:
    if i in my_dick:
        my_dick[i]+=1
    else:
        my_dick[i] = 1
print()
print('Вот что ты сделал с добби')
print(my_dick)