tags: `Shortest Path`, `Heap(Priority Queue)`
## 개념
- 가중치가 있는 그래프에서 하나의 시작점에서 모든 정점까지의 최단 경로를 찾는 알고리즘
- 음수 가중치는 다룰 수 없음
- 주로 우선순위 큐(힙)를 사용해서 가장 가까운 정점부터 탐색하며 경로를 갱신
## 복잡도
> 간선의 수 = E, 노드의 수 = V
+ 시간복잡도
	+ 우선순위 큐를 사용할 경우 `O(ElogV)`
	+ 단순 배열을 사용하는 경우 `O(V^2)`
+ 공간복잡도: `O(V + E)`
## 특징
- 음수 가중치 간선이 있는 경우 사용 불가
- 빠르고 효율적 (음수 간선 없을 때 최적)
- 도로, 네트워크 경로 찾기 등 다양한 문제에 사용됨
## 예시
### Python
```python
import heapq

def dijkstra(graph, start):
	"""
	graph = [[(v1, w)], [(v2, w), (v3, w)], ...] 인접 리스트 형태
	start = 시작 정점
	"""
    V = len(graph)
    distance = [float('inf')] * V
    distance[start] = 0

    pq = [(0, start)]  # (거리, 정점)
    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distance[u]:
            continue
        for v, w in graph[u]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(pq, (cost, v))
    return distance
```