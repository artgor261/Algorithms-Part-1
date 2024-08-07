def binary_search(array, k):
    l = 0
    n = len(array)
    try:
        while l <= n:
            i = (n + l) // 2
            if array[i] == k:
                return i
            elif k > array[i]:
                l = i + 1
            else:
                n = i - 1
    except IndexError:
        pass
    return -1


def main():
    array = list(map(int, input().split()))[1:]
    k = list(map(int, input().split()))[1:]
    for i in k:
        print(binary_search(array, i))


main()
