N, M = map(int, input().split())
dy = [0] * (M + 1) # dy[j]는 가방에 j 무게만큼 담는다고 했을 때 최대 보석 값

for i in range(N):
    w, v = map(int, input().split())
    for j in range(w, M + 1):
        dy[j] = max(dy[j], dy[j - w] + v)

print(dy[M])