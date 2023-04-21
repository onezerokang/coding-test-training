n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: x[0])
times.sort(key=lambda x: x[1])

cnt = 0
last = 0
for i in range(len(times)):
    # 앞뒤가 같은 애들은 무조건 호출해야 한다. 조건에 안맞더라도
    # 운영 시간이 제일 짧은데 손해임

    if times[i][0] >= last:
        cnt += 1
        last = times[i][1]

print(cnt)