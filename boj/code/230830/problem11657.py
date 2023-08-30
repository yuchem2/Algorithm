import sys


def problem11657():
    n, m = map(int, sys.stdin.readline().split())
    bus = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    time = [123456789]*n
    time[0] = 0

    for i in range(n):
        for u, v, w in bus:
            if time[u-1] != 123456789 and time[v-1] > time[u-1] + w:
                if i == n-1:
                    print(-1)
                    return
                time[v-1] = time[u-1] + w

    for t in time[1:]:
        if t == 123456789:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(t)+"\n")


problem11657()
