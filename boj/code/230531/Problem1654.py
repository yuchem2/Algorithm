# baekjoon Problem1654
# 05-31-2023

import sys


def problem1654():
    k, n = map(int, input().split())
    array = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
    l, r = 1, max(array)

    while l <= r:
        m = (l+r)//2
        cnt = 0
        for i in range(k):
            cnt += (array[i]//m)
        if cnt >= n:
            l = m + 1
        else:
            r = m - 1
    print(r)


if __name__ == '__main__':
    problem1654()
