from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)

def bfs(start, end):
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        curr, count = queue.popleft()
        up = curr + U
        down = curr - D
        
        if curr == end:
            return count
        
        if up <= F and not visited[up]:
            queue.append((up, count + 1))
            visited[up] = True
            
        if down > 0 and not visited[down]:
            queue.append((down, count + 1))
            visited[down] = True
    
    return "use the stairs"

print(bfs(S, G))