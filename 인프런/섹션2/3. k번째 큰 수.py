n, k = map(int, input().split())
card_list = list(map(int, input().split()))

res=set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(card_list[i], card_list[j], card_list[m])

res = list(res)
res.sort(reverse=True)

print(res[k - 1])