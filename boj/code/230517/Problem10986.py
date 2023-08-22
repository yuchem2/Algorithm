# baekjoon Problem10986
# input: two integer and sequence
# output: number of interval
# 05-17-2023

num, divisor = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.insert(0, 0)

cnt = [0]*divisor
for i in range(1, num+1):
    sequence[i] = (sequence[i] + sequence[i-1])%divisor
    cnt[sequence[i]] += 1

result = cnt[0]
for i in range(divisor):
    if cnt[i] > 1:
        result += ((cnt[i] * (cnt[i]-1))//2)
print(result)