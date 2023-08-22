# baekjoon Problem14888
# input: n[2, 11], sequence, operator
# output: maximum and minimum result
# 2023-03-29 00:15-00:59

def calculate(a, b, op):
    if op == 0:       # +
        return a + b
    elif op == 1:     # -
        return a - b
    elif op == 2:     # x
        return a * b
    else:                   # /
        if a < 0:
            return -(abs(a) // b)
        elif b < 0:
            return -(a // abs(b))
        else:
            return a // b


def dfs(x):
    if x == maxCnt:
        maxMinList[0] = max(maxMinList[0], intArray[-1])
        maxMinList[1] = min(maxMinList[1], intArray[-1])
        return

    for i in range(4):
        if operator[i] > 0:
            temp = intArray[x+1]
            intArray[x+1] = calculate(intArray[x], intArray[x+1], i)
            operator[i] -= 1
            dfs(x+1)
            intArray[x+1] = temp
            operator[i] += 1


if __name__ == "__main__":
    n = int(input())
    intArray = list(map(int, input().split()))
    operator = list(map(int, input().split()))  # +, -, x, /

    maxCnt = sum(operator)
    maxMinList = [-1000000000, 1000000000]

    dfs(0)
    for num in maxMinList:
        print(num)
