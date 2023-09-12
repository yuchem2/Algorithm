import sys
sys.setrecursionlimit(10**6)


def problem1967(x, c):
    global max_d, max_node

    visited[x] = 1
    if max_d < c:
        max_node, max_d = x, c

    for v in adj[x]:
        if visited[v[0]] == 0:
            problem1967(v[0], v[1]+c)


v_num = int(input())
adj = [[] for _ in range(v_num)]
for i in range(v_num-1):
    parent, child, w = map(int, sys.stdin.readline().split())
    adj[parent-1].append((child-1, w))
    adj[child-1].append((parent-1, w))

max_d, max_node = -1, -1
visited = [0]*v_num
problem1967(0, 0)

for i in range(v_num):
    visited[i] = 0
problem1967(max_node, 0)
print(max_d)
