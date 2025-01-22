encripted_text = 'АБВГДЕЕЖЗ'
decripted_text = ''
for char in range(0,len(encripted_text),2):
    if char+1  < len(encripted_text):
        decripted_text += encripted_text[char+1]
    decripted_text += encripted_text[char]
print(decripted_text)