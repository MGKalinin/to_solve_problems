import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    temp=list(map(int,input().split()))
    # temp=[1 ,5 ,1 ,5 ,1]
    count=0
    for i in range(1,len(temp)-1):
        if temp[i]>temp[i-1] and temp[i]>temp[i+1]:
            count+=1
    print(count)


if __name__ == '__main__':
    main()
