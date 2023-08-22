# baekjoon Problem15652
# input: n, m (1<=M<=N<=8)
# output: 비 내림차순을 만족하는 수열(수열 내 중복 가능)
# 2023-03-22
# JaeHyun Yoon

import sys
print = sys.stdout.write

n, m = map(int, input().split())

s = []
def Dfs(n, m):
    if len(s) == m:
        print(' '.join(map(str, s)) + "\n")
        return

    for i in range(1, n+1):
        if len(s) == 0 or i >= s[-1]:
            s.append(i)
            Dfs(n, m)
            s.pop()

Dfs(n, m)