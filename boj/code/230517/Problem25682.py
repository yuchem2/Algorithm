# baekjoon Problem25682
# input: 2D chess board
# output: minimumm the number of repainting square
# 05-17-2023

import sys

def solution():
    global sol
    for i in range(1, row + 1):
        temp = sys.stdin.readline().rstrip()
        sol.append(sol[0][:])
        for j in range(1, col + 1):
            sol[i][j] = (sol[i - 1][j] + sol[i][j - 1] - sol[i - 1][j - 1]) + (int)(
                temp[j - 1] == color[(abs(i - j - 2)) % 2])

    result = n ** 2
    for i in range(1, row - n + 2):
        for j in range(1, col - n + 2):
            temp = sol[i + n - 1][j + n - 1] - sol[i - 1][j + n - 1] - sol[i + n - 1][j - 1] + sol[i - 1][j - 1]
            result = min(result, temp, n ** 2 - temp)
    return result

def cumulativeSum():
    global sol

row, col, n = map(int, input().split())

color = ['B', 'W']
sol = [[0]*(col+1)]
print(solution())