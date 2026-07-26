import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n=int(input())#28656
    # n=1
    if n==1:
        print(n)
        return
    temp=[0]*n
    # print(len(temp))
    temp[0]=1
    temp[1]=1
    # t[i]=t[i-1]+t[i-2]
    for i in range(2,n):
        temp[i]=temp[i-1]+temp[i-2]
    # print(temp)
    print(sum(temp))

if __name__ == '__main__':
    main()
