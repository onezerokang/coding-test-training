import sys
input = sys.stdin.readline
n = int(input())
score = list(map(int, input().split()))
high_score = max(score)

new_score = []

for s in score:
    new_score.append(s / high_score * 100)

print(sum(new_score) / n)