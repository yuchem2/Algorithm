import sys

input = sys.stdin.readline
print = sys.stdout.write

inNum = int(input())

numLen = len(str(inNum))
stNum = inNum - (inNum // (10 ** (numLen - 1)) + 9 * (numLen-1))

ctorNum = 0
for i in range(stNum, inNum+1):
    calculateNum = i + sum(list(map(int, str(i))))
    if calculateNum == inNum:
        ctorNum = i
        break

print(str(ctorNum))