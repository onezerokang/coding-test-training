from collections import deque
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

# 사과 배치
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 2

L = int(input())
turn_info = {}
for _ in range(L):
    x, c = input().split()
    turn_info[int(x)] = c

# 0(상), 1(우), 2(하), 3(좌)
direction = 1
go_to = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sec = 0

head_x = 0
head_y = 0
curr_coord = deque([[0, 0]])

while True:
    sec += 1
    head_x += go_to[direction][0]
    head_y += go_to[direction][1]

    # 나한테 부딪혔을 때
    if head_x < 0 or head_x >= N or head_y < 0 or head_y >= N or [head_x, head_y] in curr_coord:
        break

    if board[head_x][head_y] != 2:
        tail_x, tail_y = curr_coord.popleft()
        board[tail_x][tail_y] = 0
    
    board[head_x][head_y] = 1
    curr_coord.append([head_x, head_y])

    if sec not in turn_info:
        continue

    if turn_info[sec] == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

print(sec)