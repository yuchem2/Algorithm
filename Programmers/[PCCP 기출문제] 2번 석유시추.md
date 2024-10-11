# [Programmers]  [PCCP 기출문제] 2번 석유시추 (PYTHON)
Programmers 코딩테스트 연습: https://school.programmers.co.kr/learn/courses/30/lessons/250136

ID: yuchem2@gmail.com

Date: 2024.10.11

소요시간: 20~30분

## 1. 문제설명

### 문제
---
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

세로길이가 n 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견되었습니다. 석유는 여러 덩어리로 나누어 묻혀있습니다. 당신이 시추관을 수직으로 단 하나만 뚫을 수 있을 때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚫을 수 없습니다.

![image](https://github.com/user-attachments/assets/3237021d-bd5c-4407-a478-e55cbfb8ba02)

예를 들어 가로가 8, 세로가 5인 격자 모양의 땅 속에 위 그림처럼 석유가 발견되었다고 가정하겠습니다. 상, 하, 좌, 우로 연결된 석유는 하나의 덩어리이며, 석유 덩어리의 크기는 덩어리에 포함된 칸의 수입니다. 그림에서 석유 덩어리의 크기는 왼쪽부터 8, 7, 2입니다.

![image](https://github.com/user-attachments/assets/c6c8891f-293b-4e64-91af-8e0c14e93ea2)

시추관은 위 그림처럼 설치한 위치 아래로 끝까지 뻗어나갑니다. 만약 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다. 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다. 시추관을 설치한 위치에 따라 뽑을 수 있는 석유량은 다음과 같습니다.

|시추관의 위치|	획득한 덩어리	|총 석유량|
| :--: | :--: | :--: |
|1	|[8]|	8|
|2	|[8]|	8|
|3	|[8]|	8|
|4	|[7]|	7|
|5	|[7]|	7|
|6	|[7]|	7|
|7	|[7, 2]|	9|
|8	|[2]|	2|

오른쪽 그림처럼 7번 열에 시추관을 설치하면 크기가 7, 2인 덩어리의 석유를 얻어 뽑을 수 있는 석유량이 9로 가장 많습니다.

석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 land가 매개변수로 주어집니다. 이때 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요.


### 제한사항
+ 1 ≤ land의 길이 = 땅의 세로길이 = n ≤ 500
  + 1 ≤ land[i]의 길이 = 땅의 가로길이 = m ≤ 500
  + land[i][j]는 i+1행 j+1열 땅의 정보를 나타냅니다.
  + land[i][j]는 0 또는 1입니다.
  + land[i][j]가 0이면 빈 땅을, 1이면 석유가 있는 땅을 의미합니다.

정확성 테스트 케이스 제한사항
+ 1 ≤ land의 길이 = 땅의 세로길이 = n ≤ 100
+ 1 ≤ land[i]의 길이 = 땅의 가로길이 = m ≤ 100

효율성 테스트 케이스 제한사항
+ 주어진 조건 외 추가 제한사항 없습니다.

 
### 예제입출력
|land|	result|
| :-- | :-- |
|[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]|	9|
|[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]] |	16|

## 2. 소스코드

### 알고리즘
해당 문제는 DFS 혹은 BFS 기법을 사용하면 금방 해결할 수 있는 문제이다.
1. 주어진 배열을 순회하면서 석유가 있는 지점을 찾는다.
2. 석유가 있는 지점을 찾으면 그 때부터 BFS or DFS를 이용해 인접한 부분(상하좌우)에 석유가 있는지 순회를 하며 석유블럭을 탐색한다.
3. 탐색하면서 석유블럭에 번호를 매기고, 그 석유블럭의 크기를 저장한다.
4. 1~3 과정을 통해 배열의 모든 요소를 탐색할 때까지 반복한다.
5. 모든 과정이 끝나면, 다시 한번 배열을 순회한다. 이때 열 기준으로 탐색을 진행한다. 탐색을 진행하면서 석유블럭이 잇는 지점은 그 블럭의 번호를 기록한다.
6. 한 열의 탐색이 끝나면, 만난 석유블럭의 크기를 모두 더한 결과를 계산한다.
7. 5~6 과정을 모든 열에 수행을 하면 각 열에서 얻을 수 있는 총 석유량이 나오게 된다. 이 중 가장 큰 석유량을 리턴하면 된다.

### 코드
```python
def get_points(i, j):
    return [[i-1, j], [i, j-1], [i, j+1], [i+1, j]]


def solution(land):
    answer = 0
    visit = [[0] * len(land[i]) for i in range(len(land))]

    ## 석유 탐색
    stack = []
    petroleum = []
    for i in range(len(land)):
        for j in range(len(land[0])):
            if visit[i][j] == 0:
                if land[i][j] == 1:
                    stack.append([i, j])
                else:
                    visit[i][j] = -1
            size = 0
            while stack:
                cur = stack.pop()
                if land[cur[0]][cur[1]] == 1 and visit[cur[0]][cur[1]] == 0:
                    visit[cur[0]][cur[1]] = len(petroleum) + 1
                    size += 1
                else:
                    visit[cur[0]][cur[1]] = -1
                    continue
                points = get_points(cur[0], cur[1])
                for x, y in points:
                    if x < 0 or x >= len(land):
                        continue
                    if y < 0 or y >= len(land[0]):
                        continue
                    if visit[x][y] == 0:
                        stack.append([x, y])
            if size > 0:
                petroleum.append(size)

    ## 총 석유량 계산
    for j in range(len(visit[0])):
        check = []
        for i in range(len(visit)):
            if visit[i][j] > 0:
                if visit[i][j] not in check:
                    check.append(visit[i][j])
        cur_amount = sum([petroleum[x-1] for x in check])
        if cur_amount > answer:
            answer = cur_amount
    return answer
```
## 3. 개선점
x
## 4. 개선사항
x
## 5. 개선사항 평가
x
