# baekjoon Problem11399
# input: the number fo people and the time of withdraw
# output: minimum number of coins
# 05-19-2023

def greedy(a, n):
    a.sort()
    for i in range(1, n):
        a[i] += a[i-1]

    return sum(a)

def problem11399():
    num = int(input())
    withdrawTime =  list(map(int, input().split()))

    print(greedy(withdrawTime, num))


problem11399()