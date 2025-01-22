my_dick = {
    "Толстой": "Война и мир",
    "Достоевский": "Преступление и наказание",
    "Пушкин": "Евгений Онегин",
    "Гоголь": "Мертвые души",
    "Чехов": "Вишневый сад"
}

num_right = 0
num_wrong = 0
for i in my_dick.keys():
    answer = input(f'Введи что написал тов.  {i}')
    answer = answer.lower().strip()
    if answer == my_dick[i].lower():
        num_right += 1
    else:
        num_wrong += 1

print('Вот что из тебя получилось, литератор :')
print(f'Твой результат : {num_right} правильных ответов и {num_wrong} неправильных')

