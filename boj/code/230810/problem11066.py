import sys


def merge():
    num = int(sys.stdin.readline())
    array = tuple(map(int, sys.stdin.readline().split()))
    cumulative = [0]*(num+1)
    dp = [[0]*num for _ in range(num)]
    m_dp = [[0]*num for _ in range(num)]

    cumulative[1] = array[0]
    for i in range(2, num + 1):
        cumulative[i] = cumulative[i-1] + array[i-1]
        m_dp[i-1][i-1] = i-1

    for d in range(1, num):
        for i in range(0, num-d):
            j = i+d
            dp[i][j] = sys.maxsize
            for m in range(m_dp[i][j-1], m_dp[j][j]):
                cost = dp[i][m] + dp[m+1][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    m_dp[i][j] = m
            dp[i][j] += cumulative[j+1] - cumulative[i]

    print(str(dp[0][num-1]))


def problem11066():
    test = int(input())
    for _ in range(test):
        merge()


problem11066()
