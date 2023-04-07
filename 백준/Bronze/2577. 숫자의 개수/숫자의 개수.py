a = int(input())
b = int(input())
c = int(input())

calc_result = str(a * b * c)
a_list = [0 for i in range(10)]

for c in calc_result:
    a_list[int(c)] += 1

for num in a_list:
    print(num)