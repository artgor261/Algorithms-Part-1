def fib_mod(n, m):
    arr = list()
    arr.append(0)
    arr.append(1)
    i = 2

    while i <= n:
        arr.append((arr[i - 1] + arr[i - 2]) % m)
        if arr[i] == 1 and arr[i - 1] == 0:
            arr_len = len(arr) - 2
            return arr[n % arr_len] % m
        i += 1
    return arr[n] % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
