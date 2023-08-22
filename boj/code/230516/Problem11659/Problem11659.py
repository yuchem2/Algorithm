# baekjoon Problem11659
# input: the length of sequence, sequence, and some intervals
# output: cumulative sum of each interval
# 05-16-2023

import sys

num, intervalNum = map(int, input().split())
sequence = list(map(int, input().split()))

intervals = [0]*intervalNum
for i in range(intervalNum):
    intervals[i] = list(map(int, sys.stdin.readline().strip().split()))

sequence.insert(0, 0)
for i in range(0, num+1):
    sequence[i] += sequence[i-1]

for i in range(intervalNum):
    sys.stdout.write(str(sequence[intervals[i][1]]-sequence[intervals[i][0]-1])+"\n")