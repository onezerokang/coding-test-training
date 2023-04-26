import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip()))

result = 0
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    if A[u - 1] == 1 and A[v - 1] == 1: # 실내가 인접되어 있으면
        result += 2 # 경로를 2개 추가한다.

def dfs(start, inside_cnt):
    visted[start] = True

    for v in graph[start]:
        if visted[v]:
            continue

        if A[v - 1] == 1: # 도착 지점이 실내면
            inside_cnt += 1
            visted[v] = True
        else: # 도착 지점이 실외면
            inside_cnt += dfs(v, inside_cnt)
    
    return inside_cnt

inside_cnt = 0
visted = [False] * (N + 1)
for i in range(1, N + 1):
    if A[i - 1] == 0: # 시작 지점이 실외면
        inside_cnt = dfs(i, inside_cnt)

result += inside_cnt * (inside_cnt - 1)
print(result)