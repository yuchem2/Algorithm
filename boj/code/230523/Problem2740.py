# baekjoon Problem2740
# input: two 2D array
# output: AxB
# 05-23-2023
import sys


def multi(a, b, i, j, m):
    result = 0
    for k in range(m):
        result += (a[i][k]*b[k][j])
    return result


def problem2740():
    n, m = map(int, input().split())
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    m, k = map(int, input().split())
    b = [list(map(int, sys.stdin.readline().split())) for i in range(m)]

    for i in range(n):
        for j in range(k):
            sys.stdout.write(str(multi(a, b, i, j, m)) + " ")
        sys.stdout.write("\n")


if __name__ == '__main__':
    problem2740()
