import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, flooded):
    global dx, dy
    que = deque([[x, y]])
    flooded[x][y] = 2
    
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or flooded[nx][ny]:
                continue

            if not flooded[nx][ny]:
                que.append([nx, ny])
                flooded[nx][ny] = 2
        
result = 0
rain = 0
while True:
    flooded = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= rain:
                flooded[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not flooded[i][j]:
                bfs(i, j, flooded)
                cnt += 1
    
    if cnt == 0:
        break
    result = max(result, cnt)
    rain += 1
    
print(result)
