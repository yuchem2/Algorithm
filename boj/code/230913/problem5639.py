import sys

sys.setrecursionlimit(10 ** 6)


def to_postorder(st, ed):
    if st > ed:
        return
    right_st = ed + 1

    for i in range(st + 1, ed + 1):
        if preorder[i] > preorder[st]:
            right_st = i
            break

    to_postorder(st + 1, right_st - 1)
    to_postorder(right_st, ed)

    sys.stdout.write(str(preorder[st]) + "\n")


preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline().rstrip()))
    except ValueError:
        break

to_postorder(0, len(preorder) - 1)
