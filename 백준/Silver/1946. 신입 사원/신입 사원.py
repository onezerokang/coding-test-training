import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    interviewees = [list(map(int, input().split())) for _ in range(N)]
    interviewees.sort(key=lambda x: x[0])

    cut_line = interviewees[0][1]
    passed_count = 1
    for i in range(1, N):
        if interviewees[i][1] < cut_line:
            cut_line = interviewees[i][1]
            passed_count += 1
    print(passed_count)