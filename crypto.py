import json
from collections import Counter
from random import sample


def create_key(alphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") -> str:
    return "".join(sample(alphabet, len(alphabet)))


def encryption(text: str, key: str, alphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") -> str:
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] in alphabet:
            text_list[i] = key[alphabet.find(text_list[i])]
    return "".join(text_list)

def caesar_cipher_encode(text: str, key: int, alphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") -> str:
    encoded_text = ""
    for letter in text:
        if letter in alphabet:
            unicode = ord(letter) - ord(alphabet[0])
            encoded_unicode = (unicode + key) % 32 + ord(alphabet[0])
            encoded_text += chr(encoded_unicode)
        else:
            encoded_text += letter
    return encoded_text


def write_frequency(path: str) -> str:
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)


def frequency_analysis():
    pass


def replacing_letter():
    pass