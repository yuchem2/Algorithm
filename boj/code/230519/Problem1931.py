# baekjoon Problem11047
# input: conference number
# output: maximum number of conferences
# 05-19-2023

import sys

def merge(a, l, m, r):
    L, R = a[l:m+1], a[m+1:r+1]
    i, j, k = 0, 0, l
    while i < len(L) and j < len(R):
        if L[i][1] < R[j][1] or (L[i][1] == R[j][1] and L[i][0] < R[j][0]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1

def mergeSort(a, l, r):
    if l < r:
        m = (l+r)//2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m, r)

def greedy(a):
    cnt = 1
    cntTime = a[0][1]
    for i in range(1, len(a)):
        if cntTime <= a[i][0]:
            cnt += 1
            cntTime = a[i][1]
    return cnt


def problem1931():
    num = int(input())

    conference = [0]*num
    for i in range(num):
        conference[i] = list(map(int, sys.stdin.readline().split()))

    mergeSort(conference, 0, len(conference))
    print(greedy(conference))


problem1931()
