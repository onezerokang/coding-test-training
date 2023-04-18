import sys
input = sys.stdin.readline

def qsort(a, left, right):
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

n = int(input())
num = [int(input()) for _ in range(n)]
qsort(num, 0, n - 1)

for x in num:
    print(x)