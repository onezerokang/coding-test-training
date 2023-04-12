w, h = map(int, input().split())
n = int(input())

row_list = [0, w]
col_list = [0, h]

for _ in range(n):
    xy, length = map(int, input().split())
    if xy == 0:
        col_list.append(length)
    else:
        row_list.append(length)

row_list.sort()
col_list.sort()

result = 0
for i in range(1, len(row_list)):
    for j in range(1, len(col_list)):
        w = row_list[i] - row_list[i-1]
        h = col_list[j] - col_list[j-1]
        result = max(result, w * h)
print(result)