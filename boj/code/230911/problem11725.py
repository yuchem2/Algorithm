import sys
from collections import deque


def problem11725():
    n = int(input())
    tree = [0]*n
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        v1, v2 = map(int, sys.stdin.readline().split())
        adj[v2-1].append(v1-1)
        adj[v1-1].append(v2-1)

    queue = deque([0])
    while queue:
        v1 = queue.popleft()
        for v2 in adj[v1]:
            if tree[v2] == 0:
                tree[v2] = v1+1
                queue.append(v2)

    for i in range(1, n):
        sys.stdout.write(str(tree[i])+"\n")


problem11725()
