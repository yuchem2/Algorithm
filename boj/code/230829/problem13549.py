from queue import PriorityQueue
from collections import deque


# BFS
def problem13549_bfs():
    st, ed = map(int, input().split())
    time = [100000] * 100001

    time[st] = 0
    que = deque()
    que.append((time[st], st))

    while que:
        u = que.popleft()
        if u[1] == ed:
            break
        for w, v in [[0, 2 * u[1]], [1, u[1] + 1], [1, u[1] - 1]]:
            w += u[0]
            if 0 <= v < 100001 and time[v] > w:
                time[v] = w
                que.append((w, v))
    print(time[ed])


# Dijkstra
def problem13549():
    st, ed = map(int, input().split())
    time = [100000] * 100001

    time[st] = 0
    que = PriorityQueue()
    que.put((time[st], st))

    while not que.empty():
        u = que.get()
        if u[1] == ed:
            break
        for w, v in [[0, 2 * u[1]], [1, u[1] + 1], [1, u[1] - 1]]:
            w += u[0]
            if 0 <= v < 100001 and time[v] > w:
                time[v] = w
                que.put((w, v))

    print(time[ed])


problem13549()
