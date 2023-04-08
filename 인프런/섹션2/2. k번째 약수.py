# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.

n, k = map(int, input().split())

divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)

if k > len(divisor):
    print(-1)
else:
    print(divisor[k - 1])
