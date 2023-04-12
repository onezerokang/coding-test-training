n = int(input())

def hanoi(n, start, end):
    mid = 6 - start- end

    if n != 1:
        hanoi(n - 1, start, mid)
    
    print(start, end)
    
    if n != 1:
        hanoi(n - 1, mid, end)

print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3)