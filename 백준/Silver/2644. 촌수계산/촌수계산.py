# DFS 풀이
from collections import deque
import sys
input = sys.stdin.readline
           
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = -1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, depth):
    visited[node] = True

    if node == end:
        global result
        result = depth

    for i in graph[node]:
        if not visited[i]:
            dfs(i, depth + 1)

dfs(start, 0)

print(result)