# baekjoon Problem6549
# input: 2D array
# output: A^B (A is matrix)
# 05-24-2023
import sys


def divide(a, l, r):
    if l < r:
        m = (l+r)//2
        l_max = divide(a, l, m)
        r_max = divide(a, m+1, r)

        i, j = m, m+1
        min_h = min(a[i], a[j])
        result = min_h * (j-i+1)
        while l <= i and j <= r:
            ih = a[i-1] if i > l else 0
            jh = a[j+1] if j < r else 0
            if ih > jh:
                min_h = min(min_h, ih)
                i -= 1
            else:
                min_h = min(min_h, jh)
                j += 1
            result = max(result, min_h * (j-i+1))
        return max(l_max, r_max, result)
    else:
        return a[r]


def problem6549():
    in_str = sys.stdin.readline().rstrip()
    while in_str[0] != '0':
        heights = list(map(int, in_str.split()))
        print(divide(heights, 1, heights[0]))
        in_str = sys.stdin.readline().rstrip()


def problem6549_stack():
    in_str = sys.stdin.readline().rstrip()
    while in_str[0] != '0':
        heights = list(map(int, in_str.split()))
        stack = []
        result = 0
        for i in range(1, len(heights)):
            if stack and heights[stack[-1]] > heights[i]:
                while stack:
                    idx = stack.pop()
                    width = stack[-1] + 1 if stack else 1
                    result = max(result, heights[idx] * (i-width))
                    if not stack or heights[stack[-1]] <= heights[i]:
                        break
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)

        while stack:
            idx = stack.pop()
            width = stack[-1] + 1 if stack else 1
            result = max(result, heights[idx]*(heights[0]-width+1))

        print(result)
        in_str = sys.stdin.readline().rstrip()


def problem1725():
    n = int(input())
    heights = [0]*n
    for i in range(n):
        heights[i] = int(sys.stdin.readline().rstrip())

    print(divide(heights, 0, n-1))


if __name__ == "__main__":
    problem6549_stack()
    # problem1725()
