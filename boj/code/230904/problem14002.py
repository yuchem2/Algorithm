import sys


def problem14002():
    n = int(input())
    array = list(map(int, input().split()))
    dp = [1]*n
    tmp, index = 0, 0
    for i in range(n):
        for j in range(i+1):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j]+1)
        if tmp < dp[i]:
            tmp = dp[i]
            index = i

    print(tmp)
    result = []
    while index >= 0:
        if dp[index] == tmp:
            result.append(array[index])
            tmp -= 1
        index -= 1

    while result:
        sys.stdout.write(str(result.pop())+" ")


problem14002()
