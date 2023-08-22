# baekjoon Problem9461
# input: test cases
# output: Padovan sequence result of test cases
# 2023-04-04 00:45-00:58
import sys
input = sys.stdin.readline

testNum = int(input().rstrip())
padovanSequence = [1, 1, 1, 2, 2] + [0]*95
resultList = [0]*testNum

for i in range(testNum):
    n = int(input().rstrip())
    for j in range(5, n):
        padovanSequence[j] = padovanSequence[j-1] + padovanSequence[j-5]
    resultList[i] = padovanSequence[n-1]

for result in resultList:
    print(result)