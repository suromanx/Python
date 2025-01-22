text = 'АБВГДЕЁЖЗ'
new_text = ''

for char in range(0,len(text)-1,2):
        new_text += text[char+1]
        new_text += text[char]
if len(text)% 2 != 0:
    new_text += text[-1]

print(new_text)
