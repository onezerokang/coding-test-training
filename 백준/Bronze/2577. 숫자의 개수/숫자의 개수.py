a = int(input())
b = int(input())
c = int(input())
calc_result = str(a * b * c)

check_list = [0] * 10
for i in range(len(calc_result)):
    check_list[int(calc_result[i])] += 1

for num in check_list:
    print(num)