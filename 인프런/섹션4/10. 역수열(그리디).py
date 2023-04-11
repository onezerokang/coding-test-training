# 역수열: 내 앞에 나보다 큰 수가 몇개가 있는가

N = int(input())
a = list(map(int, input().split()))
seq = [0] * N

for i in range(N):
    for j in range(N):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=" ")
    
