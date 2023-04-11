n = int(input())

meeting = [(a, b) for _ in range(n) for a, b in [map(int, input().split())]]

meeting.sort(key=lambda x: (x[1], x[0]))

ep = 0
cnt = 0

for s, e in meeting:
    if s >= ep:
        ep = e
        cnt += 1

print(cnt)