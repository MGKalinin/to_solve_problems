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
    ans = [[sum(a[i][p] * b[p][j] for p in range(m)) #умножение
           for i in range(n)]
           for j in range(k)]
    temp = [[ans[i][j] for i in range(len(ans))]
           for j in range(len(ans[0]))]

    print(ans)
    print(temp)


if __name__ == '__main__':
    main()
