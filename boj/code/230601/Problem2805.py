# baekjoon Problem2805
# 06-01-2023
def problem2850():
    n, m = map(int, input().split())
    height = list(map(int, input().split()))
    l, r = 0, max(height)

    while l <= r:
        cnt = 0
        mid = (l+r)//2
        for i in range(n):
            if mid < height[i]:
                cnt += (height[i]-mid)

        if cnt >= m:
            l = mid + 1
        else:
            r = mid - 1
    print(r)


if __name__ == '__main__':
    problem2850()
