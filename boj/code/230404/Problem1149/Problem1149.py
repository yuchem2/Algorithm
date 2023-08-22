# baekjoon Problem 1149
# input: n개의 집과 그 집을 RGB로 칠하는 비용
# output: RGB로 집을 칠하는 최소 비용
# 2023-04-04 21:16


houseNum = int(input())

costRGB = [0]*houseNum
for i in range(houseNum):
    costRGB[i] = list(map(int, input().split()))

resultArray = [[0, 0, 0] for _ in range(houseNum)]
resultArray[0] = costRGB[0]
for i in range(1, houseNum):
    resultArray[i][0] = min(resultArray[i-1][1], resultArray[i-1][2]) + costRGB[i][0]
    resultArray[i][1] = min(resultArray[i - 1][0], resultArray[i - 1][2]) + costRGB[i][1]
    resultArray[i][2] = min(resultArray[i - 1][0], resultArray[i - 1][1]) + costRGB[i][2]

print(min(resultArray[-1][0], resultArray[-1][1], resultArray[-1][2]))