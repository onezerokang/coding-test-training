import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

max_price = max(price[:-1])
min_price = min(price[:-1])

ret = 0
for i in range(N - 1):
    if price[i] == max_price:
        ret += price[i] * road[i]
    elif price[i] == min_price:
        ret += price[i] * sum(road[i:])

print(ret)