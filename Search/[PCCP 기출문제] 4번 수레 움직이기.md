tags: `Programmers`, `Graph`, `BFS/DFS`
# [Programmers] [PCCP 기출문제] 4번 수레 움직이기 (PYTHON)
Programmers 코딩테스트 연습: https://school.programmers.co.kr/learn/courses/30/lessons/250134

ID: yuchem2@gmail.com

Date: 2024.10.15

소요시간: 1시간

## 1. 문제설명

### 문제
---
n x m 크기 격자 모양의 퍼즐판이 주어집니다.

퍼즐판에는 빨간색 수레와 파란색 수레가 하나씩 존재합니다. 각 수레들은 자신의 시작 칸에서부터 자신의 도착 칸까지 이동해야 합니다.
모든 수레들을 각자의 도착 칸으로 이동시키면 퍼즐을 풀 수 있습니다.

당신은 각 턴마다 반드시 모든 수레를 상하좌우로 인접한 칸 중 한 칸으로 움직여야 합니다. 단, 수레를 움직일 때는 아래와 같은 규칙이 있습니다.

+ 수레는 벽이나 격자 판 밖으로 움직일 수 없습니다.
+ 수레는 자신이 방문했던 칸으로 움직일 수 없습니다.
+ 자신의 도착 칸에 위치한 수레는 움직이지 않습니다. 계속 해당 칸에 고정해 놓아야 합니다.
+ 동시에 두 수레를 같은 칸으로 움직일 수 없습니다.
+ 수레끼리 자리를 바꾸며 움직일 수 없습니다.

예를 들어, 아래 그림처럼 n = 3, m = 2인 퍼즐판이 있습니다.

+ 속이 빨간색인 원은 빨간색 수레를 나타냅니다.
+ 속이 파란색인 원은 파란색 수레를 나타냅니다.
+ 테두리가 빨간색인 원은 빨간색 수레의 도착 칸을 나타냅니다.
+ 테두리가 파란색인 원은 파란색 수레의 도착 칸을 나타냅니다.

![image](https://github.com/user-attachments/assets/4d450afd-d821-4458-b936-46396c9b8fcd)


위 퍼즐판은 아래와 같은 순서로 3턴만에 풀 수 있습니다.

![image](https://github.com/user-attachments/assets/40d4acf7-91bd-4971-b4b9-a6337fdf64ac)

+ 빨간색 사선이 처진 칸은 빨간색 수레가 방문했던 칸을 나타냅니다. 규칙에 따라 빨간색 수레는 빨간색 사선이 처진 칸(방문했던 칸)으로는 이동할 수 없습니다.
+ 파란색 사선이 처진 칸은 파란색 수레가 방문했던 칸을 나타냅니다. 규칙에 따라 파란색 수레는 파란색 사선이 처진 칸(방문했던 칸)으로는 이동할 수 없습니다.

![image](https://github.com/user-attachments/assets/64b249c3-e000-486b-95b5-adf7b91154a2)

+ 위처럼 동시에 수레를 같은 칸으로 움직일 수는 없습니다.

퍼즐판의 정보를 나타내는 2차원 정수 배열 maze가 매개변수로 주어집니다. 퍼즐을 푸는데 필요한 턴의 최솟값을 return 하도록 solution 함수를 완성해 주세요. 퍼즐을 풀 수 없는 경우 0을 return 해주세요.

### 제한사항

+ 1 ≤ maze의 길이 (= 세로 길이) ≤ 4
  + 1 ≤ maze[i]의 길이 (= 가로 길이) ≤ 4
  + maze[i][j]는 0,1,2,3,4,5 중 하나의 값을 갖습니다.

| maze[i][j]	|의미|
| :--: | :--: |
|0	|빈칸|
|1|	빨간 수레의 시작 칸|
|2|	파란 수레의 시작 칸|
|3|	빨간 수레의 도착 칸|
|4|	파란 수레의 도착 칸|
|5|	벽|

+ 빨간 수레의 시작 칸, 빨간 수레의 도착 칸, 파란 수레의 시작 칸, 파란 수레의 도착 칸은 퍼즐판에 1개씩 존재합니다.
 
### 예제입출력
|maze	|result|
| :--: | :--: |
|[[1, 4], [0, 0], [2, 3]]	|3|
|[[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]	|7|
|[[1, 5], [2, 5], [4, 5], [3, 5]]	|0|
|[[4, 1, 2, 3]]|	0|


## 2. 소스코드

### 알고리즘
처음에는 두 수레를 동시에 bfs 혹은 dfs를 이용해 탐색하면서 문제를 해결하고자 하였다. 그러나 이 방식으로 코드를 작성하자 코드의 조건이 너무 많이 첨가되어 복잡해지는 경향이 존재하였다. 그래서 다음과 같은 방법으로 문제를 해결하였다.

1. BFS를 통해 각 수레를 도착점까지 진행하는 가능한 모든 경로를 탐색한다. 이때 지나온 경로를 다시 탐색하지 않고, 벽을 통과하지 못하는 조건만을 기준으로 탐색을 진행한다.
2. 탐색이 완료되면 두 수레가 도착점에 도달할 수 있는 모든 경로가 탐색된다. 탐색결과를 검사하면서 검사하지 않은 나머지 조건(두 수레가 자리를 바꾸며 이동, 현재 이동할 위치에 수레가 있는 경우)을 검사한다.
3. 모든 조건을 만족하는 경로가 발견된 경우 그 경로의 길이가 현재 최단 경로보다 작은 경우 최단 경로를 해당 경로로 업데이트한다.

위 방법을 통해 문제를 해결할 수 있었다. 


### 코드
```python
from collections import deque

def solution(maze):
    def bfs(start, end):
        queue = deque()
        queue.append([start, [start]])
        
        paths = []
        while queue:
            cur, path = queue.popleft()
            if len(path) >= 16: 
                continue
            if cur == end:
                paths.append(path)
                continue
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nxt = [cur[0] + x, cur[1] + y]
                if 0 <= nxt[0] < len(maze) and 0 <= nxt[1] < len(maze[0]):
                    if nxt not in walls and nxt not in path:
                        queue.append([nxt, path + [nxt]])
        return paths
    
    
    answer = 17
    walls = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                r_start = [i, j]
            elif maze[i][j] == 2:
                b_start = [i, j]
            elif maze[i][j] == 3:
                r_end = [i, j]
            elif maze[i][j] == 4:
                b_end = [i, j]
            elif maze[i][j] == 5:
                walls.append([i, j])
    
    r_paths = bfs(r_start, r_end)
    b_paths = bfs(b_start, b_end)
    
    for r_path in r_paths:
        for b_path in b_paths:
            if len(r_path) < len(b_path):
                long_path = b_path
                short_path = r_path
            else:
                long_path = r_path
                short_path = b_path
            if len(long_path) - 1 > answer:
                continue
            
            for i in range(len(long_path) - 1):
                if i < len(short_path) - 1:
                    short_i = i
                else:
                    short_i = -1
                if long_path[i] == short_path[short_i]:
                    break
                if short_i != -1:
                    if long_path[i+1] == short_path[short_i] and long_path[i] == short_path[short_i+1]:
                        break
            else:
                answer = min(answer, len(long_path) - 1)
    
    return answer if answer != 17 else 0
```
## 3. 개선점
x
## 4. 개선사항
x
## 5. 개선사항 평가
x
