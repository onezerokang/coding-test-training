import sys
input = sys.stdin.readline
n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

pl = 1
pr = houses[-1] - houses[0]
result = 0

while pl <= pr:
    pc = (pl + pr) // 2
    recent = houses[0]
    cnt = 1
    
    for i in range(1, n):
        if houses[i] - recent >= pc:
            recent = houses[i]
            cnt += 1
    if cnt >= c:
        if pc > result:
            result = pc
        pl = pc + 1
    else:
        pr = pc - 1

print(result)