import sys

#9. Умножай и транспонируй!

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # n,m,k = map(int,input().split())#строки,столбцы/строки столбцы
    n,m,k=6,1,4
    # a = [[0]*m for _ in range(n)]
    # b = [[0]*k for _ in range(m)]
    a = [[6], [1], [3], [3], [1], [9]]
    b = [[10, 2, 0, 3]]
    # for i in range(n):
    #     a[i] = list(map(int,input().split()))
    # for i in range(m):
    #     b[i] = list(map(int,input().split()))



if __name__ == '__main__':
    main()
