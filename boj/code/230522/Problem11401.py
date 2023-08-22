# baekjoon Problem11401
# input: natural number and integer number
# output: find the number of -0, 1, 1 squares
# 05-22-2023

import sys


def factorial(n):
    global divisor
    result = 1
    for i in range(2, n+1):
        result = (result*i) % divisor
    return result


def square(n, k):
    global divisor
    if k == 0:
        return 1
    elif k == 1:
        return n

    buff = square(n, k//2)
    if k % 2:
        return (buff * buff * n) % divisor
    else:
        return (buff * buff) % divisor


def problem11401():
    n, k = map(int, input().split())
    top = factorial(n)
    bottom = (factorial(n-k)*factorial(k)) % divisor
    print(top*square(bottom, divisor-2) % divisor)


if __name__ == '__main__':
    divisor = 1000000007
    sys.setrecursionlimit(10**6)
    problem11401()
