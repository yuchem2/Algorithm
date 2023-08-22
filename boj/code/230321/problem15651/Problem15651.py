# baekjoon Problem15651
# input: n, m(1 <= M <= N <= 7)
# output: 1부터 N까지 자연수 중에서 중복 있이 고른 수열(n^m)
# 2023-03-21

import sys
print = sys.stdout.write
s = []

def Dfs(n, m):
    if len(s) == m:
        print(' '.join(map(str, s)) + "\n")
        return

    for i in range(1, n+1):
        s.append(i)
        Dfs(n, m)
        s.pop()


n, m = map(int, input().split())
Dfs(n, m)