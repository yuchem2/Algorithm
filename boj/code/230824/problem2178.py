import sys
input = sys.stdin.readline


def problem2178():
    n, m = map(int, input().split())
    array = [list(input().rstrip()) for _ in range(n)]
    predecessor = [[0]*m for _ in range(n)]
    queue = [[0, 0]]
    array[0][0], predecessor[0][0] = '2', 1
    possible = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while queue:
        u = queue.pop(0)
        for x, y in possible:
            dx, dy = u[0] + x, u[1] + y
            if 0 <= dx < n and 0 <= dy < m:
                if array[dx][dy] == '1':
                    queue.append([dx, dy])
                    array[dx][dy] = '2'
                    predecessor[dx][dy] = predecessor[u[0]][u[1]] + 1

    print(predecessor[n-1][m-1])


problem2178()
