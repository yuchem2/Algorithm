import sys


def bfs(x):
    global count
    visited[x-1] = count
    queue = [x]
    while queue:
        u = queue.pop(0)
        for e in edges[u-1]:
            if visited[e-1] == 0:
                count += 1
                visited[e-1] = count
                queue.append(e)


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
bfs(r)
for v in visited:
    sys.stdout.write(str(v)+"\n")

