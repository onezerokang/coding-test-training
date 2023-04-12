a = input()
stack = []
ret = ""

# stack 상단에는 우선순위가 높은 연산자가 있어야 한다.
# 만약 새로운 값이 stack 상단보다 우선순위가 낮다면 stack 상단의 연산자를 pop한다.

for x in a:
    if x.isdecimal():
        ret += x
        continue
    
    if x == "(":
        stack.append(x)
    elif x == "*" or x == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            ret += stack.pop()
        stack.append(x)
    elif x == "+" or x == "-":
        while stack and stack[-1] != "(":
            ret += stack.pop()
        stack.append(x)
    elif x == ")":
        while stack and stack[-1] != "(":
            ret += stack.pop()
        stack.pop()

while stack:
    ret += stack.pop()

print(ret)