n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    row_num, dire, move_num = map(int, input().split())
    
    if dire == 0:
        # 왼쪽 이동
        for i in range(move_num):
            a[row_num - 1].append(a[row_num - 1].pop(0))
    else:
        # 오른쪽 이동
        for i in range(move_num):
            a[row_num - 1].insert(0, a[row_num - 1].pop())

# 몇 개인지 카운트
lp = 0
rp = n
ret = 0
for i in range(n):
    ret += sum(a[i][lp:rp])

    if i < n // 2:
        lp += 1
        rp -= 1
    else:
        lp -= 1
        rp += 1

print(ret)