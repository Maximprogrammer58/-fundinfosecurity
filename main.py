import crypto

def main():
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    text = '''Использование автоматизированных систем во всех сферах деятельности человека, основанных на применении современных информационно-коммуникационных технологий, выдвинуло целый ряд проблем перед разработчиками и пользователями этих систем. Одна из наиболее острых проблем – проблема информационной безопасности, которую необходимо обеспечивать, контролировать, а также создавать условия для ее управления.'''
    key = crypto.create_key()
    print(alphabet)
    print(text)
    print(crypto.caesar_cipher_encode(text.upper(), 3))
    print(key)
    print(crypto.encryption(text.upper(), key))


if __name__ == "__main__":
    main()
    d = crypto.write_frequency("freq.json")
    sorted_tuple = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
