## baekjoon Problem10872
## input: 0 <= n < 20
## output: fib(n)
## 2023-03-16

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
result = fib(n)
print(result)