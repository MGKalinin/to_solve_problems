import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # a=int(input())
    # b=int(input())
    # c=int(input())
    a=3
    b=4
    c=5

    if (a+b)>c and (a+c)>b and (b+c)>a:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
