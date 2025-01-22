text_1 = '123'
text_2 = 'АБВГДЕЁЖЗ'
new_text = ''
max_length = max(len(text_1),len(text_2))
for char in range(max_length):
    if char < len(text_1):
        new_text += text_1[char]
    else:
        new_text +='*'
    if char < len(text_2):
        new_text += text_2[char]
    else:
        new_text +='*'
print(new_text)