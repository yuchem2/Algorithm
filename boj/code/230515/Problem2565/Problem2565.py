# baekjoon Problem2565
# input: electric wire case
# output: estimate minimum number of the electric wire
# 2023-05-15


num = int(input())
wireCase = [[0, 0] for x in range(num)]
for i in range(num):
    wireCase[i] = list(map(int, input().split()))

wireCase.sort()
dp = [1] * num
for i in range(num):
    for j in range(i):
        if wireCase[i][1] > wireCase[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(num-max(dp))