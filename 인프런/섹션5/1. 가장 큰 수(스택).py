n, m = map(int, input().split())
n = list(map(int, str(n)))
stack = []

for num in n:
    while stack and m > 0 and stack[-1] < num:
        stack.pop()
        m -= 1

    stack.append(num)

if m != 0:
    stack=stack[:-m]

ret = "".join(str(x) for x in stack)
print(ret)