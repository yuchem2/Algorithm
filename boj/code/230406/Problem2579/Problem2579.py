# baekjoon Problem2579
# input: stairs num
# output: max score
# 2023-04-06

n = int(input())
stairArray = [0]*n
for i in range(n):
    stairArray[i] = int(input())

if n < 3:
    if n == 1:
        print(stairArray[0])
    else:
        print(max(stairArray[0] + stairArray[1], stairArray[1]))
else:
    score = [0] * n
    score[0] = stairArray[0]
    score[1] = max(stairArray[0] + stairArray[1], stairArray[1])
    score[2] = max(stairArray[0] + stairArray[2], stairArray[1] + stairArray[2])

    for i in range(3, n):
        score[i] = max(stairArray[i] + score[i-2], stairArray[i] + stairArray[i-1] + score[i-3])

    print(score[-1])