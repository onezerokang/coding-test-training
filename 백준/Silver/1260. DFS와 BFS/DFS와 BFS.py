import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for row in graph:
    row.sort()

def DFS(start):
    visted[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visted[i]:
            DFS(i)


def BFS(start):
    queue = deque([start])
    visted[start] = True

    while queue:
        a = queue.popleft()
        
        print(a, end=' ')
        for i in graph[a]:
            if not visted[i]:
                visted[i] = True
                queue.append(i)
        

visted = [False] * (N + 1)
DFS(V)
print()
visted = [False] * (N + 1)
BFS(V)