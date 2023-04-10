# 해설
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)

# 혼자 작성한 코드 - O(n^2)
# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# val = 0
# cnt = 0
# for i in range(n):
#     for j in range(i, n):
#         val += a[j]
#
#         if val > m:
#             val = 0
#             break;
#         elif val == m:
#             cnt += 1
#             val = 0
#             break;
#
# print(cnt)
