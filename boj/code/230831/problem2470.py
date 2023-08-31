def problem2470():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    result = [array[0], array[n-1]]
    l, r = 0, n-1
    while l < r:
        buff = array[l] + array[r]
        if abs(buff) < abs(result[0] + result[1]):
            result[0], result[1] = array[l], array[r]

        if buff > 0:
            r -= 1
        elif buff < 0:
            l += 1
        else:
            break

    print(result[0], result[1])


problem2470()
