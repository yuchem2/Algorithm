def problem9935():
    target = input()
    boom = input()
    stack = []
    for ch in target:
        stack.append(ch)
        if boom[-1] == ch and ''.join(stack[len(stack)-len(boom):]) == boom:
            for _ in range(len(boom)):
                stack.pop()

    if stack:
        print(''.join(stack))
    else:
        print('FRULA')


problem9935()
