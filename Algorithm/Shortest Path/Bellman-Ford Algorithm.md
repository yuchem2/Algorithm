tags: `Shortest Path`
## 개념
- **단일 출발점**에서 **모든 정점까지의 최단 경로**를 구하는 알고리즘
- **음수 가중치 간선**이 포함된 그래프에서도 동작 가능
- 모든 간선을 `V-1`번 반복적으로 탐색하면서 최단 경로를 갱신
- `V`번째 반복에서도 갱신이 발생하면 **음수 사이클 존재**로 판단
## 복잡도
- **시간복잡도:** `O(V × E)`
- **공간복잡도:** `O(V)`
## 특징
- 출발 정점에서 **도달 가능한 정점**에 대해서만 최단 거리 계산
- **음수 가중치 간선**이 있는 경우에도 사용할 수 있는 몇 안 되는 알고리즘 중 하나
- **음수 사이클 유무를 감지**할 수 있음
- 다익스트라와 달리, **우선순위 큐를 사용하지 않음**
## 예시
### Python
```python
def bellman_ford(n, edges, start):
    """
    n: 정점 개수
    edges: [(u, v, w)] 형태의 간선 리스트 (u -> v, 가중치 w)
    start: 시작 정점 (0-based index)
    반환값: start에서 각 정점까지 최단 거리 리스트, 음수 사이클이 있으면 None
    """
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0

    for i in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    # 음수 사이클 체크
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            return None  # 음수 사이클 존재

    return dist
```