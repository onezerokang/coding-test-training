import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100_001

def bfs(start, end, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        curr, sec = queue.popleft()
        sec += 1
        
        if curr == end:
            return sec - 1
        if curr < 100_000 and not visited[curr + 1]:
            queue.append((curr + 1, sec))
            visited[curr + 1] = True
        if curr > 0 and not visited[curr - 1]:
            queue.append((curr - 1, sec))
            visited[curr - 1] = True
        if curr * 2 < 100_001 and not visited[curr * 2]:
            queue.append((curr * 2, sec))
            visited[curr * 2] = True

print(bfs(N, K, visited))