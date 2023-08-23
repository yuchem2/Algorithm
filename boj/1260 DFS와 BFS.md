# [BOJ] 1260번 DFS와 BFS (PYTHON)
백준온라인저지(BOJ) https://www.acmicpc.net/

ID: yuchem2

Date: 2023.08.23
## 1. 문제설명
| 시간 제한 | 메모리 제한 | 제출  | 정답 | 맞은 사람 | 정답 비율 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2초  | 128MB | 247342 | 94806 | 56312 | 37.157% |

### 문제
---
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
### 입력
---
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
### 출력
---
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
### 예제입력1
```
4 5 1
1 2
1 3
1 4
2 4
3 4
```
### 예제출력1
```
1 2 4 3
1 2 3 4
```
## 2. 소스코드

### 알고리즘
단순히 bfs와 dfs를 두번 실행하면 된다. 이때 visited 배열을 다시 한번 0으로 초기화 해준다. 
### 코드
```Python
import sys
sys.setrecursionlimit(10**6)


def dfs(x):
    print(x, end=" ")
    visited[x-1] = 1
    for e in edges[x-1]:
        if visited[e-1] == 0:
            dfs(e)


def bfs(x):
    visited[x-1] = 1
    print(x, end=" ")
    queue = [x]
    while queue:
        u = queue.pop(0)

        for e in edges[u-1]:
            if visited[e-1] == 0:
                visited[e-1] = 1
                queue.append(e)
                print(e, end=" ")


n, m, v = map(int, input().split())
edges = [[] for _ in range(n)]
visited = [0]*n
for _ in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    edges[st-1].append(ed)
    edges[ed-1].append(st)

for e in edges:
    e.sort()

dfs(v)
print()
visited = [0]*n
bfs(v)

```
| 결과 | 메모리 | 시간 | 코드길이 |
|:---:|:-----: | :---: | :----: |
| 맞았습니다 | 32372KB | 56ms | 728B |

## 3. 개선점
x
## 4. 개선사항

x

## 5. 개선사항 평가
x
