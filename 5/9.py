my_text = 'Привет этот текст не такой уж и длинный'
new_text = []
word = ''
for char in my_text:
    if char != ' ':
        word += char
    else:
        if word:
            new_text.append(word)
            word = ''

if word:
    new_text.append(word)

else:
    print('Ввел что то не то')
print(new_text)

max_len = max(new_text,key=len)
min_len = min(new_text,key=len)

new_text.remove(max_len)
new_text.remove(min_len)


print(new_text)


