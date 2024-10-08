# [Programmers] [PCCP 기출문제] 4번 수식 복원하기 (PYTHON)
Programmers 코딩테스트 연습: https://school.programmers.co.kr/learn/courses/30/lessons/340210

ID: yuchem2@gmail.com

Date: 2024.10.06

소요시간: 2시간

## 1. 문제설명

### 문제
---

당신은 덧셈 혹은 뺄셈 수식이 여러 개 적힌 고대 문명의 유물을 찾았습니다. 이 수식들을 관찰하던 당신은 이 문명이 사용하던 진법 체계가 10진법이 아니라는 것을 알아냈습니다. (2 ~ 9진법 중 하나입니다.)

수식들 중 몇 개의 수식은 결괏값이 지워져 있으며, 당신은 이 문명이 사용하던 진법에 맞도록 지워진 결괏값을 채워 넣으려 합니다.

다음은 그 예시입니다.

<수식>
```
14 + 3 = 17
13 - 6 = X
51 - 5 = 44
```
+ X로 표시된 부분이 지워진 결괏값입니다.

51 - 5 = 44에서 이 문명이 사용하던 진법이 8진법임을 알 수 있습니다. 따라서 13 - 6 = X의 지워진 결괏값을 채워 넣으면 13 - 6 = 5가 됩니다.

다음은 또 다른 예시입니다.

<수식>
```
1 + 1 = 2
1 + 3 = 4
1 + 5 = X
1 + 2 = X
```
주어진 수식들에서 이 문명에서 사용한 진법이 6 ~ 9진법 중 하나임을 알 수 있습니다.
1 + 5 = X의 결괏값은 6진법일 때 10, 7 ~ 9진법일 때 6이 됩니다. 이와 같이 결괏값이 불확실한 수식은 ?를 사용해 1 + 5 = ?와 같이 결괏값을 채워 넣습니다.
1 + 2 = X의 결괏값은 6 ~ 9진법에서 모두 3으로 같습니다. 따라서 1 + 2 = X의 지워진 결괏값을 채워 넣으면 1 + 2 = 3이 됩니다.

덧셈 혹은 뺄셈 수식들이 담긴 1차원 문자열 배열 expressions가 매개변수로 주어집니다. 이때 결괏값이 지워진 수식들의 결괏값을 채워 넣어 순서대로 문자열 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

### 제한사항
+ 2 ≤ expressions의 길이 ≤ 100
  + expressions의 원소는 "A + B = C" 혹은 "A - B = C" 형태의 문자열입니다. A, B, C와 연산 기호들은 공백 하나로 구분되어 있습니다.
  + A, B는 음이 아닌 두 자릿수 이하의 정수입니다.
  + C는 알파벳 X 혹은 음이 아닌 세 자릿수 이하의 정수입니다. C가 알파벳 X인 수식은 결괏값이 지워진 수식을 의미하며, 이러한 수식은 한 번 이상 등장합니다.
  + 결괏값이 음수가 되거나 서로 모순되는 수식은 주어지지 않습니다.

