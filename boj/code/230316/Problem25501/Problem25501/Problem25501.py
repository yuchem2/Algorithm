## baekjoon Problem10872
## input: testcase palindrome string list
## output: return function ispalidrome and recursion call #
## 2023-03-16

import sys

def recursion(a, l, r):
    if l >= r:
        a[1] += 1
        return 1
    elif a[0][l] != a[0][r]:
        a[1] += 1 
        return 0
    else:
        a[1] += 1
        return recursion(a, l+1, r-1)

def isPalidrome(a):
    return recursion(a, 0, len(a[0])-1)

input = sys.stdin.readline
print = sys.stdout.write
testNum = int(input())

testList = []
for i in range(testNum):
    testList.append([input().strip("\n"), 0])

for i in range(testNum):
    testList[i][0] = isPalidrome(testList[i])

for i in range(testNum):
    print(str(testList[i][0]) + " " + str(testList[i][1]) + "\n")