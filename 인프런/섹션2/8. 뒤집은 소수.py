n = int(input())
num_list = list(map(int, input().split()))

def reverse(x):
    result = ""
    x = str(x)
    for i in range(len(x) - 1, -1, -1):
        result += x[i]
    
    return int(result)

def is_prime(x):
    x = int(x)
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for num in num_list:
    reversed_num = reverse(num)
    if is_prime(reversed_num):
        print(reversed_num)