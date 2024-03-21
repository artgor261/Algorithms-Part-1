import math


def fib_digit(n):
    return fib(math.pow(10, 7))[n] % 10


def fib(n):
    arr = list()
    arr.append(0)
    arr.append(1)
    i = 2

    while i <= n:
        arr.append((arr[i - 1] % 10) + (arr[i - 2] % 10))
        i += 1

    return arr


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
