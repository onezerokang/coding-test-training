import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def bin_search(a, val):
    pl = 0
    pr = len(a) - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == val:
            return pc
        elif a[pc] <= val:
            pl = pc + 1
        else:
            pr = pc - 1
    return -1
            

for num in b:
    result = bin_search(a, num)
    if result == -1:
        print(0)
    else:
        print(1)