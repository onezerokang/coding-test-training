import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

result = 0
plugs = []
for i in range(len(a)):
    if a[i] in plugs:
        continue
    if len(plugs) < N:
        plugs.append(a[i])
        continue

    idxs = []
    for j in range(N):
        try:
            idx = a[i:].index(plugs[j])
        except:
            idx = 101
        idxs.append(idx)
    
    out = idxs.index(max(idxs))
    plugs[out] = a[i]
    result += 1

print(result)
