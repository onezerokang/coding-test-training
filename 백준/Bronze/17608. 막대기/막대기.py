import sys
input = sys.stdin.readline
n = int(input())

stack = []

for _ in range(n):
    h = int(input())
    
    while True:
        if not stack or stack[-1] > h:
            break
        stack.pop()
    stack.append(h)


print(len(stack))
    