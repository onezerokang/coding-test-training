postfix = input()

stack = []

for x in postfix:
    if x.isdecimal():
        stack.append(int(x))
        continue

    a = stack.pop()
    b = stack.pop()
    
    if x == "*":
        stack.append(b * a)
    elif x == "/":
        stack.append(b / a)
    elif x == "+":
        stack.append(b + a)
    elif x == '-':
        stack.append(b - a)

print(stack[0])