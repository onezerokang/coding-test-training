# 윤년 = 1, 아니면 = 0
# 조건: 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수

year = int(input())

if year % 400 == 0:
    print(1)
elif (year % 4 == 0) and (year % 100 != 0):
    print(1)
else:
    print(0)