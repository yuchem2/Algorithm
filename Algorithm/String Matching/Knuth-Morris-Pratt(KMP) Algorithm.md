tags: `String Matching`
## 개념
+ 문자열에서 특정 패턴을 효율적으로 찾는 알고리즘
+ 문자열 비교 중 실패가 발생했을 때, 이미 비교한 정보를 활용해 불필요한 비교를 줄여 빠르게 다음 비교 위치로 이동
+ 핵심은 패턴 내에서 접두사와 접미사의 겹치는 부분을 미리 계산하여 재사용하는 것.
## 복잡도
> 패턴 길이 = m, 텍스트 길이 = n
+ 시간 복잡도: `O(n + m)`
	+ 패턴 전처리(접두사 함수 계산): `O(m)`
	+ 텍스트 탐색: `O(n)`
+ 공간 복잡도: `O(m)`
	+ 텍스트 길이와는 상관없이 패턴 길이 m만큼의 추가 메모리가 필요 (접두사 함수)
## 특징
- 실패했을 때 텍스트 인덱스는 그대로 두고, 패턴 인덱스만 이동시켜 비교를 계속합니다.
- 패턴 내 중복된 부분을 활용해 점프할 위치를 미리 계산해둠 (접두사 함수 또는 실패 함수).
- 모든 매칭 위치를 찾을 수 있음.
## 예시
### python
```python
def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0  # 이전까지 일치한 길이

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    j = 0  # 패턴 인덱스

    positions = []  # 패턴이 나타나는 위치 저장 (1-based)
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i - m + 2)  # 1-based index
            j = pi[j - 1]
    return positions
```