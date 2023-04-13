def addZero(num):
    num = str(num)
    if len(num) == 1:
        num = "0" + num
    return str(num)

def calc(num):
    num = addZero(num)
    sum = addZero(str(int(num[0]) + int(num[1])))
    new_num = num[1] + sum[1]
    return int(new_num)


n = new_num = int(input())
is_start = False
cnt = 0

while True:
    if is_start and n == new_num:
        break

    is_start = True
    new_num = calc(new_num)
    cnt += 1
    
print(cnt)
