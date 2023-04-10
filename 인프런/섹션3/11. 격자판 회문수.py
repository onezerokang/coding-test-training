board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        temp = board[j][i:i+5]
        if temp == temp[::-1]:
            cnt += 1
        
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1                

print(cnt)