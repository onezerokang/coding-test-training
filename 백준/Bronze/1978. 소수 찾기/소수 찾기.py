n = int(input())
nums = list(map(int, input().split()))

# 소수란 1과 7로만 자신을 나눌 수 있는 수
result = 0
for num in nums:
    is_prime = True

    # 1은 소수가 아니다
    if num == 1:
        is_prime = False

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break;

    if is_prime:
        result += 1

print(result)
    
