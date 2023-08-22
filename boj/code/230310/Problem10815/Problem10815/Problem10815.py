
cardNum = int(input())
cardList = list(map(int, input().split()))
intNum = int(input())
intList = list(map(int, input().split()))

#cardList.sort()

#mid = cardNum // 2
#for i in range(intNum):
#    l = 0
#    r = cardNum - 1
#    while l <= r:
#        m = (l + r) // 2
#        if intList[i] < cardList[m]:
#            r = m - 1
#        elif intList[i] > cardList[m]:
#            l = m + 1
#        else:
#            intList[i] = 1
#            break
#    if l > r:
#        intList[i] = 0

#for i in intList:
#    print(i, end = " ")


cardList = {x:0 for x in cardList}

for i in range(intNum):
    if intList[i] in cardList:
        intList[i] = 1
    else:
        intList[i] = 0

for i in intList:
    print(i, end = " ")