# 별 찍기 19의 규칙
# 1. N번째 결과는 (4 * N - 3)의 크기이다.
# 2. N이 하나씩 줄 때마다 x, y 좌표가 각각 2씩 증가한다.

# 알고리즘
# 0. (4 * n - 3)의 제곱인 2차원 배열을 생성한다.
# 1. n == 1이면 x, y좌표에 별을 하나 찍는다.
# 2. 바깥 테두리부터 좌표를 찾아가며 별을 찍는다.
n = int(input())
lens = 4 * n - 3
stars = [[' '] * lens for _ in range(4 * n - 3)]

def fill_star(n, coord):
    if n == 1:
        stars[coord][coord] = '*'
        return
    
    length = 4 * n - 3

    for i in range(length):
        stars[coord][coord + i] = '*'
        stars[coord + i][coord] = '*'
        stars[coord + length - 1][coord + i] = '*'
        stars[coord + i][coord + length - 1] = '*'
    
    fill_star(n - 1, coord + 2)

fill_star(n, 0)

for row in stars:
    for s in row:
        print(s, end="")
    print()