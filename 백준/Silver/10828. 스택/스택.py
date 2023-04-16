import sys
input = sys.stdin.readline
n = int(input())

s = []
ptr = 0

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        s.append(int(command[1]))
        ptr += 1
    elif command[0] == 'pop':
        if ptr <= 0:
            print(-1)
        else:
            print(s[ptr - 1])
            del s[ptr - 1]
            ptr -= 1
    elif command[0] == 'size':
        print(ptr)
    elif command[0] == 'empty':
        if ptr <= 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if ptr <= 0:
            print(-1)
        else:
            print(s[ptr - 1])