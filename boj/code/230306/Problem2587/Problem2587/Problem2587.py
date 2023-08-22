n = 5
intArray = []
avg = 0
for i in range(0, n):
    num = int(input())
    intArray.append(num)
    avg = avg + num

intArray.sort()
avg = int(avg/5)

print(avg)
print(intArray[2])