import sys
input = sys.stdin.readline
n, c = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()

start = 1 # 최소 거리
end = h[-1] - h[0] # 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    curr = h[0] # 첫번째 집에 공유기 설치
    cnt = 1
    
    for i in range(1, n):
        if h[i] - curr >= mid:
            cnt += 1
            curr = h[i]
            
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
