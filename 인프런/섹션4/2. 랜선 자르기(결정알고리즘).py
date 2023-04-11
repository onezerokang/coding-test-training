k, n = map(int, input().split())

def count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

line = [int(input()) for _ in range(k)]
largest = max(line)
ret = 0

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= n:
        ret = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(ret)
