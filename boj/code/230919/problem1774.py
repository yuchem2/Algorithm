import sys
import math
from heapq import heappop, heappush


def problem1774():
    n, m = map(int, sys.stdin.readline().split())
    targets = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    connect = [{} for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        connect[a-1][b-1] = 1
        connect[b-1][a-1] = 1

    adj = [[0]*n for _ in range(n)]

    visited = [0]*n
    que = []
    for i in range(n):
        for j in range(n):
            if j in connect[i] or i == j:
                continue
            else:
                adj[i][j] = math.dist(targets[i], targets[j])

    heappush(que, (0, 0))
    cost = 0.0
    while que:
        nxt = heappop(que)
        if visited[nxt[1]] == 1:
            continue
        visited[nxt[1]] = 1
        cost += nxt[0]

        for i in range(n):
            if visited[i] == 0:
                heappush(que, (adj[nxt[1]][i], i))

    print("%.2f" % cost)


problem1774()
