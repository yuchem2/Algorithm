# baekjoon Problem9251
# input: two sentences
# output: the length of LCS
# 2023-05-15

str1 = input()
str2 = input()
strLen1 = len(str1)+1
strLen2 = len(str2)+1

dp = [[0]*(strLen2) for x in range(strLen1)]

for i in range(1, strLen1):
    for j in range(1, strLen2):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[-1]))