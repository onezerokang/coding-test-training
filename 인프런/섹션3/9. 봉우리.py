n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * (n + 2))
a.append([0] * (n + 2))

for row in a:
    row.insert(0,0)
    row.append(0)


cnt = 0
for i in range(n+2):
    if i == 0 or i == n + 1:
        continue

    for j in range(n+2):
        if j == 0 or j == n + 1:
            continue

        # 상하좌우 비교
        curr = a[i][j]
        t = a[i - 1][j]
        b = a[i + 1][j]
        l = a[i][j-1]
        r = a[i][j+1]

        if curr > t and curr > b and curr > l and curr > r:
            cnt += 1

print(cnt)
