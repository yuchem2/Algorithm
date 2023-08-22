
## baekjoon Problem10872
## input: number n = 3^k (1<= k <8)
## output: star list
## 2023-03-16


def Star(n):
    if n == 3:
        return ["***", "* *", "***"]
    arr = Star(n//3)
    stars = []

    for i in arr:
        stars.append(i * 3)
    for i in arr: 
        stars.append(i+" "*(n//3)+i)
    for i in arr:
        stars.append(i * 3)
    return stars


n = int(input())
print('\n'.join(Star(n)))