import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
cards = deque([i for i in range(1, n + 1)])

is_to_delete = True

while len(cards) > 1:
    if is_to_delete:
        cards.popleft()
    else:
        c = cards.popleft()
        cards.append(c)

    is_to_delete = not is_to_delete

print(cards.pop())
