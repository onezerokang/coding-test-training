n = int(input())
score_list = map(int, input().split())

total_score = 0
bonus = 0
for score in score_list:
    if score == 0:
        bonus = 0
        continue
    bonus += 1
    total_score += bonus

print(total_score)