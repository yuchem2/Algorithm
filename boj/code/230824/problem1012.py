import sys


input = sys.stdin.readline


def problem1012():
    m, n, k = map(int, input().split())
    array = [dict({}) for _ in range(m)]
    possible = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for _ in range(k):
        x, y = map(int, input().split())
        array[x][y] = 0
    count = 0
    for i in range(m):
        for j in array[i]:
            if array[i][j] == 0:
                queue = [[i, j]]
                array[i][j] = 1
                while queue:
                    u = queue.pop(0)
                    for x, y in possible:
                        dx, dy = x + u[0], y + u[1]
                        if 0 <= dx < m and 0 <= dy <= n:
                            if dy in array[dx]:
                                if array[dx][dy] == 0:
                                    queue.append([dx, dy])
                                array[dx][dy] = 1
                count += 1

    sys.stdout.write("{}\n".format(count))


t = int(input())
for _ in range(t):
    problem1012()
