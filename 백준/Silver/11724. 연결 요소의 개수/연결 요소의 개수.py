import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visted[start] = True
    for i in graph[start]:
        if not visted[i]:
            dfs(i)

visted = [False] * (N + 1)
visted[0] = True
result = 0
while False in visted: # 모든 노드를 탐색할 때까지 루프
    start = visted.index(False)
    result += 1
    dfs(start)

print(result)