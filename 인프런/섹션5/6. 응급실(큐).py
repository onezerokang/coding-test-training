from collections import deque

n, m = map(int, input().split())
Q = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)

cnt = 0
while True:
    curr = Q.popleft()
    if any(curr[1] < x[1] for x in Q):
        Q.append(curr)
    else:
        cnt += 1
        if curr[0] == m:
            print(cnt)
            break
