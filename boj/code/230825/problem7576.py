import sys
from collections import deque


def problem7576():
    m, n = map(int, input().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    promise = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append([i, j])

    cnt = 0
    while queue:
        u = queue.popleft()
        cnt = board[u[0]][u[1]]
        for x, y in promise:
            dx, dy = u[0]+x, u[1]+y
            if 0 <= dx < n and 0 <= dy < m:
                if board[dx][dy] == 0:
                    queue.append([dx, dy])
                    board[dx][dy] = cnt + 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print(-1)
                return

    print(cnt-1)


problem7576()
