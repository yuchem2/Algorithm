import sys
from collections import deque


def problem9019():
    st, ed = map(int, sys.stdin.readline().split())
    limit = 10000
    visited = [-1]*limit
    before = ['']*limit
    visited[st] = -2
    queue = deque([st])

    while queue:
        u = queue.popleft()
        if u == ed:
            break

        arg1 = (2*u) % limit
        arg2 = 9999 if u == 0 else u-1
        arg3 = (u % 1000) * 10 + u // 1000
        arg4 = (u % 10) * 1000 + u // 10

        if visited[arg1] == -1:
            queue.append(arg1)
            visited[arg1] = u
            before[arg1] = 'D'
        if visited[arg2] == -1:
            queue.append(arg2)
            visited[arg2] = u
            before[arg2] = 'S'
        if visited[arg3] == -1:
            queue.append(arg3)
            visited[arg3] = u
            before[arg3] = 'L'
        if visited[arg4] == -1:
            queue.append(arg4)
            visited[arg4] = u
            before[arg4] = 'R'

    buff = visited[ed]
    stack = [before[ed]]

    while buff != -2:
        stack.append(before[buff])
        buff = visited[buff]
    while stack:
        sys.stdout.write(stack.pop())
    sys.stdout.write('\n')


t = int(input())
for _ in range(t):
    problem9019()
