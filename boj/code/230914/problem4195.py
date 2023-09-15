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
            return self.data[x][1]

        if self.data[x][1] > self.data[y][1]:
            self.data[y][0] = x
            self.data[x][1] += self.data[y][1]
            return self.data[x][1]
        else:
            self.data[x][0] = y
            self.data[y][1] += self.data[x][1]
            return self.data[y][1]

    def union(self, x, y):
        return self.link(self.find(x), self.find(y))


def problem4195():
    n = int(sys.stdin.readline())
    dis_set = Disjoint(2*n)
    dic = {}
    for _ in range(n):
        f1, f2 = sys.stdin.readline().split()
        if f1 not in dic:
            dic[f1] = len(dic)
        if f2 not in dic:
            dic[f2] = len(dic)

        sys.stdout.write(str(dis_set.union(dic[f1], dic[f2]))+"\n")


t = int(input())
for _ in range(t):
    problem4195()
