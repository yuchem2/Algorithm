import sys

def Merge(A, l, m, r):
    L = A[l:m+1]
    R = A[m+1:r+1]
    i = 0
    j = 0
    k = l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def MergeSort(A, l, r):
    if l < r:
        m = (l+r) // 2
        MergeSort(A, l, m)
        MergeSort(A, m+1, r)
        Merge(A, l, m, r)


input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
intArray = []
for i in range(0, n):
    num = int(input())
    intArray.append(num)

MergeSort(intArray, 0, n)
for num in intArray:
    print(str(num)+"\n")