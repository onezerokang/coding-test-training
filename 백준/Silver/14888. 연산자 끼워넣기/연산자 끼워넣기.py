import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

def dfs(calc_cnt, total, plus, minus, multiply, divide):
    global min_val, max_val

    if calc_cnt == N:
        if total < min_val:
            min_val = total
        if total > max_val:
            max_val = total
        return
    
    if plus:
        dfs(calc_cnt + 1, total + nums[calc_cnt], plus - 1, minus, multiply, divide)
    if minus:
        dfs(calc_cnt + 1, total - nums[calc_cnt], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(calc_cnt + 1, total * nums[calc_cnt], plus, minus, multiply - 1, divide)
    if divide:
        dfs(calc_cnt + 1, int(total / nums[calc_cnt]), plus, minus, multiply, divide - 1)

min_val = 1e9
max_val = -1e9
dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_val)
print(min_val)
