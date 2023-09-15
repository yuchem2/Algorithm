import sys


class Disjoint:
    def __init__(self, n):
        self.data = [[-1, 1] for _ in range(n)]
        self.size = n

    def find(self, idx):
        value = self.data[idx][0]
        if value < 0:
            return idx

        return self.find(value)

    def link(self, x, y):
        if x == y:
            return False

        if self.data[x][1] > self.data[y][1]:
            self.data[y][0] = x
        else:
            self.data[x][0] = y
            if self.data[x][1] == self.data[y][1]:
                self.data[y][1] += 1

        return True

    def union(self, x, y):
        return self.link(self.find(x), self.find(y))


def problem9372():
    n, m = map(int, sys.stdin.readline().split())
    dis_set = Disjoint(n)
    cnt = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if dis_set.union(a-1, b-1):
            cnt += 1

    sys.stdout.write(str(cnt)+"\n")


t = int(input())
for _ in range(t):
    problem9372()
