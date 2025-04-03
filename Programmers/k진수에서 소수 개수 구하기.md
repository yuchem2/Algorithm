# [Programmers] k 진수에서 소수 개수 구하기 (JS)
Programmers 코딩테스트 연습

ID: yuchem2@gmail.com

Date: 2025.04.03

소요시간: 10

## 1. 문제설명

### 문제
---

양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

+ 0P0처럼 소수 양쪽에 0이 있는 경우
+ P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
+ 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
+ P처럼 소수 양쪽에 아무것도 없는 경우
+ 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
  + 예를 들어, 101은 P가 될 수 없습니다.

예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.

정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.

### 제한사항
+ 1 ≤ n ≤ 1,000,000
+ 3 ≤ k ≤ 10
### 예제입출력
| n      | k  | result  |
|--------|----|---------|
| 437674 | 3  | 3       |
| 110011 | 10 | 2       |

## 2. 소스코드

### 알고리즘
해당 문제는 주어진 숫자 데이터를 k진수로 변경한 후 그 안에서 0을 기준으로 만들어지는 숫자 중에서 소수의 개수를 세는 문제이다.
간단한 소수 판별 알고리즘으로 문제를 해결할 수 있다. 소수 판별에서 걸리는 시간을 감소시키고자 메모니제이션을 추가하였다. 

### 코드
```javascript
function solution(n, k) {
    const memo = new Set(), exclude = new Set();
    const isPrime = (number) => {
        if (memo.has(number)) {
            return true;
        } else if(exclude.has(number)) {
            return false;
        }
        
        for (let i = 2; i <= Math.sqrt(number); i++) {
            if (number % i === 0) {
                exclude.add(number);
                return false;
            }
        }
        memo.add(number);
        return true; 
    }    
    
    return n.toString(k).split('0').reduce((acc, cur) => acc + (parseInt(cur) > 1 ? isPrime(cur) : 0), 0);
}
```
## 3. 개선점

## 4. 개선사항

## 5. 개선사항 평가
