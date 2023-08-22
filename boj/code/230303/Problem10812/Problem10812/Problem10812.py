

FInput = input()
boxNum, rotationNum = FInput.split()
boxNum = int(boxNum)
rotationNum = int(rotationNum)

boxArray = []
for i in range(1, boxNum+1):
    boxArray.append(i)

for _ in range(0, rotationNum):
    inStr = input()
    begin, end, mid = inStr.split()
    bufferArray1 = boxArray[int(begin)-1:int(mid)-1]
    bufferArray2 = boxArray[int(mid)-1:int(end)]
    boxArray = boxArray[:int(begin)-1] + bufferArray2 + bufferArray1 + boxArray[int(end):]

for i in boxArray:
    print(i, end = " ")
print()