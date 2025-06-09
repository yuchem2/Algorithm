tags: `Shortest Path`
## 개념
- 모든 정점 쌍 사이의 최단 경로를 구하는 알고리즘
- 각 정점 쌍 `(i, j)`에 대해 중간 정점 집합을 점점 확장하며 최단 거리를 갱신
- 음수 가중치가 있어도 동작하지만, 음수 사이클이 있으면 결과가 의미 없을 수 있음
- 최단 경로뿐만 아니라 최소 사이클 길이 탐색에도 활용 가능
## 복잡도
- 시간복잡도: `O(V^3)`
- 공간복잡도: `O(V^2)`
## 특징
- 그래프의 모든 정점 쌍 최단 경로를 한 번에 구할 수 있음
- 음수 가중치 간선이 있어도 동작 (단, 음수 사이클이 없을 때 정확함)
- 대규모 그래프에는 비효율적이나, 중간 규모 그래프에서는 구현이 간단해 자주 사용됨
## 예시
### Python
```python
def floyd_warshall(distance):
    """
    distance: 2차원 배열 (인접행렬)로, distance[i][j]는 i에서 j로 가는 간선의 가중치 또는 INF
    반환값: 모든 정점 쌍 간 최단 경로가 담긴 2차원 배열
    """
    n = len(distance)
    for k in range(n):          # 중간 경유지
        for i in range(n):      # 출발지
            for j in range(n):  # 도착지
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance
```