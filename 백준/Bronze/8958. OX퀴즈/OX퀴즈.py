n = int(input())

for _ in range(n):
    score = input()
    result = 0
    combo = 0
    for x in score:
        if x == 'O':
            result += 1 + combo
            combo += 1
        else:
            combo = 0
    print(result)
