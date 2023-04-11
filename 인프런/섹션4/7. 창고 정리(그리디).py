L = int(input())
storage = list(map(int, input().split()))
M = int(input()) # 조정 횟수

storage.sort(reverse=True)
print(storage)

high_index = 0
low_index = len(storage) - 1

for i in range(M):
    storage[high_index] -= 1
    storage[low_index] += 1

    storage.sort(reverse=True)

print(storage[high_index] - storage[low_index])