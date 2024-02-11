import crypto
import file_handler


def main():
    # part 1
    text = file_handler.read_file("texts/part1/text.txt")
    key = file_handler.read_file("texts/part1/key.txt")
    encrypted_text = crypto.caesar_cipher(text, int(key))
    file_handler.write_file("texts/part1/encrypted_text.txt", encrypted_text)

    #part 2
    code = file_handler.read_file("texts/part2/code.txt")

    print(file_handler.read_json("freq.json"))
    print(crypto.frequency_analysis(code))

    print(code)
    key_dict = file_handler.read_json("texts/part2/key.json")
    decode_text = crypto.decryption_by_key(code, key_dict)
    print(decode_text)
    file_handler.write_file("texts/part2/decode_text.txt", decode_text)


if __name__ == "__main__":
    main()