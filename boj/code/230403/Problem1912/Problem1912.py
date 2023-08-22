# baekjoon Problem1912
# input: integer sequence
# output: max sum
# 2023-04-04 01:07-01:31

n = int(input())
intArray = list(map(int, input().split()))

cur = 0
best = -10 ** 8
for num in intArray:
    cur = max(num, cur + num)
    best = max(best, cur)

print(best)