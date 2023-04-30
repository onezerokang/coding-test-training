N = int(input())

# 선을 1m 혹은 2m 길이로 자른다.
# Nm선이 주어질 때 자르는 방법은 몇 가지인가

d = [0] * (N + 1)
d[1] = 1
d[2] = 2

for i in range(3, N + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[N])
