# baekjoon Problem15649
# input: n, m(1 <= M <= N <= 8)
# output: 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 2023-03-20
import sys
print = sys.stdout.write

n, m = map(int, input().split())
naturalNumList = [x for x in range(1, n+1)]

# use stack
# if m == 1:
#     resultList = naturalNumList
#     for result in resultList:
#         print(str(result) + "\n")
# else:
#     naturalNumList.reverse()
#     # 수열의 경우의 수 n!/ (n-m)!
#     resultNum = n
#     for i in range(n-1, n-m, -1):
#         resultNum = resultNum * i
#
#     i = 1
#     resultList = []
#     while len(resultList) < resultNum:
#         stack = [[i, x] for x in naturalNumList]
#         result = [i]
#         stack.remove([i, i])
#         while stack:
#             result.append(stack.pop()[1])
#
#             # check collision
#             target = result[-1]
#             for j in range(0, len(result)-1):
#                 if target == result[j]:
#                     result.pop()
#                     break
#
#             if len(result) == m:
#                 resultList.append(result.copy())
#                 result.pop()
#                 while len(stack) != 0 and result[-1] != stack[-1][0]:
#                     result.pop()
#             else:
#                 for num in naturalNumList:
#                     if num not in result:
#                         stack.append([result[-1], num])
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
        if i not in s:
            s.append(i)
            Dfs(n, m)
            s.pop()

Dfs(n, m)
