import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()

pl = 0
pr = n - 1
diff = abs(a[pl] + a[pr])
result = [a[pl], a[pr]]

while pl < pr:
    sum = a[pl] + a[pr]
    if abs(sum) < diff:
        diff = abs(sum)
        result[0] = a[pl]
        result[1] = a[pr]
        if sum == 0:
            break
    if sum > 0:
        pr -= 1
    else:
        pl += 1

print(result[0], result[1])