class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.frequency = left.frequency + right.frequency


class Node:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.left = None
        self.right = None


def count(string):
    s = set()
    for letter in string:
        s.add(letter)
    return len(s)


def get_alphabet(string):
    s = set()
    for letter in string:
        s.add(letter)
    return sorted(s)


def extract_min(queue):
    def return_frequency(node):
        return node.frequency
    minimum = min(queue, key=return_frequency)
    queue.remove(minimum)
    return minimum


def huffman(f, queue):
    for i in f:
        queue.append(i)
    while len(queue) > 1:
        min1 = extract_min(queue)
        min2 = extract_min(queue)
        new_node = Tree(min1, min2)
        queue.append(new_node)
    return queue


def encode(root, code_string, huffman_table):
    if type(root) is Node:
        huffman_table[root.letter] = code_string
    else:
        encode(root.left, code_string + '0', huffman_table)
        encode(root.right, code_string + '1', huffman_table)


def string_size(string, huffman_table):
    string.split()
    str_size = 0
    for letter in string:
        str_size += len(huffman_table.get(letter))
    return str_size


def fill_nodes(user_input, alphabet):
    index = 0
    nodes = list()
    while index < len(alphabet):
        letter = alphabet[index]
        freq = 0
        for ch in user_input:
            if ch == letter:
                freq += 1
        index += 1
        nodes.append(Node(letter, freq))
    return nodes


def bin_string(user_input, huffman_table):
    bin_str = str()
    for ch in user_input:
        bin_str += huffman_table.get(ch)
    return bin_str


def main():
    user_input = input()
    alphabet = get_alphabet(user_input)
    nodes = fill_nodes(user_input, alphabet)
    huffman_table = dict()
    queue = list()
    amount = count(user_input)
    huffman(nodes, queue)
    if len(alphabet) > 1:
        encode(queue[0], '', huffman_table)
    elif len(alphabet) == 1:
        huffman_table[user_input[0]] = '0'
    else:
        print('')
    print(amount, string_size(user_input, huffman_table))
    for letter, code in huffman_table.items():
        print(letter + ': ' + code)
    print(bin_string(user_input, huffman_table))


main()
