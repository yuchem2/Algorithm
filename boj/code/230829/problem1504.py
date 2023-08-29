import sys
from queue import PriorityQueue


def dijkstra(st, ed):
    distance = [123456789]*v_num
    que = PriorityQueue()
    distance[st] = 0
    que.put((distance[st], st))

    while que.qsize() > 0:
        u = que.get()
        for v in edges[u[1]]:
            w = u[0] + edges[u[1]][v]
            if distance[v] > w:
                distance[v] = w
                que.put((distance[v], v))

    return distance


v_num, e_num = map(int, input().split())
edges = [{} for _ in range(v_num)]
for _ in range(e_num):
    u, v, w = map(int, sys.stdin.readline().split())
    edges[u-1][v-1] = edges[v-1][u-1] = w
v1, v2 = map(int, input().split())

a = dijkstra(0, v_num-1)
b = dijkstra(v1-1, v_num-1)
c = dijkstra(v2-1, v_num-1)
answer = min(a[v1-1] + b[v2-1] + c[v_num-1], a[v2-1] + b[v_num-1] + c[v1-1])
if answer >= 123456789:
    print(-1)
else:
    print(answer)
