# 일의 선후관계를 유지하면서 전체 일의 순서를 짜는 알고리즘
# 위상정렬에서는 진입 차수가 중요하다.

# 1. 그래프를 구현한다
# 2. 각 노드의 진입 차수를 저장할 배열을 하나 만든다.
# 3. 큐에 진입 차수가 0인 데이터를 먼저 넣는다
# 4. 큐를 pop할 진입 차수를 -1 해준다.
# 5. 모든 노드의 진입차수가 0이 될 때까지 위 작업을 반복한다.

from collections import deque
N, M = map(int, input().split())

degree = [0] * (N + 1) # 진입 차수 기록
graph = [[0] * (N + 1) for _ in range(N + 1)]
dq = deque()

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1

for i in range(1, N + 1):
    if degree[i] == 0:
        dq.append(i)

while dq:
    x = dq.popleft()
    print(x, end = ' ')
    for i in range(1, N + 1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)