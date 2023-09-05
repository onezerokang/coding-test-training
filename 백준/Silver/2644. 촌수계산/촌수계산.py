import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, end, depth):
    if node == end:
        print(depth)
        exit(0)
    
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i, end, depth + 1)

dfs(a, b, 0)
print(-1)