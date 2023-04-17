import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input()

stack = []
cnt = 0
for i in range(n):
    while stack and stack[-1] < num[i] and cnt < k:
        stack.pop()
        cnt += 1
    
    stack.append(num[i])

while len(stack) > n - k:
    stack.pop()

for x in stack:
    print(x, end="")
