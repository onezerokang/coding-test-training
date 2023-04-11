N = int(input())
a = list(map(int, input().split()))

lt = 0
rt = N - 1
last = 0
ret = ""

while lt <= rt:
    temp = []
    if a[lt] > last:
        temp.append((a[lt], "L"))
    if a[rt] > last:
        temp.append((a[rt], "R"))
    temp.sort()

    if len(temp) == 0:
        break
    last = temp[0][0]
    ret += temp[0][1]
    if temp[0][1] == "L":
        lt += 1
    else:
        rt -= 1

print(len(ret))
print(ret)