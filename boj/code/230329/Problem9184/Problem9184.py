# filename: Problem9184
# convert recursive function to dynamic programming
# 2023-03-30 01:08-01:54
# Jaehyun Yoon

import sys
input = sys.stdin.readline

def w(a, b, c):
    # 예외 처리
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 동적 할당법 + 재귀 이용해 계산
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
inArray = []
while True:
    temp = list(map(int, input().rstrip().split()))
    if temp[0] == -1 and temp[1] == -1 and temp[2] == -1:
        break
    inArray.append(temp)

for i in range(len(inArray)):
    print("w(" + str(inArray[i][0]) + ", " + str(inArray[i][1]) + ", " + str(inArray[i][2]) + ") =",
          w(inArray[i][0], inArray[i][1], inArray[i][2]))
