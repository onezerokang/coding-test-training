N = int(input())
dist = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dist[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

low_score = int(1e9)
for i in range(1, N + 1):
    low_score = min(low_score, max(dist[i]))

chairman_list = []
for i in range(1, N + 1):
    if max(dist[i]) == low_score:
        chairman_list.append(i)

print(low_score, len(chairman_list))
for c in chairman_list:
    print(c, end = ' ')


# Input
# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 2 4
# 5 3
# -1 -1