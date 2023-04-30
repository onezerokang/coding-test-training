N = int(input()) # 동전 개수
coins = list(map(int, input().split())) # 동전 종류
M = int(input()) # 만들어야 하는 금액
dy = [0] + [501] * (M) # d[i]는 i원을 거슬러주는데 사용된 동전의 최소 개수

for coin in coins:
    for i in range(1, M + 1):
        # dy[i] = min(dy[i], dy[i % coin] + i // coin)
        dy[i] = min(dy[i], dy[i - coin] + 1)
    print(dy)

print(dy[M])