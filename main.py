import sys
import math
from collections import Counter

import numpy as np


# 69. Клавиатура

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())# количество клавиш
    k = list(map(int,input().split())) # количество выдерживаемых нажатий i-й клавиши
    v = int(input()) # общее количество нажатий клавиш
    temp = list(map(int,input().split())) # последовательность нажатых клавиш

    # n= 5
    # k = [1, 50, 3, 4, 3]
    # v = 16
    # temp = [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5 ,5 ,4 ,5]
    dict_temp = Counter(temp) # {5: 7, 3: 3, 4: 3, 1: 2, 2: 1}
    sort_dict_temp = dict(sorted(dict_temp.items())) # {1: 2, 2: 1, 3: 3, 4: 3, 5: 7}

    dict_k = {} # {1: 1, 2: 50, 3: 3, 4: 4, 5: 3}
    for i,val in enumerate(k):
        dict_k[i+1]=val

    for key in sort_dict_temp:# пройти циклом и сравнить
        # если значение ключа sort_dict_temp меньше либо равно dict_k -вывести NO
        if sort_dict_temp[key] > dict_k[key]:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
