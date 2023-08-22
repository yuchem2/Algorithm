# baekjoon Problem1463
# input: an integer n (1<= n <=10^6)
# output: minimum num of operators
# 2023-05-11
import sys
sys.setrecursionlimit(10**5)


n = int(input())

if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    cnt = [100] * n
    cnt[0], cnt[1], cnt[2] = 0, 1, 1
    x = 3
    while x <= n:
        num1, num2 = 100, 100
        if x % 3 == 0:
            num1 = cnt[x // 3 - 1] + 1
        if x % 2 == 0:
            num2 = cnt[x // 2 - 1] + 1

        cnt[x - 1] = min(num1, num2, cnt[x - 2] + 1)
        x += 1

    print(cnt[n-1])