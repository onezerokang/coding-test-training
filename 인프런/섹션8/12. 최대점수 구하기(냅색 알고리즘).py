N, M = map(int, input().split())
dy = [0] * (M + 1)
for i in range(N):
    score, time = map(int, input().split())
    for j in range(M, time - 1, -1):
        dy[j] = max(dy[j], dy[j - time] + score)

print(dy[M])
