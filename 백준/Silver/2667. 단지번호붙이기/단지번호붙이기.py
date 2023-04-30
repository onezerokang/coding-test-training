import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    house_cnt = 0

    while q:
        x, y = q.popleft()
        if graph[x][y] == 1:
            graph[x][y] = -1
            house_cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] <= 0:
                continue

            if [nx, ny] not in q:
                q.append([nx, ny])
    return house_cnt

group_cnt = 0
house_cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            group_cnt += 1
            house_cnt.append(bfs(i, j))

# 각 단지 내 집 수를 오름차순 정렬
house_cnt.sort()
print(group_cnt)
for i in house_cnt:
    print(i)
