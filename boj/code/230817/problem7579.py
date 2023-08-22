def problem7579():
    n, m = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    sums_cost = sum(costs)
    dp = [[0]*(sums_cost+1) for _ in range(n)]
    for i in range(n):
        for j in range(sums_cost+1):
            if j >= costs[i]:
                dp[i][j] = max(dp[i-1][j-costs[i]] + memories[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    for i in range(sums_cost+1):
        if dp[-1][i] >= m:
            print(i)
            break


problem7579()
