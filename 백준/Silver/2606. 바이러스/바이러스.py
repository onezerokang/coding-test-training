# 바이러스
import sys
N = int(sys.stdin.readline()) # 컴퓨터 개수
M = int(sys.stdin.readline()) # 간선 수

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global result
    result += 1
    visted[v] = True
    for i in graph[v]:
        if not visted[i]:
            dfs(i)

result = -1 # 1은 감염한 컴퓨터로 세지 않는다.
visted = [False] * (N + 1)
dfs(1)
print(result)