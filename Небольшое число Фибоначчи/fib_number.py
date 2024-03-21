def fib(n):
    arr = list()
    arr.append(0)
    arr.append(1)
    i = 2

    while i <= n:
        arr.append(arr[i - 1] + arr[i - 2])
        i += 1

    return arr[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
