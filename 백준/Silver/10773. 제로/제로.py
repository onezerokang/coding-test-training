import sys
input = sys.stdin.readline
k = int(input())

s = []

for _ in range(k):
    n = int(input())
    if n == 0:
        del s[-1]
        continue
    s.append(n)

print(sum(s))