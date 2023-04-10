n = int(input())

def check_hansu(num):
    if 99 >= num:
        return True
    str_num = str(num)
    diff = int(str_num[0]) - int(str_num[1])
    for i in range(len(str_num)):
        if i == len(str_num) - 1:
            break
        if diff != int(str_num[i]) - int(str_num[i + 1]):
            return False
    return True

count = 0
for i in range(1, n + 1):
    if check_hansu(i):
        count += 1

print(count)