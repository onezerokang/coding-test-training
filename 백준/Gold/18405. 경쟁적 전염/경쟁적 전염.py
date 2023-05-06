import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

virus = []
graph = []

for x in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

    for y in range(N):
        if row[y] > 0:
            virus.append([row[y], x, y, 0])

virus.sort()

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(S, X, Y):
    queue = deque()
    for v in virus:
        queue.append(v)
    
    while queue:
        _type, x, y, time = queue.popleft()

        if time == S:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                queue.append((_type, nx, ny, time + 1))
                graph[nx][ny] = _type
    return graph[X - 1][Y - 1]

print(bfs(S, X, Y))
