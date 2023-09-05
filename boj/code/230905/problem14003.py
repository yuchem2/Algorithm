import sys


def binary_search(array, target):
    l, r = 0, len(array)-1
    while l <= r:
        m = (l+r)//2
        if array[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l


def problem14003():
    n = int(input())
    array = list(map(int, input().split()))
    vector = []
    dp = [0]*n
    for i in range(n):
        if not vector or vector[-1] < array[i]:
            vector.append(array[i])
            dp[i] = len(vector)
        else:
            index = binary_search(vector, array[i])
            vector[index] = array[i]
            dp[i] = index + 1

    buff = len(vector)
    stack = []
    print(buff)
    for i in range(n-1, -1, -1):
        if dp[i] == buff:
            stack.append(array[i])
            buff -= 1

    while stack:
        sys.stdout.write(str(stack.pop())+" ")


problem14003()
