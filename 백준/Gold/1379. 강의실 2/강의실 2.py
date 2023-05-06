import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
room = [0] * (N + 1)
pq = []

arr.sort(key=lambda x: (x[1], x[2])) # 시작 시간 기준 정렬
cnt = 0
for no, start, end in arr:
    if pq and pq[0][0] <= start:
        room[no] = room[pq[0][2]]
        heappop(pq)
    else:
        cnt += 1
        room[no] = cnt
    
    heappush(pq, [end, start, no])

print(cnt)
for i in room[1:]:
    print(i)


