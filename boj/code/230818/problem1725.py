import sys


def problem1725():
    n = int(input())
    heights = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    stack = []
    result = 0
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            idx = stack.pop()
            width = stack[-1] + 1 if stack else 0
            result = max(result, heights[idx] * (i-width))
        stack.append(i)

    while stack:
        idx = stack.pop()
        width = stack[-1] + 1 if stack else 0
        result = max(result, heights[idx] * (n - width))

    print(result)


problem1725()
