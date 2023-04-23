import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(i, total, plus, minus, multiply, divide):
    global maximum, minimum
    if i == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
    else:
        if plus:
            dfs(i + 1, total + nums[i], plus - 1, minus, multiply, divide)
        if minus:
            dfs(i + 1, total - nums[i], plus, minus - 1, multiply, divide)
        if multiply:
            dfs(i + 1, total * nums[i], plus, minus, multiply - 1, divide)
        if divide:
            dfs(i + 1, int(total / nums[i]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)