import sys
input = sys.stdin.readline

while True:
    legs = list(map(int, input().split()))
    if legs[0] == 0 and legs[1] == 0 and legs[2] == 0:
        break
    
    legs.sort()
    a = legs[0] ** 2 + legs[1] ** 2
    b = legs[2] ** 2
    
    if a == b:
        print("right")
    else:
        print("wrong")