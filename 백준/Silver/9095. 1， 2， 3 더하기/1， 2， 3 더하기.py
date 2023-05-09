import sys;
input = sys.stdin.readline

def dfs(n):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    return dfs(n - 1) + dfs(n - 2) + dfs(n - 3)

T = int(input())
for i in range(T):
    n = int(input())
    print(dfs(n))