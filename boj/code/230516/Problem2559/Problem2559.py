# baekjoon Problem2559
# input: integer n, k. temperature sequence
# output: maximum sum of temperature
# 05-16-2023

dates, window = map(int, input().split())
temperature = list(map(int, input().split()))


sumTemp = [0] * (dates-window+1)
sumTemp[0] = sum(temperature[0:window])

for i in range(1, len(sumTemp)):
    sumTemp[i] = sumTemp[i-1] - temperature[i-1] + temperature[i+window-1]
print(max(sumTemp))