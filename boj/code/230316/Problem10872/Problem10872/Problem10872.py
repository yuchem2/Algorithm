## baekjoon Problem10872
## input: 0 <= n <= 12
## output: n!
## 2023-03-16

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())

result = factorial(n)
print(result)