import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
# 1 ~ N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
nums = [i for i in range(1, N + 1)]
nCm = list(combinations(nums, M))
for c in nCm:
    print(" ".join(map(str, c)))