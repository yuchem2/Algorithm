# baekjoon Problem1629
# input: 3 integer number
# output: find mode(A^B, C)
# 05-22-2023

import sys


def divide(a, b, c):
    if b > 1:
        x = divide(a, b//2, c)
        if b % 2 == 0:
            return (x*x) % c
        else:
            return (a*x*x) % c

    else:
        return a % c


def problem1629():
    a, b, c = map(int, input().split())
    print(divide(a, b, c))


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    problem1629()
