import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
words = set(words)
words = list(words)

words.sort(key=lambda w: (len(w), w))

for w in words:
    print(w)