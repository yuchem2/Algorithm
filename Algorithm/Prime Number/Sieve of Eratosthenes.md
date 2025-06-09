tags: `Prime Number`
## 개념
+ 어떤 자연수 n 이하의 모든 소수를 찾는 알고리즘
+ 2부터 시작해서 자신의 배수들을 제거하면서 남은 수들이 소수라는 점을 이용
+ 즉, 2의 배수, 3의 배수, 5의 배수 등을 차례로 제거해가면서 소수를 얻음
## 복잡도
+ 시간복잡도: `O(nloglogn)`
+ 공간복잡도: `O(n)`
## 특징
+ 매울 효율적인 소수 판별법 중 하나
+ 소수를 구하는 데 가장 널리 쓰이며, 구현도 간단
## 예시
### Python
```python
def sieve(n):
	"""
	n = 1 이상의 정수
	"""
    prime = [True] * (n + 1)  # 0부터 n까지 True 초기화
    prime[0], prime[1] = False, False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            # i의 배수들을 False 처리 (i*i부터 시작)
            for j in range(i*i, n+1, i):
                prime[j] = False

    # 소수 리스트 만들기
    primes = [i for i in range(2, n+1) if prime[i]]
    return primes
```