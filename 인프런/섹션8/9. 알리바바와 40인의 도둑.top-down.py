n = int(input())
vally = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)]

# 왼쪽은 x랑 y 1씩 줄이자
def dfs(x, y):
    if dy[x][y]:
        return dy[x][y]
    
    if x == 0 and y == 0:
        return vally[0][0]
    
    if y == 0:
        dy[x][y] = dfs(x - 1, y) + vally[x][y]
    elif x == 0:
        dy[x][y] = dfs(x, y - 1) + vally[x][y]
    else:
        dy[x][y] = min(dfs(x - 1, y), dfs(x, y - 1)) + vally[x][y]
    return dy[x][y]

print(dfs(n - 1, n - 1))