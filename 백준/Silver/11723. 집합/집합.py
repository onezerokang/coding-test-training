import sys
input = sys.stdin.readline

def add(set, value):
    if set[value] == 0:
        set[value] = 1

def remove(set, value):
    if set[value] == 1:
        set[value] = 0
    
def check(set, value):
    print(set[value])

def toggle(set, value):
    if set[value] == 0:
        set[value] = 1
    else:
        set[value] = 0

def all(set):
    for i in range(1, 21):
        set[i] = 1

def empty(set):
    for i in range(1, 21):
        set[i] = 0

S = [0] * 21
M = int(input())
for _ in range(M):
    cmd = input().rstrip().split()

    if cmd[0] == 'add':
        add(S, int(cmd[1]))
    elif cmd[0] == 'remove':
        remove(S, int(cmd[1]))
    elif cmd[0] == 'check':
        check(S, int(cmd[1]))
    elif cmd[0] == 'toggle':
        toggle(S, int(cmd[1]))
    elif cmd[0] == 'all':
        all(S)
    else:
        empty(S)