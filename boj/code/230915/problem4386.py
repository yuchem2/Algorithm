import sys
import math
from heapq import heappop, heappush


def problem4386():
    n = int(input())
    stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

    visited = [0]*n
    que = [(0, 0)]
    cost = 0.0
    while que:
        u = heappop(que)
        if visited[u[1]] == 1:
            continue
        visited[u[1]] = 1
        cost += u[0]
        for i in range(n):
            if i != u[1] and visited[i] == 0:
                heappush(que, (math.dist(stars[u[1]], stars[i]), i))

    print("%.2f" % cost)


problem4386()
