import sys
sys.setrecursionlimit(10**6)


def problem1167(i, w):
    visited[i] = 1
    global max_distance, max_node
    if w > max_distance:
        max_distance, max_node = w, i

    for u, c in adj[i]:
        if visited[u] == 0:
            problem1167(u, w+c)


v_num = int(input())
adj = [[] for _ in range(v_num)]
for _ in range(v_num):
    buff = list(map(int, sys.stdin.readline().split()))
    i = 1
    while buff[i] != -1:
        adj[buff[0]-1].append((buff[i]-1, buff[i+1]))
        i += 2
max_distance, max_node = -1, -1
visited = [0]*v_num
problem1167(0, 0)

max_distance = -1
for i in range(v_num):
    visited[i] = 0

problem1167(max_node, 0)
print(max_distance)
