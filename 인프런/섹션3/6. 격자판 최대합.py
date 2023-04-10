n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

high_sum = -2147000000

for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        # 좀 더 생각해보기
        print(f'({i}, {j}): {a[i][j]}')
        print(f'({j}, {i}): {a[j][i]}')

        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > high_sum:
        high_sum = sum1
    if sum2 > high_sum:
        high_sum = sum2

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > high_sum:
    high_sum = sum1
if sum2 > high_sum:
    high_sum = sum2

print(high_sum)

        
        