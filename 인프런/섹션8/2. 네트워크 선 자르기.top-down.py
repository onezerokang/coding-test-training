n = int(input())

d = [0] * (n + 1)
def dfs(n):
    if n == 1 or n == 2:
        return n
    if d[n]:
        return d[n]
    d[n] = dfs(n - 1) + dfs(n - 2)
    return d[n]

print(dfs(n))