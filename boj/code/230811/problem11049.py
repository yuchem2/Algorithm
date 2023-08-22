import sys


def problem11049():
    num = int(input())
    cases = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
    dp = [[0]*num for _ in range(num)]

    for d in range(1, num):
        for i in range(0, num-d):
            j = i + d
            cost = cases[i][0]*cases[j][1]
            dp[i][j] = min(dp[i][m] + dp[m+1][j] + cases[m][1]*cost for m in range(i, j))

    print(dp[0][num-1])


problem11049()
