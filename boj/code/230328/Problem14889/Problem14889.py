# baek joon Problem14889
# input: n, n xn array(4<=n<=20, n is even)
# output: 두 팀의 능력지 차
# 2023-03-29 01:05 - 02:24

def dfs(x, idx):
    if x == n // 2:
        global minDiff
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += statArray[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += statArray[i][j]
        minDiff = min(abs(team1 - team2), minDiff)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(x+1, i+1)
            visited[i] = False


n = int(input())
statArray = [list(map(int, input().split())) for _ in range(n)]
minDiff = 123456789
visited = [False]*n

dfs(0, 0)
print(minDiff)
