import sys
sys.setrecursionlimit(10**6)


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def problem2618():
    road_num = int(input())
    case_num = int(input())
    cases = [[(1, 1)], [(road_num, road_num)]]
    for _ in range(case_num):
        case = tuple(map(int, sys.stdin.readline().split()))
        cases[0].append(case)
        cases[1].append(case)
    dp = [[-1]*(case_num+1) for _ in range(case_num+1)]

    def dfs(i, j):
        if i == case_num or j == case_num:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        k = max(i, j) + 1
        dp[i][j] = min(dfs(k, j) + dist(cases[0][i], cases[0][k]), dfs(i, k) + dist(cases[1][j], cases[1][k]))
        return dp[i][j]

    def back(i, j):
        if i == case_num or j == case_num:
            return

        k = max(i, j) + 1
        if dp[i][j] - dp[k][j] >= dist(cases[0][i], cases[0][k]):
            sys.stdout.write('1\n')
            back(k, j)
        else:
            sys.stdout.write('2\n')
            back(i, k)

    print(dfs(0, 0))
    back(0, 0)


problem2618()
