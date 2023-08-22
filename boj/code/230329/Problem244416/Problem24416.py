# filename: Problem24416.py
# dynamic Programming for fibonacci
# 2023-03-29
# Jaehyun Yoon

def fib(x):
    f = [0] * x
    f[0], f[1] = 1, 1
    cnt = 0
    for i in range(2, x):
        f[i] = f[i-1] + f[i-2]  # code 2
        cnt += 1
    print(f[n-1], cnt)

n = int(input())
fib(n)
