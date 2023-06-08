import sys
input = sys.stdin.readline

N = int(input())
homes = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 2, -1, -1):
    for j in range(3):
        if j == 0:
            homes[i][j] += min(homes[i + 1][1], homes[i + 1][2])
        elif j == 1:
            homes[i][j] += min(homes[i + 1][0], homes[i + 1][2])
        else:
            homes[i][j] += min(homes[i + 1][0], homes[i + 1][1])

print(min(homes[0]))