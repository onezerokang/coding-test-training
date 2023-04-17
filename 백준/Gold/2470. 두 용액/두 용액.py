import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()

pl = 0
pr = n - 1
result = [0, 0]
diff = float('inf')
while pl < pr:
    sum = a[pl] + a[pr]
    if diff > abs(sum):
        result[0], result[1] = a[pl], a[pr]
        diff = abs(sum)
    if sum == 0:
        break
    elif sum > 0:
        pr -= 1
    else:
        pl += 1
        
print(result[0], result[1])
    