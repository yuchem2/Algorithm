import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
k = 10000
intArray = [0 for i in range(0, k)]

for i in range(0, n):
    num = int(input())
    intArray[num-1] += 1

for i in range(0, k):
    while intArray[i] > 0:
        print(str(i+1)+"\n")
        intArray[i] -= 1