calc_exp = input().split('-')

tmp = []
for term in calc_exp:
    tmp_result = 0
    for num in term.split('+'):
        tmp_result += int(num)
    tmp.append(tmp_result)

result = tmp[0]
for i in range(1, len(tmp)):
    result -= tmp[i]

print(result)