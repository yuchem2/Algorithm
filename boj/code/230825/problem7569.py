import sys
from collections import deque


def problem7569():
    m, n, h = map(int, input().split())
    board = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
    promise = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [1, 0, 0], [-1, 0, 0]]
    queue = deque()

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if board[k][i][j] == 1:
                    queue.append([k, i, j])

    cnt = 0
    while queue:
        u = queue.popleft()
        cnt = board[u[0]][u[1]][u[2]]
        for z, x, y in promise:
            dz, dx, dy = u[0]+z, u[1]+x, u[2]+y
            if 0 <= dz < h and 0 <= dx < n and 0 <= dy < m:
                if board[dz][dx][dy] == 0:
                    queue.append([dz, dx, dy])
                    board[dz][dx][dy] = cnt + 1
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if board[k][i][j] == 0:
                    print(-1)
                    return

    print(cnt-1)


problem7569()
