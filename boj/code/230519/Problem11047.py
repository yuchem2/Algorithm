# baekjoon Problem11047
# input: value of coins
# output: minimum number of coins
# 05-19-2023

import sys

def greedy(a, k):
    cnt = 0
    idx = len(a)-1
    while k > 0:
        if k//a[idx] > 0:
            quotient = k//a[idx]
            k = k - a[idx] * quotient
            cnt += quotient
        idx -= 1
    return cnt

def problem11047():
    n, k = map(int, input().split())

    values = [0]*n
    for i in range(n):
        values[i] = int(sys.stdin.readline().rstrip())

    print(greedy(values, k))


problem11047()