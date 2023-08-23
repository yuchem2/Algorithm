import sys
sys.setrecursionlimit(10**6)


def dfs(x):
    print(x, end=" ")
    visited[x-1] = 1
    for e in edges[x-1]:
        if visited[e-1] == 0:
            dfs(e)


def bfs(x):
    visited[x-1] = 1
    print(x, end=" ")
    queue = [x]
    while queue:
        u = queue.pop(0)

        for e in edges[u-1]:
            if visited[e-1] == 0:
                visited[e-1] = 1
                queue.append(e)
                print(e, end=" ")


n, m, v = map(int, input().split())
edges = [[] for _ in range(n)]
visited = [0]*n
for _ in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    edges[st-1].append(ed)
    edges[ed-1].append(st)

for e in edges:
    e.sort()

dfs(v)
print()
visited = [0]*n
bfs(v)
