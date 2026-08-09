import sys

#8. Возрастает ли список?


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # text= set(sys.stdin.read().split())
    # print(len(text))
    temp = list(map(int, input().split()))
    # print(min(temp))

    # temp=[2,2,2]
    count=1
    for i in range(len(temp)-1):
        if temp[i]<temp[i+1]:
            # print(temp[i], temp[i+1])
            count+=1
            # print(count)

    print("YES" if count==len(temp) else "NO")


if __name__ == '__main__':
    main()
