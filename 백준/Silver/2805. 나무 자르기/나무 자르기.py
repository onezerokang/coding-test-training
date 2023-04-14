import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

pl = 1
pr = max(trees)
result = 0

while pl <= pr:
    pc = (pl + pr) // 2
    sum = 0
    for t in trees:
        if t - pc > 0:
            sum += t- pc
    
    if sum == m:
        result = pc
        break
    elif sum > m:
        result = pc
        pl = pc + 1
    else:
        pr = pc - 1

print(result)