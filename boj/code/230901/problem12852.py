import sys


def problem12852():
    n = int(input())
    dp = [[int(1e6)+1, -1] for _ in range(n+1)]
    dp[1] = [0, -1]
    for u in range(1, n+1):
        c = dp[u][0]
        if u*3 <= n and dp[u*3][0] > c + 1:
            dp[u*3][0], dp[u*3][1] = c+1, u

        if u*2 <= n and dp[u*2][0] > c + 1:
            dp[u*2][0], dp[u*2][1] = c+1, u

        if u+1 <= n and dp[u+1][0] > c + 1:
            dp[u+1][0], dp[u+1][1] = c+1, u

    print(dp[n][0])
    i = n
    while i != -1:
        sys.stdout.write(str(i)+" ")
        i = dp[i][1]


problem12852()
