n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 큰 동전이 작은 동전들의 배수이기 때문에
# 나눌 수 있는 가장 큰 값으로 나눠보고
# 안되면 한칸씩 내려서 나눈다.

result = 0
for i in range(len(coins) - 1, -1, -1):
    if k == 0:
        break
    if k // coins[i] != 0:
        result += k // coins[i]
        k %= coins[i]

print(result)