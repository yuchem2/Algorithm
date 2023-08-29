import sys
from queue import PriorityQueue


def problem1753():
    v_num, e_num = map(int, input().split())
    st = int(input())
    edges = [{} for _ in range(v_num)]
    for _ in range(e_num):
        u, v, w = map(int, sys.stdin.readline().split())
        if v-1 in edges[u-1] and edges[u-1][v-1] <=w:
            continue
        edges[u-1][v-1] = w

    result = [123456789]*v_num
    visited = [0] * v_num
    result[st-1] = 0
    que = PriorityQueue()
    que.put((result[st-1], st-1))

    while que.qsize() > 0:
        u = que.get()
        visited[u[1]] = 1
        for v in edges[u[1]]:
            if visited[v] == 0:
                w = u[0] + edges[u[1]][v]
                if result[v] > w:
                    result[v] = w
                    que.put((result[v], v))

    for r in result:
        if r == 123456789:
            sys.stdout.write("INF\n")
        else:
            sys.stdout.write(str(r)+"\n")


problem1753()
