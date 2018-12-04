def encode(caesar, string):
    encode_string = ''
    for i in string:
        encode_string += caesar[i] if i != ' ' else ' '
    return encode_string


def decode(caesar, string):
    decode_string = ''
    for i in string:
        decode_string += caesar[i] if i != ' ' else ' '
    return decode_string


def reverse(dict):
    return {value: key for key, value in dict.items()}


def generate_dict(shift, start, stop):
    return {chr(i): chr(i + shift if i + shift < stop else start + i + shift - stop) for i in range(start, stop)}


def main(shift, string):
    up_en = generate_dict(shift, 65, 91)
    down_en = generate_dict(shift, 97, 123)
    all_rus = generate_dict(shift, 1040, 1104)

    caesar = {**up_en, **down_en, **all_rus}

    caesar_reverse = reverse(caesar)
    caesar['ё'] = caesar_reverse['ё'] = 'к'
    encode_string = encode(caesar, string)

    decode_string = decode(caesar_reverse, encode_string)
    print(caesar)
    print(caesar_reverse)
    return decode_string


if __name__ == '__main__':
    main(5, 'Как дела')
