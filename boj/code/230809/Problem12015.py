def problem12015():
    num = int(input())
    int_array = list(map(int, input().split()))
    dp = [0]*num
    last_index = 0
    dp[0] = int_array[0]
    for i in range(1, len(int_array)):
        if int_array[i] > dp[last_index]:
            dp[last_index+1] = int_array[i]
            last_index += 1
        else:
            l, r = 0, last_index
            while l < r:
                m = (l+r)//2
                if dp[m] < int_array[i]:
                    l = m+1
                else:
                    r = m
            dp[l] = int_array[i]

    print(last_index+1)


if __name__ == '__main__':
    problem12015()