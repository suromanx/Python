consonants = ["Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"]
vowels = ["А", "И", "О", "У", "Ы", "Э", "Я"]


def incrypt(text):
    encrypted_text = []
    for char in text:
        if char.upper() in consonants:
            index = consonants.index(char.upper())
            new_word = consonants[(index + 1) % len(consonants)]
            encrypted_text.append(new_word if char.isupper() else new_word.lower())
        elif char.upper() in vowels:
            index = vowels.index(char.upper())
            new_word = vowels[(index + 1) % len(vowels)]
            encrypted_text.append(new_word if char.isupper() else new_word.lower())
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


def decrypt(text):
    decrypt_text = []
    for char in text:
        if char.upper() in consonants:
            index = consonants.index(char.upper())
            new_word = consonants[(index - 1) % len(consonants)]
            decrypt_text.append(new_word if char.isupper() else new_word.lower())
        elif char.upper() in vowels:
            index = vowels.index(char.upper())
            new_word = vowels[(index - 1) % len(vowels)]
            decrypt_text.append(new_word if char.isupper() else new_word.lower())
        else:
            decrypt_text.append(char)
    return ''.join(decrypt_text)


user_input = 'Текст для шифрования и дешифрования'

# Шифруем текст
encrypted = incrypt(user_input)
print("Зашифрованный текст:", encrypted)

# Дешифруем текст
decrypted = decrypt(encrypted)
print("Дешифрованный текст:", decrypted)
