## baekjoon Problem1269
## input: 자연수를 원소를 가지는 두 집합 A, B
## output: 대칭 차집합의 원소의 개수
## 2023-03-15

setANumber, setBNumber = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))

setADict = {setA[i]: 0 for i in range(setANumber)}
setBDict = {setB[i]: 0 for i in range(setBNumber)}

cnt = 0
for i in range(setANumber):
    if setA[i] in setBDict:
        cnt += 1
result = len(setA) - cnt

cnt = 0
for i in range(setBNumber):
    if setB[i] in setADict:
        cnt += 1
result = result + len(setB) - cnt

print(result)