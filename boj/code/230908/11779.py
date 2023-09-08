import sys
from heapq import heappop, heappush
read = sys.stdin.readline


def problem11779():
    v_num, e_num = int(read()), int(read())
    edges = [{} for _ in range(v_num)]
    for _ in range(e_num):
        st, ed, c = map(int, read().split())
        if ed-1 not in edges[st-1] or edges[st-1][ed-1] > c:
            edges[st-1][ed-1] = c

    st, ed = map(int, read().split())

    distance = [int(1e8)]*v_num
    path = [-1]*v_num
    distance[st-1], path[st-1] = 0, st-1
    queue = []
    heappush(queue, (distance[st-1], st-1))

    while queue:
        u = heappop(queue)
        if u[0] > distance[u[1]]:
            continue

        for v in edges[u[1]]:
            w = u[0] + edges[u[1]][v]
            if distance[v] > w:
                distance[v] = w
                path[v] = u[1]
                heappush(queue, (w, v))
            elif distance[v] == w:
                path[v] = u[1]

    print(distance[ed-1])

    buff = ed-1
    stack = [ed]
    while buff != st-1:
        buff = path[buff]
        stack.append(buff + 1)

    print(len(stack))
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=" ")


problem11779()
