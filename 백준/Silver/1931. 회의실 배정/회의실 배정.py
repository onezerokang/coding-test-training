import sys
input = sys.stdin.readline

N = int(input())
meeting_list = [list(map(int, input().split())) for _ in range(N)]

meeting_list.sort(key=lambda x: x[0])
meeting_list.sort(key=lambda x: x[1])

end_time = 0
result = 0
for x in meeting_list:
    if x[0] >= end_time:
        end_time = x[1]
        result += 1

print(result)