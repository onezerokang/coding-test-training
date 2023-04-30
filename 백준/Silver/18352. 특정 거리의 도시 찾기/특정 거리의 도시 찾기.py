import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    queue = deque()
    queue.append(start)
    visted = [-1] * (N + 1)
    visted[start] = 0

    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visted[i] == -1:
                visted[i] = visted[v] + 1
                queue.append(i)

    is_exist = False
    for i in range(1, N + 1):
        if visted[i] == K:
            print(i)
            is_exist = True
    
    if not is_exist:
        print(-1)
bfs(X)