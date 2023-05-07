import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(x, y):
    if visited[x][y]:
        return
    
    visited[x][y] = True
    if floor[x][y] == "-":
        if y + 1 < M and floor[x][y + 1] == "-":
            dfs(x, y + 1)
    elif floor[x][y] == "|":
        if x + 1 < N and floor[x + 1][y] == "|":
            dfs(x + 1, y)

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j)

print(cnt)