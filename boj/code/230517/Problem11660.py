# baekjoon Problem11660
# input: 2D array
# output: cumulative sum
# 05-17-2023

import sys

features, num = map(int, input().split())
array = [0]*(features+1)
array[0] = [0]*(features+1)
for i in range(features):
    array[i+1] = list(map(int, sys.stdin.readline().split()))
    array[i+1].insert(0, 0)

for i in range(1, features+1):
    for j in range(1, features+1):
        array[i][j] += (array[i-1][j] + array[i][j-1]-array[i-1][j-1])

for i in range(num):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = array[x2][y2] - array[x2][y1-1] - array[x1-1][y2] + array[x1-1][y1-1]
    sys.stdout.write(str(result)+"\n")