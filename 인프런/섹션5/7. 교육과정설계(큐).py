from collections import deque
required = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(required)
    for x in plan:
        if x in dq and x != dq.popleft():
            print(f'#{i+1} NO')
            break
    else:
        if len(dq) == 0:
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')