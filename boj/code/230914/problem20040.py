import sys
sys.setrecursionlimit(10**6)


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
            return True

        if self.data[x][1] > self.data[y][1]:
            self.data[y][0] = x
        else:
            self.data[x][0] = y
            if self.data[x][1] == self.data[y][1]:
                self.data[y][1] += 1

        return False

    def union(self, x, y):
        return self.link(self.find(x), self.find(y))


def problem20040():
    n, m = map(int, sys.stdin.readline().split())
    dis_set = Disjoint(n)
    for i in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        if dis_set.union(v1, v2):
            print(i+1)
            return

    print(0)


problem20040()
