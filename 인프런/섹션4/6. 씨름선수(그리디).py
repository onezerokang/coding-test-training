n = int(input())
pro = [(height, weight) for height, weight in [map(int, input().split()) for _ in range(n)]]
pro.sort(reverse=True)

cnt = 0
largest = 0

for height, weight in pro:
    if weight > largest:
        cnt += 1
        largest = weight

print(cnt)