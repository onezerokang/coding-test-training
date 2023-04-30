import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = input().rstrip()

stack = []
cnt = 0

for num in nums:
    num = int(num)
    while stack and num > stack[-1] and k > cnt:
        stack.pop()
        cnt += 1
    stack.append(num)

for i in range(n - k):
    print(stack[i], end="")
    