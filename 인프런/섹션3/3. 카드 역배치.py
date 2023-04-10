a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        # 시작지점에서 1씩 더했고
        # 끝 지점에서 1씩 빼기
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)

for n in a:
    print(n, end=" ")