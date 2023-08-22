import sys


def problem2293():
    n, k = map(int, input().split())
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    dp = [0]*(k+1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], k+1):
            dp[j] = dp[j] + dp[j-coins[i]]
    print(dp[-1])


problem2293()
