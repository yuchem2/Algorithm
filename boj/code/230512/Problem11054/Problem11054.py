# baekjoon Problem11053
# input: integer sequential
# output: Longest Bitonic sequential
# 2023-05-12

num = int(input())
array = list(map(int, input().split()))

l_dp = [1] * num
r_dp = [1] * num
dp = [0] * num

for i in range(num):
    for j in range(i):
        if array[i] > array[j]:
            l_dp[i] = max(l_dp[i], l_dp[j]+1)

for i in range(num-1, -1, -1):
    for j in range(i+1, num):
        if array[i] > array[j]:
            r_dp[i] = max(r_dp[i], r_dp[j]+1)

print(l_dp, r_dp)
for i in range(num):
    dp[i] = max(r_dp[i] + l_dp[i], dp[i])

print(max(dp)-1)

l_dp = [1] * num
r_dp = [1] * num
l_d = [[0], [0]]
r_d = [[0], [0]]
dp = [0] * num


def find(x, i, dp, d):
    if x[i] > d[1][-1]:
        dp[i] = d[0][-1]+1
        d[0].append(dp[i])
        d[1].append(x[i])
    elif array[i] == d[1][-1]:
        dp[i] = d[0][-1]
    else:
        j = 0
        while j < len(d[1]):
            if x[i] > d[1][j]:
                j += 1
            elif x[i] == d[1][j]:
                dp[i] = d[0][j]
                break
            else:
                d[1][j] = x[i]
                dp[i] = d[0][j]
                break

for i in range(0, num):
    find(array, i, l_dp, l_d)
for i in range(num-1, -1, -1):
    find(array, i, r_dp, r_d)
for i in range(num):
    dp[i] = max(r_dp[i] + l_dp[i], dp[i])
print(l_dp, r_dp)
print(max(dp)-1)