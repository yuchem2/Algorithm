
## baekjoon Problem11729
## input: n(1<= n <= 20)
## output: hanoi top moving list
## 2023-03-16

def Move(a, b):
    print(a + " " + b)

def Hanoi(n, a, b, c):
    if n == 0:
        return 0
    Hanoi(n-1, a, c, b)
    Move(a, c)
    Hanoi(n-1, b, a, c)


n = int(input())
print(2**n -1)
Hanoi(n, "1", "2", "3")