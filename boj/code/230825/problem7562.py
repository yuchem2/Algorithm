import sys


def problem7562():
    num = int(sys.stdin.readline().rstrip())
    st = list(map(int, sys.stdin.readline().split()))
    ed = list(map(int, sys.stdin.readline().split()))
    board = [[0]*num for _ in range(num)]
    promise = [[-1, -2], [-2, -1], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
    queue = [st]
    while queue:
        u = queue.pop(0)
        if u == ed:
            print(board[ed[0]][ed[1]])
            break
        for x, y in promise:
            dx, dy = u[0]+x, u[1]+y
            if 0 <= dx < num and 0 <= dy < num:
                if board[dx][dy] == 0:
                    queue.append([dx, dy])
                    board[dx][dy] = board[u[0]][u[1]] + 1


t = int(input())
for _ in range(t):
    problem7562()
