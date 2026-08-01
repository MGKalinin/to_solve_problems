import sys

#6. OpenCalculator

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    first = set(map(str,input().split()))
    second = set([i for i in input()])
    # print(first)
    # print(second)

    ans=second-first
    print(len(ans))

if __name__ == '__main__':
    main()
