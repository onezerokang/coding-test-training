import sys
input = sys.stdin.readline

a = input().rstrip().split('-')

nums = []
for i in a:
    s = map(int, i.split('+'))
    nums.append(sum(s))

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)
