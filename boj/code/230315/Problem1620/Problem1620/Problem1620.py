## Baaek Joon Problem 1620
## 2023-03-15

import sys
input = sys.stdin.readline
print = sys.stdout.write

pokemonNum, problemNum = map(int, input().strip("\n").split())

pokemonList = []
for i in range(pokemonNum):
    pokemonList.append(input().strip("\n"))

pokemonDic1 = {pokemonList[i]:i+1 for i in range(pokemonNum) }

resultList = []
for _ in range(problemNum):
    inStr = input().strip("\n")
    if inStr[0] >= 'A' and inStr[0] <= 'Z':
        resultList.append(str(pokemonDic1[inStr]))
    else:
        resultList.append(pokemonList[int(inStr)-1])

for result in resultList:
    print(result + "\n")