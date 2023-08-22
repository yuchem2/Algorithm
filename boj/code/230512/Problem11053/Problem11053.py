# baekjoon Problem11053
# input:
# output:
# 2023-05-12

num = int(input())
inArray = list(map(int, input().split()))

inArray.insert(0, 0)
dp = [1] * (num+1)

for i in range(1, num+1):
    for j in range(1, i):
        if inArray[i] > inArray[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp[1:]))

d = [[0], [0]]
for i in range(1, num+1):
    if inArray[i] > d[1][-1]:
        d[0].append(d[0][-1]+1)
        d[1].append(inArray[i])
    elif inArray[i] < d[1][-1]:
        j = 0
        while j < len(d[1]):
            if inArray[i] > d[1][j]:
                j += 1
            elif inArray[i] == d[1][j]:
                break
            else:
                d[1][j] = inArray[i]
                break

print(d[0][-1])