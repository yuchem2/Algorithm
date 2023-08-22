def problem17298():
    n = int(input())
    array = list(map(int, input().split()))
    stack = []
    for i in range(n):
        while stack and array[i] > array[stack[-1]]:
            array[stack.pop()] = array[i]
        stack.append(i)
    while stack:
        array[stack.pop()] = -1

    print(' '.join(map(str, array)))


problem17298()
