import json

def caesar_cipher(text: str, key: int, alphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") -> str:
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            unicode = ord(letter) - ord(alphabet[0])
            encrypted_unicode = (unicode + key) % 32 + ord(alphabet[0])
            encrypted_text += chr(encrypted_unicode)
        else:
            encrypted_text += letter
    return encrypted_text

def write_frequency(path: str) -> str:
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)

def frequency_analysis(text: str) -> dict:
    frequency = {}
    for letter in text:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    for key in frequency:
        frequency[key] = frequency[key] / len(text)
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

def decryption_by_key(code: str, key: dict) -> str:
    for letter in key:
        code = code.replace(letter, key[letter])
    return code