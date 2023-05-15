import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    y = 0
    x = 1
    for _ in range(N):
        if y >= H:
            x += 1
            y = 0
        y += 1
        
    y = str(y)
    x = str(x)
    if len(x) == 1:
        x = "0" + x
        
    print(y, x, sep="")