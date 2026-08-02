import sys

#7. Количество слов в тексте


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    text= set(sys.stdin.read().split())
    print(len(text))

if __name__ == '__main__':
    main()
