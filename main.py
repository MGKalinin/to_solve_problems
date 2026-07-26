import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # D=b**2-4*a*c
    #D>0 x1=(-b-math.sqr(D))/(2*a) x2=(-b+math.sqr(D))/(2*a)
    #D==0 x=-(b/2*a)
    #D<0 нет корней
    a,b,c=map(int,input().split())
    # a,b,c=6 ,-5 ,-8
    D = (b ** 2) - (4 * a * c)
    match D:
        case _ if D==0:
            x=-(b/(2*a))
            print(1)
            print(x)
        case _ if D>0:
            x1=(-b-(D**0.5))/(2*a)
            x2=(-b+(D**0.5))/(2*a)
            print(2)
            print(f'{min(x1,x2):.10f} {max(x1,x2):.10f}')
        case _ if D<0:
            print(0)


if __name__ == '__main__':
    main()
