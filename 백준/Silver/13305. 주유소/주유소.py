import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

max_price = max(price[:-1])
min_price = min(price[:-1])

ret = 0

for i in range(N - 1):
    next_city = 0
    for j in range(i + 1, N - 1):
        if price[i] > price[j]:
            next_city = j
            break
    if next_city:
        ret += price[i] * sum(road[i:next_city])
        i = next_city
    else:
        ret += price[i] * sum(road[i:])
        break

print(ret)