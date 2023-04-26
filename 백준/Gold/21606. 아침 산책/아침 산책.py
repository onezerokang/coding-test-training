import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip()))

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

def dfs(start):
    global result
    visted[start] = True

    for v in graph[start]:
        if visted[v]:
            continue

        if A[v - 1] == 1: # 도착 지점이 실내면
            result += 1
            visted[v] = True
        else: # 도착 지점이 실외면
            dfs(v)


for i in range(1, N + 1):
    if A[i - 1] == 1: # 시작 지점이 실내면
        visted = [False] * (N + 1)
        dfs(i)

print(result)