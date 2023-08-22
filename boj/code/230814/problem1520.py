import sys
sys.setrecursionlimit(10**6)


def problem1520(x, y):
    global dp
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(grap) and 0 <= ny < len(grap[0]):
                if grap[x][y] > grap[nx][ny]:
                    dp[x][y] += problem1520(nx, ny)
    return dp[x][y]


m, n = map(int, input().split())
grap = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

print(problem1520(0, 0))
