# 각 행과 각 열, 그리고 9개의 3x3 보드에 1 ~ 9가 중복없이 나타나면 된다.
a = [list(map(int, input().split())) for _ in range(9)]

for x in a:
    print(x)

ch1 = [0] * 10
ch2 = [0] * 10
ret = "YES"
for i in range(9):
    for j in range(9):
        ch1[a[i][j]] = 1
        ch2[a[j][i]] = 1
    
    if sum(ch1) != 9 or sum(ch2) != 9:
        ret = "NO"
        break
    
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                ret = "NO"
                break
        
print(ret)