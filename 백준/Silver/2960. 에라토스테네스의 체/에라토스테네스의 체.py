import sys
input = sys.stdin.readline

n, k = map(int, input().split())

sevie = [True] * (n + 1)
cnt = 0

for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if sevie[j] != False:
                sevie[j] = False
                cnt += 1
                if cnt == k:
                    print(j)
                    break