# baekjoon Problem2630
# input: 2D array
# output: the number of white, blue sqaure
# 05-20-2023

import sys
sys.setrecursionlimit(10**6)

def divide(a, l1, l2, r1, r2):
    global result
    iff = a[r1-1][r2-1] - a[l1-1][r2-1] - a[r1-1][l2-1] + a[l1-1][l2-1]
    if iff == (r2-l2)*(r1-l1):
        result[1] += 1
    elif iff == 0:
        result[0] += 1
    else:
        m1 = (l1+r1)//2
        m2 = (l2+r2)//2
        divide(a, l1, l2, m1, m2)
        divide(a, l1, m2, m1, r2)
        divide(a, m1, l2, r1, m2)
        divide(a, m1, m2, r1, r2)


def problem2630():
    num = int(input())

    array = [0]*(num+1)

    array[0] = [0]*(num+1)
    for i in range(1, num+1):
        array[i] = list(map(int, sys.stdin.readline().split()))
        array[i].insert(0, 0)
    for i in range(1, num+1):
        for j in range(1, num+1):
            array[i][j] = array[i][j] + array[i][j-1] + array[i-1][j] - array[i-1][j-1]

    global result
    result = [0, 0]

    divide(array, 1, 1, num+1, num+1)
    print(result[0])
    print(result[1])

problem2630()