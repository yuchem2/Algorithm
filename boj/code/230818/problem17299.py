def problem17299():
    n = int(input())
    array = list(map(int, input().split()))
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    stack = []
    for i in range(n):
        while stack and count[array[i]] > count[array[stack[-1]]]:
            array[stack.pop()] = array[i]
        stack.append(i)
    while stack:
        array[stack.pop()] = -1

    print(' '.join(map(str, array)))


problem17299()
