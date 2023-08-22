n = int(input())

intArray = []
for i in range(0, n):
    num = int(input())
    if i == 0:
        intArray.append(num)
    else:
        for j in range(0, len(intArray)):
            if intArray[j] > num:
                break
            elif intArray[j] <= num and j == len(intArray)-1:
                j = j+1
        intArray.insert(j, num)

for i in range(0, n):
    print(intArray[i])