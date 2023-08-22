# baekjoon Problem1780
# input: 2D array
# output: find the number of -0, 1, 1 squares
# 05-22-2023

import sys


def promise(a, l1, l2, r1, r2):
    cnt = a[l1][l2]
    for i in range(l1, r1):
        for j in range(l2, r2):
            if cnt != a[i][j]:
                return False

    global result
    result[cnt] += 1
    return True


def divide(a, l1, l2, r1, r2):
    if not promise(a, l1, l2, r1, r2):
        temp = (r1 - l1)//3

        for i in range(l1, r1, temp):
            for j in range(l2, r2, temp):
                divide(a, i, j, i+temp, j+temp)


def problem1780():
    num = int(input())
    array = [0]*num
    for i in range(num):
        array[i] = list(map(int, sys.stdin.readline().split()))

    global result
    result = [0, 0, 0]
    divide(array, 0, 0, num, num)
    for i in range(-1, 2):
        print(result[i])


if __name__ == '__main__':
    problem1780()
