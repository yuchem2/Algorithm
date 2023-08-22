# baekjoon Problem12865
# input: the number of objects(1<= n <= 100), weights of the objcets (1 <= K <= 100000), value of the objects
# output: the maximum values
# 2023-05-16

num, maxWeight = map(int, input().split())
weights, values = [0]*num, [0]*num
for i in range(num):
    weights[i], values[i] = map(int, input().split())

crtWeight = 0
dp = [0]*(maxWeight+1)

for i in range(num):
    for j in range(maxWeight, weights[i]-1, -1):
        dp[j] = max(dp[j], dp[j-weights[i]] + values[i])

print(dp)
print(max(dp))

