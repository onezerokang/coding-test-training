n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

lp = rp = half = n // 2
ret = 0
for i in range(n):
    # lp ~ rp까지 더해야 한다.
    ret += sum(a[i][lp:rp+1])
    
    if i >= half:
        lp += 1
        rp -= 1
    else:
        lp -= 1 
        rp += 1

print(ret)