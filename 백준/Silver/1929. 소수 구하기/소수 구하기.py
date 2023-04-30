m, n = map(int, input().split())
# m 이상 n 이하 소수 구하기

def eratosthenes(m, n):
    # m부터 n까지 체를 만든다
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, n + 1):
        if sieve[i]:
            if i >= m:
                primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return primes

primes = eratosthenes(m, n)
for p in primes:
    print(p)