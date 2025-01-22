def encrypt(text):
    encrypted = ''
    for char in text:
        if 'А' <= char <= 'Я':
            if char == 'А':
                encrypted += 'Ю'
            elif char == 'Б':
                encrypted += 'Я'
            else:
                encrypted += chr(ord(char)-2)
        else:
            encrypted += char
    return encrypted
def decrypt(text):
    decrypted = ''
    for char in text:
        if 'А' <= char <= 'Я':
            if char == 'Ю':
                decrypted += 'А'
            elif char == 'Я':
                decrypted += 'Б'
            else:
                decrypted += chr(ord(char)+2)
        else:
            decrypted += char
    return decrypted








original_text = 'АБВГДЕЁЖЗ'
encrypted = encrypt(original_text)
print(f'Зашифрованный текст: {encrypted}')

decrypted = decrypt(encrypted)
print(f'Расшифрованный текст: {decrypted}')