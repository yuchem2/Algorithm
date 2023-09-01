def binary_search(array, target):
    l, r = 0, len(array)-1
    while l <= r:
        m = (l+r)//2
        if array[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l


def problem1450():
    n, c = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()
    left, right = [], []

    def left_find(x, cnt):
        if x == n//2:
            left.append(cnt)
            return
        left_find(x + 1, cnt)
        left_find(x + 1, cnt + weights[x])

    def right_find(x, cnt):
        if x == n:
            right.append(cnt)
            return
        right_find(x + 1, cnt)
        right_find(x + 1, cnt + weights[x])

    left_find(0, 0)
    right_find(n//2, 0)
    right.sort()
    cnt = 0
    for i in range(len(left)):
        if c >= left[i]:
            cnt += binary_search(right, c-left[i])

    print(cnt)


problem1450()
