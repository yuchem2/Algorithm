import sys
sys.setrecursionlimit(10**7)


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
            return

        if self.data[x][1] > self.data[y][1]:
            self.data[y][0] = x
        else:
            self.data[x][0] = y
            if self.data[x][1] == self.data[y][1]:
                self.data[y][1] += 1

    def union(self, x, y):
        self.link(self.find(x), self.find(y))


def problem1717():
    n, m = map(int, sys.stdin.readline().split())
    dis_set = Disjoint(n+1)
    for _ in range(m):
        t, a, b = map(int, sys.stdin.readline().split())
        if t == 0:
            dis_set.union(a, b)
        elif t == 1:
            if dis_set.find(a) == dis_set.find(b):
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")


problem1717()
