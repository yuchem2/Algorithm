import sys


def problem1956():
    n, m = map(int, sys.stdin.readline().split())
    INF = float('inf')
    distance = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        distance[u - 1][v - 1] = w

    for waypoint in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][waypoint] + distance[waypoint][j]:
                    distance[i][j] = distance[i][waypoint] + distance[waypoint][j]

    result = INF
    for i in range(n):
        result = min(result, distance[i][i])
    print(result if result != INF else -1)


problem1956()
