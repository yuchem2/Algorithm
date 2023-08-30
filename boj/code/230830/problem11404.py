import sys


def problem11404():
    n, m = int(sys.stdin.readline()), int(sys.stdin.readline())
    INF = 123456789
    distance = [[INF]*n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        if distance[u-1][v-1] > w:
            distance[u-1][v-1] = w

    for waypoint in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    distance[i][j] = min(distance[i][j], distance[i][waypoint] + distance[waypoint][j])

    for i in range(n):
        for j in range(n):
            if distance[i][j] == INF:
                sys.stdout.write("0 ")
            else:
                sys.stdout.write(str(distance[i][j])+" ")
        sys.stdout.write("\n")


problem11404()
