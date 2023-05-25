import sys
input = sys.stdin.readline

N = int(input())
coord = list(map(int, input().split()))

coord2 = {}
for i, x in enumerate(sorted(list(set(coord)))):
    coord2[x] = i

for x in coord:
    print(coord2[x], end=" ")