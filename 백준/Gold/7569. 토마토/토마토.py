import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
queue = deque()

for z in range(H):
    tmp = []
    for y in range(N):
        tmp.append(list(map(int, input().split())))
        for x in range(M):
            if tmp[y][x] == 1:
                queue.append((z, y, x))
    graph.append(tmp)

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

while queue:
    z, y, x = queue.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
            queue.append((nz, ny, nx))
            graph[nz][ny][nx] = graph[z][y][x] + 1

day = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                print(-1)
                exit()
            day = max(day, graph[z][y][x])

print(day - 1)