import sys

input = sys.stdin.readline

humanNum = int(input())

weightList = []
statureList = []

for i in range(0, humanNum):
    weight, stature = map(int, input().split())
    weightList.append(weight)
    statureList.append(stature)

for w, s in zip(weightList, statureList):
    upperNum = 0
    for i, j in zip(weightList, statureList):
        if w < i and s < j:
            upperNum += 1
    print(upperNum+1, end = " ")

