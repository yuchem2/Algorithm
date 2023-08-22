from platform import java_ver
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
intArray = []
avg = 0
for i in range(0, n):
    num = int(input())
    avg += num
    intArray.append(num)

intArray.sort()
avg = round(avg / n)

i = n-1
preCount = 0
preNum = 0
beforeCount = 0
beforeNum = 0
while i>-1:
    j = i
    while j > -1 and intArray[i] == intArray[j]:
        j -= 1
    if i - j >= preCount:
        beforeCount = preCount
        beforeNum = preNum
        preCount = i - j
        preNum = intArray[i]
    if i == j:
        i = i -1
    else: 
        i = j



print(str(avg) + "\n")
print(str(intArray[n//2])+"\n")
if preCount == beforeCount:
    print(str(beforeNum) + "\n")
else:
    print(str(preNum)+ "\n")
print(str(intArray[n-1]-intArray[0])+"\n")