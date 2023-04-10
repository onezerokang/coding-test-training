n = int(input())

# 정렬, 중복 x
a_list = [int(input()) for _ in range(n)]
a_list.sort()
for num in a_list:
    print(num)