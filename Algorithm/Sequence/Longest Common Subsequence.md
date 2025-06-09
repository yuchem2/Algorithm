tags: `Sequence`, `LCS`, `DP`
## 개념
- 두 수열이 주어졌을 때, **순서를 유지하며 공통으로 등장하는 부분 수열 중 가장 긴 것**을 찾는 알고리즘
- 반드시 **연속된 값일 필요는 없고**, **순서만 일치**하면 됨.
- 핵심은 **DP 테이블을 통해 이전까지의 최적해**를 저장하며 진행하는 것
## 복잡도
> 문자열 A 길이 = n, 문자열 B 길이 = m
- **시간 복잡도**:
    - `O(n × m)` (DP 사용 시)
- **공간 복잡도**:
    - `O(n × m)` (전체 테이블 저장 시)
    - `O(min(n, m))` (최적화 시)
## 특징
- **DP 방식**: 두 수열을 비교하면서, 각 접점에서 가능한 최장 길이를 갱신.
- 두 수가 같을 경우 → 대각선 값 + 1
- 다를 경우 → 왼쪽 또는 위쪽 값 중 큰 값 선택
- **수열 길이만 구할 수도 있고**,  **실제 수열을 복원하려면 역추적이 필요**함.
## 예시
### python (길이 구하기)
```python
def lcs_length(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]
```
### python (실제 LCS 구하기)
```python
def get_lcs_sequence(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # DP 테이블 작성
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 역추적
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return result[::-1]
```