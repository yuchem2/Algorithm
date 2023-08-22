import sys
input = sys.stdin.readline
print = sys.stdout.write

def Merge(A, l, m, r):
    L = A[l:m+1]
    R = A[m+1:r+1]
    i = 0
    j = 0
    k = l
    while i < len(L) and j < len(R):
        if int(L[i][1]) < int(R[j][1]):
            A[k] = L[i]
            i += 1
        elif int(L[i][1]) == int(R[j][1]) and int(L[i][0]) < int(R[j][0]):
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

inNum = int(input())

inArray = []
for i in range(0, inNum):
    dot = input()
    dot = dot.split()
    inArray.append(dot)

MergeSort(inArray, 0, len(inArray))

for i in range(0, inNum):
    print(str(inArray[i][0]) + " " + str(inArray[i][1]) + "\n")