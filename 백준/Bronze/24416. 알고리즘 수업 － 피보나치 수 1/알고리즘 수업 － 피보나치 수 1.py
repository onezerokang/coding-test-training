import sys
input = sys.stdin.readline
n = int(input())

cnt1 = 0
cnt2 = 0

def fib(n):
    if n == 1 or n == 2:
        return 1
    
    global cnt1
    cnt1 += 1
    
    return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global cnt2

    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        cnt2 += 1
    return f[n]

fib(n)
fibonacci(n)
print(cnt1 + 1)
print(cnt2)