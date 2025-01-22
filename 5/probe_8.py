consonants = ["Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"]
vowels = ["А", "И", "О", "У", "Ы", "Э", "Я"]


def incrypt(text):
    text_decrypt = []
    for char in text:
        if char.upper() in consonants:
            index = consonants.index(char.upper())
            new_word = consonants[(index + 1) % len(consonants)]
            text_decrypt.append(new_word if char.isupper() else new_word.lower())
        elif char.upper() in vowels:
            index = vowels.index(char.upper())
            new_word = vowels[(index + 1) % len(vowels)]
            text_decrypt.append(new_word if char.isupper() else new_word.lower())
        else:
            text_decrypt.append(char)
    return ''.join(text_decrypt)


def decrypt(text):
    text_encrypt = []
    for char in text:
        if char.upper() in consonants:
            index = consonants.index(char.upper())
            new_word = consonants[(index - 1) % len(consonants)]
            text_encrypt.append(new_word if char.isupper() else new_word.lower())
        elif char.upper() in vowels:
            index = vowels.index(char.upper())
            new_word = vowels[(index - 1) % len(vowels)]
            text_encrypt.append(new_word if char.isupper() else new_word.lower())
        else:
            text_encrypt.append(char)

    return ''.join(text_encrypt)


user_input = 'Текст для шифрования и дешифрования'

# Шифруем текст
encrypted = incrypt(user_input)
print("Зашифрованный текст:", encrypted)

# Дешифруем текст
decrypted = decrypt(encrypted)
print("Дешифрованный текст:", decrypted)