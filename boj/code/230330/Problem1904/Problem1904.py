# filename: Problem1904.py
# input: n (1<= n <= 1,000,000)
# output: 만들 수 있는 길이가 n인 모든 2진 수열의 개수를 15746으로 나눈 나머지
# 2023-03-30

n = int(input())

biSequence = [0]*n
if n >= 2:
    biSequence[0] = 1
    biSequence[1] = 2
    for i in range(2, n):
        biSequence[i] = (biSequence[i-2] + biSequence[i-1]) % 15746
    print(biSequence[-1])
else:
    print(n)
