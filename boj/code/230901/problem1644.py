def eratos(n):
    prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i + i, n + 1, i):
                prime[j] = False

    array = [i for i in range(2, n + 1) if prime[i]]
    return array


def problem1644():
    n = int(input())
    if n == 1:
        print(0)
        return
    else:
        prime = eratos(n)
        i, j = 0, 0
        cnt, cumulative = 0, prime[i]
        while i <= j < len(prime):
            if cumulative >= n:
                if cumulative == n:
                    cnt += 1
                cumulative -= prime[i]
                i += 1
            elif j == len(prime)-1:
                break
            else:
                j += 1
                cumulative += prime[j]
        print(cnt)


problem1644()
