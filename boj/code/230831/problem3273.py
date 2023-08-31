def problem3273():
    n = int(input())
    array = list(map(int, input().split()))
    target = int(input())

    array.sort()
    i, j = 0, n-1
    count = 0
    while i < j:
        buff = array[i] + array[j]
        if buff == target:
            count += 1
            i += 1
            j -= 1
        elif buff > target:
            j -= 1
        else:
            i += 1
    print(count)


problem3273()
