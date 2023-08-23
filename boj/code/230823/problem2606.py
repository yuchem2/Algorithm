import sys


def dfs(x):
    visited[x-1] = 1
    for e in edges[x-1]:
        if visited[e-1] == 0:
            dfs(e)


n, m = int(input()), int(input())
edges = [[] for _ in range(n)]
visited = [0]*n
for _ in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    edges[st-1].append(ed)
    edges[ed-1].append(st)

dfs(1)
print(sum(visited)-1)

