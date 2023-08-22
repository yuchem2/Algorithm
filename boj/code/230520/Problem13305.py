# baekjoon Problem13305
# input: city graph
# output: minimum cost of route
# 05-20-2023

def problem13305():
    cityNum = int(input())
    length = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    totalLength = sum(length)

    result = cost[0]*length[0]
    cnt = cost[0]
    for i in range(1, cityNum-1):
        cnt = min(cnt, cost[i])
        result += (cnt*length[i])
    print(result)

problem13305()

