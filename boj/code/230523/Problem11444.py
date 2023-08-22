# baekjoon Problem11444
# input: 2D array
# output: A^B (A is matrix)
# 05-23-2023
import copy


def multi(a, b, i, j, m):
    result = 0
    for k in range(m):
        result += ((a[i][k]*b[k][j]) % divisor)
    return result % divisor


def matrix_multi(a, b):
    c = copy.deepcopy(a)
    for i in range(len(a[0])):
        for j in range(len(b)):
            c[i][j] = multi(a, b, i, j, len(b[0]))
    return c


def square(a, b):
    if b > 1:
        x = square(a, b//2)
        if b % 2 == 0:
            return matrix_multi(x, x)
        else:
            return matrix_multi(a, matrix_multi(x, x))
    else:
        return a


def fib(n):
    array = [[1, 1], [1, 0]]
    return square(array, n)


def problem11444():
    n = int(input())
    print(fib(n)[0][1]%divisor)


if __name__ == '__main__':
    divisor = 1000000007
    problem11444()
