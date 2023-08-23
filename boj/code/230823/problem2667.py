import sys


def problem2667():
    n = int(input())
    array = [sys.stdin.readline().rstrip() for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    result = []
    possible = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and array[i][j] == '1':
                queue = [[i, j]]
                count = 0
                while queue:
                    u = queue.pop(0)
                    visited[u[0]][u[1]] = 1
                    count += 1
                    for x, y in possible:
                        dx = u[0] + x
                        dy = u[1] + y
                        if 0 <= dx < n and 0 <= dy < n:
                            if visited[dx][dy] == 0:
                                if array[dx][dy] == '1':
                                    queue.append([dx, dy])
                                visited[dx][dy] = 1
                result.append(count)
            else:
                visited[i][j] = 1
    print(len(result))
    result.sort()
    for r in result:
        sys.stdout.write(str(r)+"\n")


problem2667()
