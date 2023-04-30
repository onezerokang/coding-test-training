import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

tree = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = []
    if b not in tree:
        tree[b] = []
    tree[a].append(b)
    tree[b].append(a)

visted = [False] * (N + 1)
parents = [0] * (N + 1)

def bfs(start):
    queue = deque([start])
    visted[start] = True

    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True
                parents[i] = v

bfs(1)

for i in range(2, len(parents)):
    print(parents[i])