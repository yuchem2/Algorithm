import sys
sys.setrecursionlimit(10**6)


def dfs(x):
    global count
    visited[x-1] = count
    count += 1
    for e in edges[x-1]:
        if visited[e-1] == 0:
            dfs(e)


n, m, r = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    edges[st-1].append(ed)
    edges[ed-1].append(st)

for e in edges:
    e.sort(reverse=True)

visited = [0]*n
count = 1
dfs(r)
for v in visited:
    sys.stdout.write(str(v)+"\n")
