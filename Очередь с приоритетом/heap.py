import sys


class Heap:
    def __init__(self, elements):
        self.elements = elements

    def insert(self, x):
        self.elements.append(x)
        if len(self.elements) > 1:
            i = len(self.elements) - 1
            parent = self.elements[(i - 1) // 2]
            self.__sift_up(x, parent, i)
        return self.elements

    def extract_max(self):
        if len(self.elements) > 0:
            max_value = self.elements[0]
            i = len(self.elements) - 1
            self.elements[0] = self.elements[i]
            self.elements[i] = max_value
            self.elements.pop()
            if len(self.elements) > 0:
                self.__sift_down(self.elements[0], 0, self.__max_child(0))
            return max_value

    def __sift_down(self, x, i, max_child):
        while (x < max_child) and ((i * 2) + 1 <= len(self.elements) - 1):
            max_child_index = self.elements.index(max_child)
            self.elements[i] = max_child
            self.elements[max_child_index] = x
            i = max_child_index
            max_child = self.__max_child(i)

    def __max_child(self, i):
        if ((i * 2) + 1) < (len(self.elements) - 1):
            child_1 = self.elements[(i * 2) + 1]
            child_2 = self.elements[(i * 2) + 2]
            return max(child_1, child_2)
        elif ((i * 2) + 1) == (len(self.elements) - 1):
            return self.elements[(i * 2) + 1]
        return 0

    def __sift_up(self, x, parent, i):
        while (x > parent) and (i > 0):
            temp = i
            i = self.elements.index(parent)
            self.elements[temp] = parent
            self.elements[i] = x
            parent = self.elements[(i - 1) // 2]


def main():
    heap = Heap(list())
    for line in sys.stdin.readlines():
        if line.split()[0] == "Insert":
            heap.insert(int(line.split()[1]))
        elif line.split()[0] == "ExtractMax":
            print(heap.extract_max())


main()
