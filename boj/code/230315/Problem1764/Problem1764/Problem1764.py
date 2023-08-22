## baekjoon Problem1764
## input: known string and problem string
## output: unkown string
## 2023-03-15

import sys
input = sys.stdin.readline
print = sys.stdout.write

peopleNum, problemNum = map(int, input().strip("\n").split())

peopleList = {}
for i in range(peopleNum):
    peopleList[input().strip("\n")] = 1

problemList = []
for i in range(problemNum):
    problemList.append(input().strip("\n"))

resultList = []
for problem in problemList:
    if problem in peopleList:
        resultList.append(problem)

resultList.sort()
print(str(len(resultList)) + "\n")
for result in resultList:
    print(result + "\n")