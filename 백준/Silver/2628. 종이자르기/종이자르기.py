w, h = map(int, input().split())
n = int(input())

col = [0, w]
row = [0, h]

for _ in range(n):
    xy, cut = map(int, input().split())
    
    if xy == 0:
        row.append(cut)
    else:
        col.append(cut)

row.sort()
col.sort()

result = 0
for i in range(len(row) - 1):
    for j in range(len(col) - 1):
        a = row[i+1] - row[i]
        b = col[j+1] - col[j]
        if a * b > result:
            result = a * b

print(result)