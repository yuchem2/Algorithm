import sys
from heapq import heappop, heappush


def problem1197():
    n, m = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        v1, v2, c = map(int, sys.stdin.readline().split())
        edges[v1-1].append([c, v2-1])
        edges[v2-1].append([c, v1-1])

    selected = [0]*n
    que = [(0, 0)]
    cost = 0
    while que:
        u = heappop(que)
        if selected[u[1]] == 1:
            continue
        cost += u[0]
        selected[u[1]] = 1
        for v in edges[u[1]]:
            if selected[v[1]] == 0:
                heappush(que, (v[0], v[1]))
    print(cost)


problem1197()
