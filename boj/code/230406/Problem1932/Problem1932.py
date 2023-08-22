# baekjoon Problem1932
# input: integer triangle
# output: max sum
# 2023-04

n = int(input())
triArray = [0]*n
for i in range(n):
    triArray[i] = list(map(int, input().split()))
for height in range(1, n):
    for i in range(0, len(triArray[height])):
        if i == 0:
            triArray[height][i] += triArray[height-1][i]
        elif i == len(triArray[height]) - 1:
            triArray[height][i] += triArray[height-1][i-1]
        else:
            triArray[height][i] += max(triArray[height-1][i], triArray[height-1][i-1])
print(max(triArray[n-1]))