# BFS 풀이
from collections import deque

N = int(input())
valley = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visted = [[int(1e9)] * N for _ in range(N)]
    visted[x][y] = valley[x][y]

    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나면 continue
            if nx >= N or ny >= N:
                continue

            # visted 표기 더 작은 경우에만
            if visted[nx][ny] > valley[nx][ny] + visted[x][y]:
                visted[nx][ny] = valley[nx][ny] + visted[x][y]
            
            q.append([nx, ny])
    
    return visted[N - 1][N - 1] 

print(bfs(0, 0))

# 강사님 코드(다이나믹 풀이)
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)]
dy[0][0]=arr[0][0]

for i in range(1, n):
    dy[0][i]=dy[0][i-1]+arr[0][i]
    dy[i][0]=dy[i-1][0]+arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]

print(dy[n-1][n-1])

# Input
# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3 
# 5 4 3 2 1 
# 1 7 5 2 4