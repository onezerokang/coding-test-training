n = int(input())
bricks = [list(map(int, input().split())) for _ in range(n)]
bricks.insert(0, [0, 0, 0])
dy = [0] * (n + 1)
dy[1] = bricks[1][1]

for i in range(2, n + 1):
    for j in range(i - 1, 0, -1):
        # bricks[i]: 새로 쌓을 벽돌
        # bricks[j]: 기존 탑의 가장 윗 벽돌
        if (
                bricks[i][0] < bricks[j][0] and
                bricks[i][2] < bricks[j][2] and
                dy[i] < dy[j] + bricks[i][1]
           ):
            dy[i] = dy[j] + bricks[i][1]

print(max(dy))

# 정렬을 사용한 코드
n = int(input())
bricks = [list(map(int, input().split())) for _ in range(n)]
bricks.sort(key=lambda x: -x[0])
dy = [0] * n
dy[0] = bricks[0][1]

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if bricks[i][2] < bricks[j][2] and dy[i] < dy[j] + bricks[i][1]:
            dy[i] = dy[j] + bricks[i][1]

print(max(dy))