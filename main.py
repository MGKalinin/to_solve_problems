import sys

#9. Умножай и транспонируй!

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # n,m,k = map(int,input().split())#строки,столбцы/строки столбцы
    n,m,k=2 ,1 ,3
    # a = [[0]*m for _ in range(n)]
    # b = [[0]*k for _ in range(m)]
    a = [[0], [2]]
    b = [[1,2,8]]
    # for i in range(n):
    #     a[i] = list(map(int,input().split()))
    # for i in range(m):
    #     b[i] = list(map(int,input().split()))
    # c=[[1,2,3],[4,5,6]]
    # d=[[7,8,9],[10,11,12]]

    ans = [[0]*k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for t in range(m):
                ans[i][j] += a[i][t]*b[t][j]
    print(ans)

    ans_t = [[0]*len(ans)  for _ in range(len(ans[0]))]
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            ans_t[j][i] = ans[i][j]

    print(ans_t)
    for row in ans_t:
        print(*row)

if __name__ == '__main__':
    main()
