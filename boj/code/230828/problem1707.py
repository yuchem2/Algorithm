import sys
from collections import deque


def problem1707():
    v_num, e_num = map(int, sys.stdin.readline().split())
    edges = [{} for _ in range(v_num)]
    for _ in range(e_num):
        st, ed = map(int, sys.stdin.readline().split())
        edges[st-1][ed-1], edges[ed-1][st-1] = 1, 1

    vertices = [0]*v_num
    vertices[0] = 1
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for e in edges[u]:
            if vertices[e] == 0:
                vertices[e] = vertices[u] * -1
                queue.append(e)
            elif vertices[e] == vertices[u]:
                sys.stdout.write("NO\n")
                return
        if not queue:
            for i in range(v_num):
                if vertices[i] == 0:
                    vertices[i] = 1
                    queue.append(i)
                    break

    sys.stdout.write("YES\n")


t = int(input())
for _ in range(t):
    problem1707()
