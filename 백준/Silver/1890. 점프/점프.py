import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

def dfs(x, y):
    if x >= N or y >= N:
        return 0
    if x == N - 1 and y == N - 1:
        return 1
    if matrix[x][y] == 0:
        return 0

    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = dfs(x + matrix[x][y], y) + dfs(x, y + matrix[x][y])
    return dp[x][y]

print(dfs(0, 0))