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
print(new_text)
new_text.reverse()
reverse_text = []
for char in new_text:
    reverse_text.append(char)
print(reverse_text)



