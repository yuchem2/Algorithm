# baekjoon Problem1300
# 06-02-2023

def problem1300():
    n = int(input())
    k = int(input())
    l, r = 1, min(10**9, n*n)

    while l <= r:
        m = (l+r)//2
        cnt = 0
        for i in range(1, n+1):
            cnt += min((m-1)//i, n)
        if cnt >= k:
            r = m - 1
        else:
            l = m + 1
    print(r)


if __name__ == '__main__':
    problem1300()
