import sys


def mergesort(arr, l, r, inversion_count):
    if l < r:
        m = (l + r) // 2
        merge(mergesort(arr, l, m, inversion_count),
              mergesort(arr, m + 1, r, inversion_count), inversion_count)
    return sorted(arr[l:r+1])


def merge(a, b, inversion_count):
    i = 0
    j = 0
    a_len = len(a)
    b_len = len(b)
    sorted_array = list()

    while i < a_len and j < b_len:
        if a[i] > b[j]:
            inversion_count[0] += (a_len - i)
            sorted_array.append(b[j])
            j += 1
        else:
            sorted_array.append(a[i])
            i += 1

    while i < a_len:
        sorted_array.append(a[i])
        i += 1
    while j < b_len:
        sorted_array.append(b[j])
        j += 1


def main():
    inversion_count = [0]
    lines = sys.stdin.readlines()
    arr = list()
    for num in lines[1].split():
        arr.append(int(num))
    mergesort(arr, 0, len(arr), inversion_count)
    print(inversion_count[0])


main()
