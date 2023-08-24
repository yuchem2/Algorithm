from collections import deque


def problem1697():
    n, k = map(int, input().split())
    visited = [0]*100001
    queue = deque([n])
    while queue:
        u = queue.popleft()
        if u == k:
            break
        for next in (u-1, u+1, 2*u):
            if 0 <= next < 100001 and not visited[next]:
                queue.append(next)
                visited[next] = visited[u] + 1

    print(visited[k])


problem1697()
