N = int(input())

# 철수가 올라갈 수 있는 방법의 수
d = [0] * (N + 1)
def dfs(n):
    if n == 1 or n == 2:
        return n
    if d[n]:
        return d[n]
    d[n] = dfs(n - 1) + dfs(n - 2)
    return d[n]

print(dfs(N))