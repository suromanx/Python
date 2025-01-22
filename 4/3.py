vowel = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
text = input('Введите текст')

intersections = vowel.intersection(text)
print(f'В вашем тексте следующие гласные :{intersections}')