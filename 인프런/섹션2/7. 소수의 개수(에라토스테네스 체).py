# 에라토스테네스 체 적용
n = int(input())

ch = [0 for _ in range(n)]
count = 0
for i in range(2, len(ch)):
    if ch[i] == 0:
        count +=1
        for j in range(i, len(ch), i):
            ch[j] = 1
print(count)

# 처음 제출한 코드
# n = int(input())

# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# count = 0
# for i in range(2, n + 1):
#     is_prime = check_prime(i)
#     if is_prime:
#         count += 1

# print(count)