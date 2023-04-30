import sys
input = sys.stdin.readline

n = int(input())

q = [None] * n
front = 0
rear = 0
cnt = 0

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        q[rear] = int(command[1])
        rear += 1
        cnt += 1
        if rear >= n:
            rear = 0

    elif command[0] == 'pop':      
        if cnt == 0:
            print(-1)
        else:
            print(q[front])
            front += 1
            cnt -= 1
            if front >= n:
                front = 0

    elif command[0] == 'size':
        print(cnt)

    elif command[0] == 'empty':
        if cnt == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if cnt == 0:
            print(-1)
        else:
            print(q[front])
            
    elif command[0] == 'back':
        if cnt == 0:
            print(-1)
        else:
            print(q[rear - 1])