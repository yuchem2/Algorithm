import sys
from collections import deque


def problem16928():
    n, m = map(int, input().split())
    board = {}
    visited = [101]*101

    for _ in range(n+m):
        st, ed = map(int, sys.stdin.readline().split())
        board[st] = ed

    queue = deque([1])
    visited[1] = 0
    while queue:
        u = queue.popleft()
        if u == 100:
            break

        for x in range(1, 7):
            dx = u + x
            if dx < 101 and visited[dx] == 101:
                while dx in board:
                    if visited[dx] > visited[u] + 1:
                        visited[dx] = visited[u] + 1
                    dx = board[dx]
                if visited[dx] == 101:
                    visited[dx] = visited[u] + 1
                    queue.append(dx)

    print(visited[-1])


problem16928()
