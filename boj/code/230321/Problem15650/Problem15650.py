# baekjoon Problem15650
# input: n, m(1 <= M <= N <= 8)
# output: 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열(nCr)
# 2023-03-21

import sys
print = sys.stdout.write

n, m = map(int, input().split())
naturalNumList = [x for x in range(1, n+1)]

# use stack
# if m == 1:
#     for num in naturalNumList:
#         print(str(num) + "\n")
# elif n == m:
#     print(' '.join([str(x) for x in naturalNumList]))
# else:
#     naturalNumList.reverse()
#
#     i = 1
#     resultList = []
#     while i <= n-m+1:
#         result = [i]
#         stack = []
#         for num in naturalNumList:
#             if num > i:
#                 stack.append([i, num])
#         while stack:
#             result.append(stack.pop()[1])
#
#             if len(result) == m:
#                 if result not in resultList:
#                     resultList.append(result.copy())
#                 result.pop()
#                 while len(stack) != 0 and result[-1] != stack[-1][0]:
#                     result.pop()
#             else:
#                 if result[-1] == n:
#                     result.pop()
#                     result.pop()
#                 else:
#                     for num in naturalNumList:
#                         if num > result[-1]:
#                             stack.append([result[-1], num])
#                         else:
#                             break
#         i += 1
#
#     for result in resultList:
#         print(' '.join(str(x) for x in result) + "\n")


# use recursion function
s = []
def Dfs(n, m):
    if len(s) == m:
        print(' '.join(map(str, s)) + "\n")
        return
    for i in range(1, n+1):
        if len(s) == 0 or i > s[-1]:
            s.append(i)
            Dfs(n, m)
            s.pop()

Dfs(n, m)

