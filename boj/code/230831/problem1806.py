def problem1806():
    n, s = map(int, input().split())
    array = list(map(int, input().split()))
    l, r = 0, 0
    length = n + 1
    cumulative = array[l]
    while r < n:
        if cumulative >= s:
            if length > r - l + 1:
                length = r - l + 1
            cumulative -= array[l]
            l += 1
        elif r == n-1:
            break
        else:
            r += 1
            cumulative += array[r]

    print(length if length != n + 1 else 0)


problem1806()
