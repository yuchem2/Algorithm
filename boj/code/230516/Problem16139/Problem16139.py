# baekjoon Problem16139
# input: string, interval, character
# output: maximum sum of character
# 05-16-2023

import sys

inStr = input()
num = int(input())

sums = [[0]*(26)]
for i in range(1, len(inStr)+1):
    sums.append(sums[-1][:])
    sums[i][ord(inStr[i-1]) -97] += 1

for i in range(num):
    x, st, end = list(sys.stdin.readline().split())
    x = ord(x)-97
    sys.stdout.write(str(sums[int(end)+1][x] - sums[int(st)][x])+"\n")