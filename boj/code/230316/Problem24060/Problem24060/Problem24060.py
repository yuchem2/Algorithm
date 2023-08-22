
## baekjoon Problem10872
## input: array size N, save num k
## output: return kth save number
## 2023-03-16

def Merge(A, l, m, r, num):
    L, R = A[l:m+1], A[m+1:r+1]
    i, j, k = 0, 0, l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        A[-2] += 1
        if A[-2] == num:
            A[-1] = A[k-1]

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
        A[-2] += 1
        if A[-2] == num:
            A[-1] = A[k-1]

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
        A[-2] += 1
        if A[-2] == num:
            A[-1] = A[k-1]

def MergeSort(A, l, r, num):
    if l < r:
        m = (l+r) // 2
        MergeSort(A, l, m, num)
        MergeSort(A, m+1, r, num)
        Merge(A, l, m, r, num)

arrayLen, saveNum = map(int, input().split())
array = list(map(int, input().split())) + [0, 0]

MergeSort(array, 0, arrayLen-1, saveNum)

if array[-2] < saveNum:
    array[-1] = -1
print(array[-1])