import sys

input = sys.stdin.readline
print = sys.stdout.write

cardNum, maxNum = map(int, input().split())
cardList = list(map(int, input().split()))

cardList.sort(reverse = True)

maxResult = 0
for i in range(0, cardNum-2):
    for j in range(i+1, cardNum-1):
        for k in range(j+1, cardNum):
            cntResult = cardList[i] + cardList[j] + cardList[k]
            if cntResult == maxNum:
                maxResult = cntResult
                break
            elif cntResult < maxNum and cntResult > maxResult:
                maxResult = cntResult

print(str(maxResult) + "\n")