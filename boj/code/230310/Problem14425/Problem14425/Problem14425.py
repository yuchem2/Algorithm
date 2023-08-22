import sys

input = sys.stdin.readline

strNum, checkStrNum = map(int, input().split())
strList = []
for i in range(strNum):
    strList.append(input().strip("\n"))

checkStrList = []
for i in range(checkStrNum):
    checkStrList.append(input().strip("\n"))

result = 0
for i in range(checkStrNum):
    if checkStrList[i] in strList:
        result += 1

print(result)