### 예제입출력
| expressions |	result |
| :--: | :--: |
|["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]|	["13 - 6 = 5"]|
|["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]|	["1 + 5 = ?", "1 + 2 = 3"]|
|["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]|	["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"]|
|["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]|	["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"]|
|["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]|	["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"]|

## 2. 소스코드

### 알고리즘

처음 문제를 접근하는 방식을 잘못 접근하여 처음부터 문제를 다시 푸느라 시간이 소요되었다.

처음에 시도한 방법은 
1. 먼저 expression을 순회하며 각 자릿수의 최대 수(0-8)을 찾는다.
2. 찾는 작업을 하면서, X가 있는 수식과 없는 수식으로 구분한다.
3. X가 없는 수식에서는 진법을 유추할 수 있으므로, 유추를 시도하고, 유추 결과가 맞지 않는 경우 가능한 진법을 검사하여, 정확한 값이 나오고 + 최대자릿수에서 값이 변경되는 구분을 구별한다.
4. 이 결과를 통해 X를 ?와 답으로 예측한다.

위 결과는 틀릴 수 밖에 없는데, 단순하게 가능한 진법의 수를 무조건 1개로 생각한 상태로 X의 결과를 예측하는 풀이였기 때문이다.  테스트 케이스는 모두 통과할 수 있어도, 그 외의 경우에서는 탐색을 못할 수 있는 가능성이 존재한다.

하지만 위 풀이에서 1, 2번과정은 맞다고 생각해 문제를 다른 방식으로 접근하였다.

1. 먼저 expression을 순회하며 각 자릿수의 최대 수(0-8)을 찾는다.
2. 찾는 작업을 하면서, X가 있는 수식과 없는 수식으로 구분한다.
3. 각 자릿수의 최대수를 찾았기 때문에 그 수 이하의 진법은 수식의 진법이 될 수 없다. 이 근거를 통해 가능한 진법의 배열을 만든다.
4. X가 없는 수식을 순회하며 수식의 결과와 예측한 수식의 결과가 동일한 진법들을 찾는다. 만약, 결과가 다른 경우가 존재하면, 그 진법은 가능하지 않기 때문에 제외한다.
5. 위 과정을 통해 최종적으로 주어진 수식에서 가능한 진법들을 추려냈다. 만약 가능한 진법이 1개이면, 그 진법의 연산 결과로 모든 X를 채운다.
6. 만약 가능한 진법이 2개 이상인 경우 X가 있는 수식에서 해당 진법을 모두 적용한 뒤 그 결과들이 모두 같으면, 그 결과를 X로 하고, 만약 하나라도 다른 결과가 있는 경우 ?로 바꾼다.

위 풀이을 통해 문제를 해결할 수 있었다.

```ps
이중 반복을 사용하지 않으려다가 오히려 문제르 해결하는데 오래걸리는 문제가 발생하였다.
n의 수가 적으면 여러 조건을 넣는 것 보단 순회가 나은 것 같다.
하지만, 이 부분도 다양한 경우가 있을 테니 항상 생각을 더 해보자.
```

### 코드
```python
def get_result(a, op, b, system):
    if op == '+':
        return int(a, system) + int(b, system)
    else:
        return int(a, system) - int(b, system)
    
def get_max_system(a, system):
    target = int(a)
    result = system
    while target > 0:
        temp = target % 10
        target = target // 10
        if result < temp + 1:
            result = temp + 1
            
    return result

def get_real_result(a, system):
    if a == 0:
        return '0'
    target = ''
    while a > 0:
        target += str(a % system)
        a = a // system
    return target[::-1]
    
    
def solution(expressions):
    answer = []
    
    system = 2
    targets = []
    predicts = []
    for e in expressions:
        a, op, b, _, result = e.split(' ')
        system = get_max_system(a, system)
        system = get_max_system(b, system)
        if result == 'X':
            targets.append([a, op, b, _, result])
        else:
            predicts.append([a, op, b, result])
            system = get_max_system(result, system)
    
    systems = [x for x in range(system, 10)]
    
    for p in predicts:
        if len(systems) == 1:
            break
        for s in systems.copy():
            result = get_result(p[0], p[1], p[2], s)
            predict_result = int(p[3], s)
            if result != predict_result:
                systems.remove(s)
    
    for t in targets:
        if len(systems) == 1:
            t[4] = get_real_result(get_result(t[0], t[1], t[2], systems[0]), systems[0])
        else:
            results = []
            for s in systems:
                result = get_real_result(get_result(t[0], t[1], t[2], s), s)
                if len(results) > 0 and result not in results:
                    t[4] = '?'
                    break
                else:
                    results.append(result)
            if len(results) == len(systems):
                t[4] = results[0]
                
        answer.append(' '.join(t))
        
    return answer
```
## 3. 개선점
x
## 4. 개선사항
x
## 5. 개선사항 평가
x
