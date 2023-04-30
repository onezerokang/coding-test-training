n = int(input())
nums = list(map(int, input().split()))
nums.insert(0, 0)
dy = [1] * (n + 1)
dy[1] = 1

for i in range(2, n + 1):
    for j in range(1, i):
        if nums[i] > nums[j] and dy[i] < dy[j] + 1:
            dy[i] = dy[j] + 1

print(max(dy))