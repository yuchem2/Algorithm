# baekjoon Problem10844
# input: the number of digits
# output: the number of stair numbers
# 2023-05-11

n = int(input())
if n == 1:
    print(9)
else:
    check = [[0]*10 for x in range(n)]
    for i in range(10):
        check[0][i] = 1
    for i in range(1, n):
        check[i][0] = check[i-1][1]
        for j in range(1, 9):
            check[i][j] = check[i-1][j-1] + check[i-1][j+1]
        check[i][9] = check[i-1][8]

    check[n-1][0] = 0
    print(sum(check[n-1])%1000000000)