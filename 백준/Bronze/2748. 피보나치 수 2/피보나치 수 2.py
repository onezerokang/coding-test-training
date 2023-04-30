n = int(input())

d = [0] * (n + 1)

def fibo(n):
    if n <= 1:
        return n
    if d[n]:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]

print(fibo(n))