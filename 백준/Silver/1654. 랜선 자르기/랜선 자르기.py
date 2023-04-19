import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan_list = [int(input()) for _ in range(k)]

pl = 1
pr = max(lan_list)
result = 0

while pl <= pr:
    cnt = 0
    cut_len = (pl + pr) // 2

    for lan in lan_list:
        cnt += (lan // cut_len)

    if n > cnt:
        pr = cut_len - 1
    else:
        pl = cut_len + 1
        result = cut_len
print(result)
