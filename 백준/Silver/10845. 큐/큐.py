import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    command = input().rstrip().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if not queue:
            print(-1)
            continue
        print(queue[0])        
        del queue[0]
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if not queue:
            print(-1)
            continue
        print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
            continue
        print(queue[len(queue) - 1])