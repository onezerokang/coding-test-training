from collections import deque
import sys
input = sys.stdin.readline

# 게임판 생성
N = int(input())
board = [[0] * N for _ in range(N)]

# 사과 배치
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 2

# 방향 정보 저장
L = int(input())
turn_info = {}
for _ in range(L):
    X, C = input().split()
    turn_info[int(X)] = C

# 뱀 좌표
snake_coord = deque()
snake_coord.append([0, 0])
head_row = 0
head_col = 0

# 뱀 이동 방향
# 상(0) -> 우(1) -> 하(2) -> 좌(3)
# left로 방향전환 할 경우 - 1
# right로 방향전환 할 경우 + 1
direction = 1
move_to = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 게임 시작
sec = 0
while True:
    sec += 1
    # 방향에 맞게 뱀 좌표 이동
    head_row += move_to[direction][0]
    head_col += move_to[direction][1]

    # 몸에 부딪히거나 벽에 부딪히면 게임 종료
    if head_row < 0 or head_row >= N or head_col < 0 or head_col >= N or [head_row, head_col] in snake_coord:
        break

    # 이동한 곳에 사과가 없으면 꼬리 제거
    if board[head_row][head_col] != 2:
        tail_row, tail_col = snake_coord.popleft()
        board[tail_row][tail_col] = 0
    
    # 뱀 좌표 저장
    board[head_row][head_col] = 1
    snake_coord.append([head_row, head_col])

    # 방향 전환: 현재 게임 진행 시간이 일치한다면 방향을 전환해야 함.
    if sec in turn_info:
        if turn_info[sec] == 'L':
            direction = (direction - 1) % 4 # 0미만이 나오거나
        else:
            direction = (direction + 1) % 4 # 0 ~ 3 범위를 벗어나지 못하게 하기 위해 4의 나머지를 이용

print(sec)
