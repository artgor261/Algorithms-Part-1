from sys import stdin


def get_key(dictionary, code):
    if code in dictionary.values():
        for key, value in dictionary.items():
            if value == code:
                return key
    return None


def decode(huffman_table, bin_str):
    if bin_str:
        start = 0
        end = 1
        decode_str = str()
        while end <= len(bin_str):
            letter = get_key(huffman_table, bin_str[start:end])
            if letter:
                decode_str += letter
                start = end
                end = start + 1
            else:
                end += 1
        return decode_str
    return None


def fill_huffman_table(user_input):
    if user_input:
        count = int(user_input[0][0])
        array = list()
        huffman_table = dict()
        for string in user_input:
            array.append(string)
        array.pop(0)
        for code in array[0:count]:
            huffman_table[code[0].replace(':', '')] = code[1]
        return huffman_table
    return None


def get_bin_str(user_input):
    if user_input:
        return user_input[-1]
    return None


def main():
    user_input = list()
    bin_str = str()
    for line in stdin:
        user_input.append(line.split())
    for line in get_bin_str(user_input):
        bin_str += line
    huffman_table = fill_huffman_table(user_input)
    print(decode(huffman_table, bin_str))


main()
