N = int(input())
nums = list(map(int, input().split()))
nums.insert(0, 0)
dy = [1] * (N + 1)
dy[1] = 1

# nums에서 최대 부분 증가수열을 구해야 한다.
for i in range(2, N + 1):
    for j in range(i - 1, 0, -1):
        if nums[i] > nums[j] and dy[i] < dy[j] + 1:
            dy[i] = dy[j] + 1

print(max(dy))