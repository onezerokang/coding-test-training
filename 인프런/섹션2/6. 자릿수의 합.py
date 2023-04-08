n = int(input())
num_list = list(map(int, input().split()))

def digit_sum(x):
    result = 0
    for x in str(x):
        result += int(x)
    return result

max = -2147000000
index = 0
for num in num_list:
    sum_result = digit_sum(num)
    if max < sum_result:
        max = sum_result
        res = num

print(res)
