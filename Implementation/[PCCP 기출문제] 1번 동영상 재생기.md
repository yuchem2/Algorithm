tags: `Programmers`, `Implementation`
# [Programmers] [PCCP 기출문제] 1번 동영상 재생기 (PYTHON)
Programmers 코딩테스트 연습: https://school.programmers.co.kr/learn/courses/30/lessons/340213

ID: yuchem2@gmail.com

Date: 2024.10.04

## 1. 문제설명

### 문제
---
당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.

10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

### 제한사항
+ video_len의 길이 = pos의 길이 = op_start의 길이 = op_end의 길이 = 5
  + video_len, pos, op_start, op_end는 "mm:ss" 형식으로 mm분 ss초를 나타냅니다.
  + 0 ≤ mm ≤ 59
  + 0 ≤ ss ≤ 59
  + 분, 초가 한 자리일 경우 0을 붙여 두 자리로 나타냅니다.
  + 비디오의 현재 위치 혹은 오프닝이 끝나는 시각이 동영상의 범위 밖인 경우는 주어지지 않습니다.
  + 오프닝이 시작하는 시각은 항상 오프닝이 끝나는 시각보다 전입니다.
+ 1 ≤ commands의 길이 ≤ 100
  + commands의 원소는 "prev" 혹은 "next"입니다.
  + "prev"는 10초 전으로 이동하는 명령입니다.
  + "next"는 10초 후로 이동하는 명령입니다.
 

### 예제입출력

| video_len |	pos |	op_start |	op_end |	commands |	result |
| :--: | :--: | :--: | :--: | :--: | :--: |
|"34:33" |	"13:00"|	"00:55"|	"02:55"|	["next", "prev"]|	"13:00"|
|"10:55"|	"00:05"|	"00:15"|	"06:55"|	["prev", "next", "next"]|	"06:55"|
|"07:22"|	"04:05"|	"00:15"	|"04:07"|	["next"]| "04:17" |


## 2. 소스코드

### 알고리즘
해당 문제는 단순히 명령에 따라 현재 동영상에 시점을 옮기는 문제로서, 주의할 점은 두 가지이다.
1. 동영상의 전체 길이의 범위를 벗어나지 말 것. (0 ≤ pos ≤ video_len)
2. 현재 동영상의 시간(pos)가 오프닝 시점에 있는 경우 무조건 op_end로 현재시간을 이동할 것

이 두 경우만 신경쓴다면 쉽게 풀 수 있는 문제이다.


### 코드
```python
def time_to_second(time):
    min, second = time.split(':')
    return int(min) * 60 + int(second)

def second_to_time(second):
    return "%02d:%02d" % (second // 60, second % 60)  
    

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    len = time_to_second(video_len)
    st = time_to_second(pos)
    op_st = time_to_second(op_start)
    op_ed = time_to_second(op_end)
    
    for command in commands:
        if op_st <= st and st <= op_ed:
            st = op_ed
        if command == 'next':
            st += 10
            if st > len:
                st = len
        else: 
            st -= 10
            if st < 0:
                st = 0
                
    if op_st <= st and st <= op_ed:
        st = op_ed
    
    answer = second_to_time(st)
    return answer
```
## 3. 개선점
x
## 4. 개선사항
x

## 5. 개선사항 평가
x
