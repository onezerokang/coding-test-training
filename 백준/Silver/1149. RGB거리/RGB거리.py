import sys
input = sys.stdin.readline

N = int(input())
homes = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 2, -1, -1):
    homes[i][0] += min(homes[i + 1][1], homes[i + 1][2])
    homes[i][1] += min(homes[i + 1][0], homes[i + 1][2])
    homes[i][2] += min(homes[i + 1][0], homes[i + 1][1])

print(min(homes[0]))