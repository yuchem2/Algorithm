import sys
from collections import deque


def problem13913():
    n, k = map(int, input().split())
    limit = 100001
    array = [-1] * limit
    queue = deque([n])
    array[n] = -2

    if k < n:
        stack = [x for x in range(n, k-1, -1)]
        print(n-k)
        print(' '.join(map(str, stack)))
    else:
        while queue:
            u = queue.popleft()
            if u == k:
                break

            if u - 1 >= 0 and array[u - 1] == -1:
                array[u - 1] = u
                queue.append(u - 1)
            if 2 * u < limit and array[2 * u] == -1:
                array[2 * u] = u
                queue.append(2 * u)
            if u + 1 < limit and array[u + 1] == -1:
                array[u + 1] = u
                queue.append(u + 1)

        cnt = 0
        buff = array[k]
        stack = [k]
        while buff != -2:
            cnt += 1
            stack.append(buff)
            buff = array[buff]

        print(cnt)
        while stack:
            sys.stdout.write(str(stack.pop()) + " ")


problem13913()
