# baekjoon Problem2110
# 06-01-2023
import sys


def problem2110():
    n, c = map(int, input().split())
    position = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    position.sort()
    l, r = 1, position[-1]//(c-1)

    while l <= r:
        m = (l+r)//2
        cnt, before = 1, position[0]
        for i in range(1, n):
            if before + m <= position[i]:
                cnt += 1
                before = position[i]
        if cnt >= c:
            l = m + 1
        else:
            r = m - 1

    print(r)


if __name__ == '__main__':
    problem2110()
