n = int(input())
score_list = list(map(int, input().split()))

average = round(sum(score_list) / n)
min = float('inf')

for index, x in enumerate(score_list):
    score_diff = abs(average - x)
    if score_diff < min:
        min = score_diff
        score = x
        res = index + 1
    elif score_diff==min:
        if x > score:
            score = x
            res= index + 1

print(average, res)
