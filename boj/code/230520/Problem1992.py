# baekjoon Problem1992
# input: 2D array
# output: the number of white, blue sqaure
# 05-20-2023

import sys

def divide(a, l1, l2, r1, r2):
    global result
    iff = a[r1-1][r2-1] - a[l1-1][r2-1] - a[r1-1][l2-1] + a[l1-1][l2-1]
    if iff == (r2-l2)*(r1-l1):
        result.append('1')
    elif iff == 0:
        result.append('0')
    else:
        result.append('(')
        m1 = (l1+r1)//2
        m2 = (l2+r2)//2
        divide(a, l1, l2, m1, m2)
        divide(a, l1, m2, m1, r2)
        divide(a, m1, l2, r1, m2)
        divide(a, m1, m2, r1, r2)
        result.append(')')


def problem1992():
    num = int(input())
    array = [0]*(num+1)
    array[0] = [0]*(num+1)
    for i in range(1, num+1):
        array[i] = list(sys.stdin.readline().rstrip())
        array[i].insert(0, 0)

    for i in range(1, num+1):
        for j in range(1, num+1):
            array[i][j] = int(array[i][j]) + array[i][j - 1] + array[i - 1][j] - array[i - 1][j - 1]

    global result
    result = []
    divide(array, 1, 1, num+1, num+1)
    print("".join(result))


problem1992()