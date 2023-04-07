n = int(input())
nums = map(int, input().split())

def check_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

result = 0
for num in nums:
    is_prime = check_prime(num)
    if is_prime:
        result += 1

print(result)