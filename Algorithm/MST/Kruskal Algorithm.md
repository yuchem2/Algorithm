tags: `MST`, `Union-Find(Disjoint Set)`
## 개념
- 그래프의 모든 간선을 비용이 낮은 순서대로 정렬한다.
- 정렬된 간선을 순회하면서 해당 간선을 추가해도 **사이클이 생기지 않으면** MST에 포함한다.
	- 사이클 생성을 방지하기 위해  **Union-Find (Disjoint Set)** 자료구조를 사용한다.
- MST에 포함된 간선의 개수가 (노드 수 - 1)이 되면 종료한다.
## 복잡도
> 간선의 수 = E, 노드의 수 = V
+ 시간 복잡도: `O(ElogE + Eα(V)) = O(ElogE)`
	+ 간선 정렬: `O(ElogE)`
	+ Union-Find 연산: 거의 상수 시간 (암시적으로 `O(α(V))`, 여기서 α는 아커만 함수의 역함수, 매우 느리게 증가)
+ 공간 복잡도: `O(E + V)`
	+ 간선 리스트: `O(E)`
	+ 부모 배열(Disjoint Set): `O(V)`
## 특징
- 희소 그래프(Sparse Graph)에서는 프림보다 더 빠를 수 있음
- 간선 중심 알고리즘 (간선을 먼저 다 본다)
- 간선을 한꺼번에 모아서 처리하므로, 입력으로 간선이 주어질 때 효율적
## 예제
### Python
```python
# Union-Find 자료구조 (Disjoint Set Union, DSU)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False  # 이미 같은 집합
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
        return True
        
def kruskal(n, edges):
    """
    n: 노드 개수 (0 ~ n-1)
    edges: (비용, 노드1, 노드2) 리스트
    """
    edges.sort(key=lambda x: x[0])  # 비용 기준 오름차순 정렬
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for cost, u, v in edges:
        if uf.union(u, v):
            mst_cost += cost
            mst_edges.append((u, v))
    return mst_cost, mst_edges
```