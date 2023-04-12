# 해쉬 스타일로 풀기
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) -1

for key in sH.keys():
    if sH.get(key) != 0:
        print("NO")
        break
else:
    print("YES")


# 정렬로 풀기
a = "".join(sorted(input()))
b = "".join(sorted(input()))

ret = "YES" if a == b else "NO"
print(ret)