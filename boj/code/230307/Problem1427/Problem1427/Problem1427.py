
inStr = input()

counterArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
outArray = [0 for x in range(len(inStr))]
for x in inStr:
    counterArray[int(x)] += 1

for i in range(len(counterArray)-2, -1, -1):
    counterArray[i] = counterArray[i] + counterArray[i+1]

for i in range(len(outArray)-1, -1, -1):
    outArray[counterArray[int(inStr[i])]-1] = int(inStr[i])
    counterArray[int(inStr[i])] -= 1

for i in outArray:
    print(i, end="")
print()
