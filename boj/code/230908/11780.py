import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline


def problem11780():
    v_num, e_num = int(read()), int(read())
    edges = [[int(1e9)]*v_num for _ in range(v_num)]
    path = [[-1]*v_num for _ in range(v_num)]

    def find_path(array, i, j):
        if path[i][j] == -1:
            array.append(i + 1)
            array.append(j + 1)
            return

        find_path(array, i, path[i][j])
        array.pop()
        find_path(array, path[i][j], j)

    for _ in range(e_num):
        st, ed, c = map(int, read().split())
        if edges[st-1][ed-1] > c:
            edges[st-1][ed-1] = c

    for waypoint in range(v_num):
        for i in range(v_num):
            for j in range(v_num):
                if i == j:
                    continue
                if edges[i][j] > edges[i][waypoint] + edges[waypoint][j]:
                    edges[i][j] = edges[i][waypoint] + edges[waypoint][j]
                    path[i][j] = waypoint

    for i in range(v_num):
        for j in range(v_num):
            if edges[i][j] == int(1e9):
                sys.stdout.write("0 ")
            else:
                sys.stdout.write(str(edges[i][j]) + " ")
        sys.stdout.write("\n")

    result = []

    for i in range(v_num):
        for j in range(v_num):
            if edges[i][j] == int(1e9):
                sys.stdout.write("0\n")
            else:
                find_path(result, i, j)
                sys.stdout.write(str(len(result))+" ")
                sys.stdout.write(' '.join(map(str, result))+"\n")
                result.clear()


problem11780()
