import sys
import math

# A. Правильная скобочная последовательность

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # n = int(input())
    # temp = input().split()
    # x = int(input())
    # n = 5
    temp = ['([)]']
    # answer = temp
    # for c in temp[0]:
    #     print(c)
    # x = -6
    # основная идея пройти по строке-проверить начиная с открытой скобки - удалять из стека
    stack = []
    pattern = {')':'(',
               ']':'[',
               '}':'{'}

    if len(temp[0]) == 1:
        print('no')
        return

    if len(temp[0])%2 != 0:
        print("no")
        return

    for ch in temp[0]:
        # print(ch)
        if ch == '(' or ch == '[' or ch == '{':
            # print(ch)
            stack.append(ch)

        elif ch == ')' or ch == ']' or ch == '}':
            if not stack or stack[-1] != pattern[ch]:
                print('no')
                return
            stack.pop()


    if len(stack) == 0:
        print('yes')
    else:
        print('no')




if __name__ == '__main__':
    main()
