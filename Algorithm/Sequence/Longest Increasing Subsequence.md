tags: `Sequence`, `LIS`, `DP`
## 개념
+ 수열에서 순서를 유지하면서 가장 길게 증가하는 부분 수열을 찾는 알고리즘.
- 반드시 **연속된 값**일 필요는 없고, **순서만 유지**되면 됨.
- 핵심은 이전까지의 최적해를 활용하여 다음 상태를 빠르게 계산하는 것.
- 이진 탐색을 활용하면 `O(n log n)` 시간에 해결 가능.
## 복잡도
> 수열 길이 = n
- 시간 복잡도
    - `O(n²)` (DP만 사용 시)
    - `O(n log n)` (DP + 이진 탐색 사용 시)
- 공간 복잡도: `O(n)`
## 특징
- DP 방식은 각 위치에서 가능한 이전 수들을 모두 확인하여 최적 값을 찾음.
- 이진 탐색 방식은 현재 수를 넣을 **최적 위치를 빠르게 찾아** 수열을 유지함.
- 길이만 구하는 경우와 실제 수열을 구하는 경우가 나뉨.
    - 길이만 구하는 것은 간단하지만,
    - 수열 자체를 구하려면 역추적이 필요함.
## 예시
### python (길이 구하기 O(nlogn))
```python
import bisect

def length_of_lis(seq):
    lis = []
    for num in seq:
        idx = bisect.bisect_left(lis, num)
        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num
    return len(lis)

```
### python (실제 LIS 구하기 O(nlogn))
```python
import bisect

def get_lis_sequence(seq):
    n = len(seq)
    lis = []
    index = [0] * n  # 각 요소가 LIS 배열의 어디에 들어갔는지 저장

    for i in range(n):
        pos = bisect.bisect_left(lis, seq[i])
        if pos == len(lis):
            lis.append(seq[i])
        else:
            lis[pos] = seq[i]
        index[i] = pos

    # LIS 수열 복원
    lis_length = len(lis)
    result = []
    for i in range(n - 1, -1, -1):
        if index[i] == lis_length - 1:
            result.append(seq[i])
            lis_length -= 1
    return result[::-1]

```