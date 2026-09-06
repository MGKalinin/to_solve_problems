import sys
import math

#9. Умножай и транспонируй!

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    a,b = map(int,input().split())
    print(math.gcd(a,b))
    print(math.lcm(a,b))

if __name__ == '__main__':
    main()
