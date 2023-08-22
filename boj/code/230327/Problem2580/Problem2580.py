# baekjoon Problem2580
# input: 9x9 sudoku board
# output: complete 9x9 sudoku board
# 2023-03-27 22:22 - 23:29 time out 23:57 correct

import sys

input = sys.stdin.readline
print = sys.stdout.write

blankList = []
sudokuBoard = [[0]*9 for x in range(9)]

# time out
# for i in range(9):
#     inLine = list(map(int, input().rstrip().split()))
#     for j in range(9):
#         sudokuBoard[i][j] = inLine[j]
#         if inLine[j] == 0:
#             blankList.append([i, j])
#
# def promise(x, y, num):
#     # row & col check
#     for i in range(9):
#         if sudokuBoard[x][i] == num or sudokuBoard[i][y] == num:
#             return False
#
#     # 3x3 check
#     dx = x // 3
#     dy = y // 3
#     for i in range(3*dx, 3*dx+3):
#         for j in range(3*dy, 3*dy+3):
#             if sudokuBoard[i][j] == num:
#                 return False
#
#     # pass the promising check
#     return True
#
# def dfs(cnt):
#     if cnt == len(blankList):
#         return True
#
#     x, y = blankList[cnt]
#     for num in range(1, 10):
#         if promise(x, y, num):
#             sudokuBoard[x][y] = num
#             if dfs(cnt+1):
#                 return True
#             sudokuBoard[x][y] = 0
#     return False

# + array: Promising Check O(1)
rowCheck = [[False]*9 for x in range(9)]
colCheck = [[False]*9 for x in range(9)]
boxCheck = [[False]*9 for x in range(9)]

for i in range(9):
     inLine = list(map(int, input().rstrip().split()))
     for j in range(9):
         sudokuBoard[i][j] = inLine[j]
         if inLine[j] == 0:
             blankList.append([i, j])
         else:
             rowCheck[i][inLine[j] - 1] = colCheck[j][inLine[j] - 1] = boxCheck[(i//3)*3 + j//3][inLine[j]-1] = True

def promise(x, y, num):
    # row & col check
    if rowCheck[x][num-1] or colCheck[y][num-1]:
        return False

    # box check
    if boxCheck[(x//3)*3 + y//3][num-1]:
        return False
    return True

def dfs(cnt):
    if cnt == len(blankList):
        return True

    x, y = blankList[cnt]
    for num in range(1, 10):
        if promise(x, y, num):
            sudokuBoard[x][y] = num
            rowCheck[x][num-1] = colCheck[y][num-1] = boxCheck[((x//3)*3 + y//3)][num-1] = True
            if dfs(cnt+1):
                return True
            sudokuBoard[x][y] = 0
            rowCheck[x][num - 1] = colCheck[y][num - 1] = boxCheck[((x // 3) * 3 + y // 3)][num - 1] = False

    return False

dfs(0)
for i in range(9):
    print(' '.join(map(str, sudokuBoard[i])) + '\n')