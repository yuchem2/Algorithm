import sys


def problem9252():
    source, target = input(), input()
    source_len, target_len = len(source)+1, len(target)+1
    dp = [[0]*target_len for _ in range(source_len)]
    for i in range(1, source_len):
        for j in range(1, target_len):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    buff = max(dp[-1])
    x, y = target_len-1, source_len-1
    print(buff)
    stack = []
    while x and y:
        if dp[y][x] == dp[y-1][x]:
            y -= 1
        elif dp[y][x] == dp[y][x-1]:
            x -= 1
        else:
            stack.append(target[x-1])
            x -= 1
            y -= 1

    while stack:
        sys.stdout.write(stack.pop())


problem9252()
