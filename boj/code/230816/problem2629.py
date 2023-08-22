def check(marble, dp):
    if len(dp) - 1 < marble:
        print("N", end=" ")
        return
    if dp[marble] == 1:
        print("Y", end=" ")
    else:
        for i in range(len(dp)-marble-1):
            if dp[i] and dp[i+marble]:
                print("Y", end=" ")
                return
        print("N", end=" ")


def problem2629():
    weight_num = int(input())
    weights = list(map(int, input().split()))
    marble_num = int(input())
    marbles = list(map(int, input().split()))
    dp = [0]*(sum(weights)+1)
    dp[0] = 1
    for i in range(weight_num):
        for j in range(len(dp)-1, -1, -1):
            if dp[j]:
                dp[j+weights[i]] = 1

    for marble in marbles:
        check(marble, dp)


problem2629()
