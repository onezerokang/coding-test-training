from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, start, end):
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        v, d = queue.popleft()
        
        for i in graph[v]:
            if i == end:
                return d + 1
                        
            if not visited[i]:
                queue.append((i, d + 1))
                visited[i] = True
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

print(bfs(graph, visited, start, end))