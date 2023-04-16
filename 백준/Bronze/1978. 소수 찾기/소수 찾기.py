n = int(input())
nums = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
        
cnt = 0
for num in nums:
    if is_prime(num):
        cnt += 1
        
print(cnt)