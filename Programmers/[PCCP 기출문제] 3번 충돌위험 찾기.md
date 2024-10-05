# [Programmers] [PCCP 기출문제] 3번 충돌위험 찾기 (PYTHON)
Programmers 코딩테스트 연습: 

ID: yuchem2@gmail.com

Date: 2024.10.05

소요시간: 45분

## 1. 문제설명

### 문제
---
어떤 물류 센터는 로봇을 이용한 자동 운송 시스템을 운영합니다. 운송 시스템이 작동하는 규칙은 다음과 같습니다.

1. 물류 센터에는 (r, c)와 같이 2차원 좌표로 나타낼 수 있는 n개의 포인트가 존재합니다. 각 포인트는 1~n까지의 서로 다른 번호를 가집니다.
2. 로봇마다 정해진 운송 경로가 존재합니다. 운송 경로는 m개의 포인트로 구성되고 로봇은 첫 포인트에서 시작해 할당된 포인트를 순서대로 방문합니다.
3. 운송 시스템에 사용되는 로봇은 x대이고, 모든 로봇은 0초에 동시에 출발합니다. 로봇은 1초마다 r 좌표와 c 좌표 중 하나가 1만큼 감소하거나 증가한 좌표로 이동할 수 있습니다.
4. 다음 포인트로 이동할 때는 항상 최단 경로로 이동하며 최단 경로가 여러 가지일 경우, r 좌표가 변하는 이동을 c 좌표가 변하는 이동보다 먼저 합니다.
5. 마지막 포인트에 도착한 로봇은 운송을 마치고 물류 센터를 벗어납니다. 로봇이 물류 센터를 벗어나는 경로는 고려하지 않습니다.

이동 중 같은 좌표에 로봇이 2대 이상 모인다면 충돌할 가능성이 있는 위험 상황으로 판단합니다. 관리자인 당신은 현재 설정대로 로봇이 움직일 때 위험한 상황이 총 몇 번 일어나는지 알고 싶습니다. 만약 어떤 시간에 여러 좌표에서 위험 상황이 발생한다면 그 횟수를 모두 더합니다.

운송 포인트 n개의 좌표를 담은 2차원 정수 배열 points와 로봇 x대의 운송 경로를 담은 2차원 정수 배열 routes가 매개변수로 주어집니다. 이때 모든 로봇이 운송을 마칠 때까지 발생하는 위험한 상황의 횟수를 return 하도록 solution 함수를 완성해 주세요.

### 제한사항


+ 2 ≤ points의 길이 = n ≤ 100
  + points[i]는 i + 1번 포인트의 [r 좌표, c 좌표]를 나타내는 길이가 2인 정수 배열입니다.
  + 1 ≤ r ≤ 100
  + 1 ≤ c ≤ 100
  + 같은 좌표에 여러 포인트가 존재하는 입력은 주어지지 않습니다.
+ 2 ≤ routes의 길이 = 로봇의 수 = x ≤ 100
  + 2 ≤ routes[i]의 길이 = m ≤ 100
  + routes[i]는 i + 1번째 로봇의 운송경로를 나타냅니다. routes[i]의 길이는 모두 같습니다.
  + routes[i][j]는 i + 1번째 로봇이 j + 1번째로 방문하는 포인트 번호를 나타냅니다.
  + 같은 포인트를 연속으로 방문하는 입력은 주어지지 않습니다.
  + 1 ≤ routes[i][j] ≤ n

### 예제입출력
| points |	routes	| result |
| :--: | :--: | :--: |
|[[3, 2], [6, 4], [4, 7], [1, 4]]|	[[4, 2], [1, 3], [2, 4]] |	1 |
|[[3, 2], [6, 4], [4, 7], [1, 4]]|	[[4, 2], [1, 3], [4, 2], [4, 3]]|	9|
|[[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]] |	[[2, 3, 4, 5], [1, 3, 4, 5]]|	0|


## 2. 소스코드

### 알고리즘

해당 문제는 (1) 먼저 주어진 경로의 시점과 종점을 통해 특정 경로를 파악한 후 (2) 구해진 경로를 한칸씩 움직이며 로봇의 충돌 횟수를 세는 문제이다.

경로를 탐색해야 한다는 점에서, 최단거리 알고리즘을 생각했으나, 간선의 비용이 모두 동일하기 때문에, 모든 경로를 똑같은 규칙을 통해 시점에서 종점으로 갈 수 있도록 구현하여 경로를 계산할 수 있었다.

경로를 계산한 다음 순회를 진행하면 되는데, 여기서 중요한 점은 충돌횟수를 세는 시점에서, 현재 이미 충돌이 발생한 point에서 또 다른 충돌이 발생하더라도 동일한 충돌로 본다는 점이다.

이를 유의해서 각 시점에 이미 충돌이 발생한 point에서 또 충돌이 발생할 경우의 예외처리만 해주면 풀리는 문제였다. 

### 코드
```python
def solution(points, routes):
    answer = 0

    robot_route_list = []
    for route in routes:
        robot_route = []
        st = points[route[0]-1].copy()
        for i in range(1, len(route)):
            end = points[route[i]-1].copy()
            while st[0] != end[0]:
                temp = st.copy()
                robot_route.append(temp)
                if st[0] < end[0]:
                    st[0] += 1
                else:
                    st[0] -= 1
            while st[1] != end[1]:
                temp = st.copy()
                robot_route.append(temp)
                if st[1] < end[1]:
                    st[1] += 1
                else:
                    st[1] -= 1
        robot_route.append(st)
        robot_route_list.append(robot_route.copy())
        
    empty = 0
    while empty != len(robot_route_list):
        robot_position = []
        danger_position = []
        empty = 0
        for r in robot_route_list:
            if len(r) == 0:
                empty += 1
                continue
            position = r.pop(0)
            if position in robot_position and position not in danger_position:
                answer += 1
                danger_position.append(position)
            else:
                robot_position.append(position)

    return answer
```
## 3. 개선점
x
## 4. 개선사항
x
## 5. 개선사항 평가
x
