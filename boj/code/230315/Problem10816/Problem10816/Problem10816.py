## baekJoon Problem10816
## 2023-03-15

cardNum = int(input())
cardList = list(map(int, input().split()))
problemNum = int(input())
problemList = list(map(int, input().split()))

cardList.sort()

problemDic = {problemList[i]: 0 for i in range(problemNum)}
for i in range(cardNum):
    if cardList[i] in problemDic.keys():
        problemDic[cardList[i]] += 1


for i in range(problemNum):
    print(problemDic[problemList[i]], end=" ")