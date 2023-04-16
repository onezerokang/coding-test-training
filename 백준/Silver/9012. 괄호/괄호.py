import sys
input = sys.stdin.readline
t = int(input())


for _ in range(t):
    stack = []
    a = input()
    for ps in a:
        if ps == "(":
            stack.append(ps)
        elif ps == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
