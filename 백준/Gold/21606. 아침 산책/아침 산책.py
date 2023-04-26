import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().rstrip()))

result = 0
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    if A[u] == 1 and A[v] == 1: # 실내가 인접되어 있으면
        result += 2 # 경로를 2개 추가한다.

def dfs(start, inside_cnt):
    visited[start] = True

    for v in graph[start]:
        if visited[v]:
            continue

        if A[v] == 1: # 도착 지점이 실내면
            inside_cnt += 1
        else: # 도착 지점이 실외면
            inside_cnt = dfs(v, inside_cnt)
    
    return inside_cnt

visited = [False] * (N + 1)
for i in range(1, N + 1):
    if A[i] == 0 and not visited[i]: # 시작 지점이 실외면
        inside_cnt = dfs(i, 0)
        result += inside_cnt * (inside_cnt - 1)

print(result)