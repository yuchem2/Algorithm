import sys
sys.setrecursionlimit(10**6)


def problem4803(n, m, t):
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)

    visited = [0]*n

    def dfs(x, parent):
        visited[x] = 1
        for i in edges[x]:
            if visited[i] == 0:
                if dfs(i, x):
                    return True
            elif parent != i:
                return True
        return False

    sys.stdout.write('Case {}: '.format(t))
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            if not dfs(i, -1):
                cnt += 1

    if cnt == 0:
        sys.stdout.write(out_strings[0])
    elif cnt == 1:
        sys.stdout.write(out_strings[1])
    else:
        sys.stdout.write(out_strings[2].format(cnt))


out_strings = ['No trees.\n', 'There is one tree.\n', 'A forest of {} trees.\n']
t = 1
n, m = map(int, sys.stdin.readline().split())
while not (n == 0 and m == 0):
    problem4803(n, m, t)
    t += 1
    n, m = map(int, sys.stdin.readline().split())
