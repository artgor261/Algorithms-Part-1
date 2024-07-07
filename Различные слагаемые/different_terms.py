def terms(n):
    terms_list = list()
    i = 1
    while i <= n and (n - i) >= (i + 1):
        n -= i
        terms_list.append(i)
        i += 1
    if (n - i) < (i + 1):
        terms_list.append(n)
    print(len(terms_list))
    for term in terms_list:
        print(term, end=' ')


def main():
    n = int(input())
    terms(n)


main()
