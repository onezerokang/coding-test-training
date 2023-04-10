word = input()

# 숫자를 누적시키는 두가지 방법
ret = ""
ret2 = 0
for w in word:
    if w.isdigit():
        ret += w
        ret2 *= 10 + int(w)

ret = int(ret)
cnt = 0
for i in range(1, ret + 1):
    if ret % i == 0:
        cnt += 1

print(ret)
print(cnt)

# 해설 코드
