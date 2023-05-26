from sys import stdin
N = int(stdin.readline().strip())
X = list(map(int, stdin.readline().strip().split()))
cpy  = list(set(X))
cpy.sort()
ans,cnt={},0
for i in cpy:
    ans[i] = cnt
    cnt+=1
for idx in X:
    print(ans[idx],end=" ")