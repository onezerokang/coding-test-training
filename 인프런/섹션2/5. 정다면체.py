n, m = map(int, input().split())

sum_list = [0 for i in range(40)]
for num1 in range(1, n + 1):
    for num2 in range(1, m + 1):
        sum_list[num1 + num2] += 1

# 가장 많이 나온 수 찾기
high_count = max(sum_list)
 
result = [str(i) for i in range(len(sum_list)) if sum_list[i] == 4]
print(' '.join(result))