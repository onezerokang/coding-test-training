import sys
from collections import deque

input = sys.stdin.readline
n , k = map(int, input().split())

dq = deque([i for i in range(1, n + 1)])
order = []
i = 1

while dq:
    x = dq.popleft()
    if i == k:
        order.append(x)
        i = 1
    else:
        dq.append(x)
        i += 1

result = "<"
for i in range(len(order)):
    result += str(order[i])
    if i != len(order) - 1:
        result += ", "

result += ">"

print(result)