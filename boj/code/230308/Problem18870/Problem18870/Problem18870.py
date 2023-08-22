
inNum = int(input())
dotList = list(map(int, input().strip('\n').split()))
buffer = dotList.copy()
buffer.sort()
dotDic = {buffer[i]: i for i in range(len(buffer))}


for dot in dotList:
    print(str(dotDic[dot]) + " ")