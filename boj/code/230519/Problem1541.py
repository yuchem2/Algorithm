# baekjoon Problem1541
# input: mathematical expression
# output: minimum result
# 05-19-2023

def problem1541():
    expression = input()

    numbers = []
    operators = []
    i = 0
    lastNum = 0
    while i < len(expression):
        if expression[i] == '-' or expression[i] == '+':
            numbers.append(int(expression[lastNum:i]))
            operators.append(expression[i])
            lastNum = i+1
        elif i == len(expression)-1:
            numbers.append(int(expression[lastNum:]))
        i += 1

    for i in range(len(operators)-1):
        if operators[i] == '-':
            operators[i+1] = '-'

    for i in range(len(operators)):
        if operators[i] == '-':
            numbers[i+1] = numbers[i] - numbers[i+1]
        if operators[i] == '+':
            numbers[i+1] = numbers[i] + numbers[i+1]
    print(numbers[-1])

problem1541()
