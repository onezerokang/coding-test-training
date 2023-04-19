n = int(input())
nums = map(int, input().split())

min_value = 1000001
max_value = -1000001

for num in nums:
    if min_value > num:
        min_value = num
    if max_value < num:
        max_value = num

print(min_value, max_value)
