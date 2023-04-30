# 플로이드-워셜: 모든 정점 사이의 최단 경로를 찾는 알고리즘
# 1. 하나의 정점에서 다른 정점으로 바로 갈 수 있다면 최소 비용을, 갈 수 없다면 INF로 배열에 값을 젖아한다.
# 2. 3중 for문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값을 바꿔준다.
# 3. 위의 과정을 반복해서 모든 정점 사이의 최단 경로를 탐색한다.

n, m = map(int, input().split())
dist = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1): # 자기 자신으로 가는 비용을 0으로 초기화
    dist[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split()) # 자신과 바로 연결된 정점으로 가는 비용을 0으로 초기화
    dist[a][b] = c

for k in range(1, n + 1): # i 정점에서 k 경유지를 거쳐 j를 도착했을 때 비용이 더 적다면 교체
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == int(1e9):
            print('M', end=' ')
        else:
            print(dist[i][j], end = ' ')
    print()




