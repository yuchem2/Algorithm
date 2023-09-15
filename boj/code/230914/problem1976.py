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
            return

        if self.data[x][1] > self.data[y][1]:
            self.data[y][0] = x
        else:
            self.data[x][0] = y
            if self.data[x][1] == self.data[y][1]:
                self.data[y][1] += 1

    def union(self, x, y):
        self.link(self.find(x), self.find(y))


def problem1976():
    n, m = int(sys.stdin.readline()), int(sys.stdin.readline())
    dis_set = Disjoint(n)
    for i in range(n):
        array = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if array[j] == 1:
                dis_set.union(i, j)

    travel = list(map(int, sys.stdin.readline().split()))
    for i in range(m-1):
        if dis_set.find(travel[i]-1) != dis_set.find(travel[i+1]-1):
            sys.stdout.write("NO")
            return

    sys.stdout.write("YES")


problem1976()
