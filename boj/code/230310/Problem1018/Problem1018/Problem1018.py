
import sys

def BoardCheckCnt(A, B, x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if A[x+i][y+j] != B[i][j]:
                cnt += 1

    return cnt

input = sys.stdin.readline

inRow, inCol = map(int, input().strip("\n").split())

board = []
for i in range(inRow):
    board.append(input().strip("\n"))

blackChessBoard = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", 
                   "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
whiteChessBorad = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
                   "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
result = 12345
for i in range(inRow-7):
    for j in range(inCol-7):
       tmp = min(BoardCheckCnt(board, whiteChessBorad, i, j), BoardCheckCnt(board, blackChessBoard, i, j))
       if tmp < result:
           result = tmp

print(result)