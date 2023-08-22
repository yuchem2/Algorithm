x = input()
n, k = x.split()
x = input()
strArray = x.split()

intArray = []
for num in strArray:
    intArray.append(int(num))

intArray.sort(reverse=True)

print(intArray[int(k)-1])