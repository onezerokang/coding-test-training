# 정렬로 풀기
# n = int(input())
# word = [input() for _ in range(n)]
# used = [input() for _ in range(n - 1)]

# word.sort()
# used.sort()

# for i in range(n):
#     used.append('')
#     if word[i] != used[i]:
#         print(word[i])
#         break

# 딕셔너리로 풀기
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1 

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)