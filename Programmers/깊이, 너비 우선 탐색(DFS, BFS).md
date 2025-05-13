# [Programmers] 깊이, 너비 우선 탐색(DFS, BFS) (PYTHON)
Programmers 코딩테스트 연습: https://school.programmers.co.kr/learn/courses/30/lessons/87694

ID: yuchem2@gmail.com

Date: 2025.05.13

소요시간: 1시간

## 1. 문제설명

### 문제
---
다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.

![image](https://github.com/user-attachments/assets/6ca716e3-8f83-4e83-abc7-a7f803bd265e)

지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.

만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.

![image](https://github.com/user-attachments/assets/a6456099-2de7-4578-a0b4-cf6980f32db9)

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.

![image](https://github.com/user-attachments/assets/cc08fe52-c6d3-4cff-93f8-883f732ba75c)

즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.

다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.

![image](https://github.com/user-attachments/assets/3266a108-45a3-4cc0-8369-922926e58f46)

한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

![image](https://github.com/user-attachments/assets/3217f76b-48ff-41cc-90ee-72ff0845921f)

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

### 제한사항
+ rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
+ rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
  + 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
  + 서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
  + 문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
+ charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
  + 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
+ itemX, itemY는 1 이상 50 이하인 자연수입니다.
  + 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
+ 캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
---
+ 전체 배점의 50%는 직사각형이 1개인 경우입니다.
+ 전체 배점의 25%는 직사각형이 2개인 경우입니다.
+ 전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.
 
### 예제입출력
| rectangle                                 | characterX | characterY | itemX | itemY | result  |
|-------------------------------------------|------------|------------|-------|-------|---------|
| [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]] | 1          | 3          | 7     | 8     | 17      |
| [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]] | 9          | 7          | 6     | 1     | 11      |
| [[1,1,5,7]]                               | 1          | 1          | 4     | 7     | 9       |
| [[2,1,7,5],[6,4,10,10]]                   | 3          | 1          | 7     | 10    | 15      |
| [[2,2,5,5],[1,3,6,4],[3,1,4,6]]           | 1          | 4          | 6     | 3     | 10      |


## 2. 소스코드

### 알고리즘
해당 문제는 주어진 사각형들에서 겹치는 부분을 제외한 외곽 테두리만을 이동해 캐릭터에서 아이템으로 이동할 수 있는 가장 짧은 경로를 찾는 문제이다.

그러므로 가장 짭은 경로는 DFS 혹은 BFS로 해결하고, 테두리를 찾는 것에 집중하면 된다. 

여기서 테두리를 찾는 것 자체는 바로 해결했으나, 다음 이동 경로를 확정시키는 것에 어려움이 있었다. 왜냐하면, 단순하게 두 좌표의 길이를 1로 설정하면, 선끼리의 구분이 어렵기 때문이다.

그러므로 모든 좌표에 2를 곱하여 선끼리에 확실한 구분이 가능하도록 수정하여 문제를 해결할 수 있었다.

### 코드
```python
from collections import deque

def isOutline(x, y, rectangle, include):
    for i in range(len(rectangle)):
        if i == include: continue
        if rectangle[i][0] * 2 < x < rectangle[i][2] * 2 and rectangle[i][1] * 2 < y < rectangle[i][3] * 2: return False
    return True

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # map 초기화
    limitX, limitY = 101, 101 # 50 * 2
    geoMap = [[0 for _ in range(limitY)] for _ in range(limitX)]
    for i in range(len(rectangle)):
        x1, y1, x2, y2 = map(lambda x: x * 2, rectangle[i])
        for tx in range(x1, x2 + 1):
            if isOutline(tx, y1, rectangle, i):
                geoMap[y1][tx] = 1
            if isOutline(tx, y2, rectangle, i):
                geoMap[y2][tx] = 1
        for ty in range(y1, y2 + 1):
            if isOutline(x1, ty, rectangle, i):
                geoMap[ty][x1] = 1
            if isOutline(x2, ty, rectangle, i):
                geoMap[ty][x2] = 1
    geoMap[itemY * 2][itemX * 2] = -1
    # print(geoMap)
    # bfs 수행
    queue = deque([[characterX * 2, characterY * 2, 0]])
    visit = set([(characterX * 2, characterY * 2)])
    while queue:
        x, y, l = queue.popleft()
        if geoMap[y][x] == -1:
            answer = l // 2
            break
        
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nxtX, nxtY = x + dx, y + dy
            if 0 <= nxtX < limitX and 0 <= nxtY < limitY and geoMap[nxtY][nxtX] != 0 and (nxtX, nxtY) not in visit:
                visit.add((nxtX, nxtY))
                queue.append([nxtX, nxtY, l + 1])
    
    return answer

```
## 3. 개선점
x
## 4. 개선사항
x
## 5. 개선사항 평가
x
