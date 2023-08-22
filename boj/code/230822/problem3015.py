import sys


def problem3015():
    n = int(input())
    people = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    result = 0
    for i in range(n):
        while stack and people[stack[-1]] < people[i]:
            result += (i - stack.pop())
        stack.append(i)

    while stack:
        result += (n - stack.pop() - 1)
    print(result)


problem3015()
