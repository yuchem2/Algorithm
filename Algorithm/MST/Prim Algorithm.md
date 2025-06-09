tags: `MST`, `Heap(Priority Queue)`
## 개념
- 시작 노드를 임의로 정하고, 이 노드에서 연결된 간선 중 최소 비용의 간선을 선택해 MST를 확장한다.
- MST에 포함된 노드 집합에서 연결된 간선 중 가장 비용이 작은 간선을 선택한다. 
- 계속 반복하여 모든 노드를 MST에 포함시킨다.
- MST에 연결된 노드들이 여러 개일 때, 이들 노드와 인접한 간선 중 최소 비용 간선을 빠르게 선택해야 하므로 최소 힙(우선순위 큐)을 사용한다.
## 복잡도
> 간선의 수 = E, 노드의 수 = V
+ 시간 복잡도: `O((E + V)logV)` (힙 없이 배열로 구현 시 `O(N^2)`)
	+ 모든 노드를 한 번씩 처리: `O(VlogV)`
	+ 각 노드에서 인접 간선 최대 V-1번 확인: `O(ElogV)`
+ 공간복잡도: `O(V + E)`
	+ 인접 리스트: `O(V + E)`
	+ 방문 배열: `O(V)`
	+ 힙(우선순위 큐): 최악의 경우 `O(E)`
## 특징
+ 간선이 많고 밀도가 높은 그래프(Dense Graph)에서 효율적
+ 노드 중심 알고리즘
+ 인접 리스트로 구현하면 성능이 더 좋아짐
## 예제
### Python
```python
def prim(n, graph):
    """
    n: 노드 개수 (0 ~ n-1)
    graph: 인접 리스트 형태, graph[u] = [(비용, v), ...]
    """
    visited = [False]*n
    min_heap = [(0, 0)]  # (비용, 시작 노드)
    mst_cost = 0
    count = 0

    while min_heap and count < n:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += cost
        count += 1

        for edge_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v))

    if count == n:
        return mst_cost
    else:
        return None  # 모든 노드 연결 불가
```