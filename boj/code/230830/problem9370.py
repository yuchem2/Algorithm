import sys
from queue import PriorityQueue


def problem9370():
    v_num, e_num, t_num = map(int, sys.stdin.readline().split())
    st, waypoint1, waypoint2 = map(int, sys.stdin.readline().split())
    roads = [{} for _ in range(v_num)]
    for _ in range(e_num):
        u, v, w = map(int, sys.stdin.readline().split())
        roads[u - 1][v - 1] = roads[v - 1][u - 1] = w
    targets = [int(sys.stdin.readline()) for _ in range(t_num)]
    targets.sort()

    def dijkstra(st):
        distance = [123456789] * v_num
        distance[st] = 0
        queue = PriorityQueue()
        queue.put((distance[st], st))

        while not queue.empty():
            u = queue.get()
            for v in roads[u[1]]:
                w = roads[u[1]][v] + u[0]
                if distance[v] > w:
                    distance[v] = w
                    queue.put((distance[v], v))
        return distance

    a = dijkstra(st - 1)
    b = dijkstra(waypoint1 - 1)
    c = dijkstra(waypoint2 - 1)
    for target in targets:
        case1 = a[waypoint1 - 1] + roads[waypoint1 - 1][waypoint2 - 1] + c[target - 1]
        case2 = a[waypoint2 - 1] + roads[waypoint1 - 1][waypoint2 - 1] + b[target - 1]
        buff = min(case1, case2)
        if buff > 123456789 or buff > a[target - 1]:
            continue
        else:
            sys.stdout.write(str(target) + " ")
    sys.stdout.write("\n")


t = int(input())
for _ in range(t):
    problem9370()
