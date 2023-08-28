import sys
from collections import deque


def problem2206():
    n, m = map(int, input().split())
    array = [sys.stdin.readline().rstrip() for _ in range(n)]
    check = [[[0]*m for _ in range(n)] for _ in range(2)]
    possible = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue = deque([[0, 0, 0]])
    check[0][0][0] = check[1][0][0] = 1
    while queue:
        u = queue.popleft()
        count = check[u[0]][u[1]][u[2]] + 1
        if u[1:] == [n-1, m-1]:
            print(count-1)
            return
        for x, y in possible:
            dx, dy = u[1] + x, u[2] + y
            if 0 <= dx < n and 0 <= dy < m:
                if u[0] == 0 and array[dx][dy] == '1' and check[1][dx][dy] == 0:
                    queue.append([1, dx, dy])
                    check[1][dx][dy] = count
                elif array[dx][dy] == '0' and check[u[0]][dx][dy] == 0:
                    queue.append([u[0], dx, dy])
                    check[u[0]][dx][dy] = count

    print(-1)


problem2206()
