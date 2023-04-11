n, c = map(int, input().split())
stall_list = [int(input()) for _ in range(n)]
stall_list.sort()

lt = 1
rt = stall_list[n-1]
ret = 0

def count_horse(len):
    ep = stall_list[0]
    cnt = 1

    for i in range(1, n):
        if stall_list[i] -ep >= len:
            ep = stall_list[i]
            cnt += 1
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    
    if count_horse(mid) >= c:
        ret = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ret)