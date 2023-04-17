import sys
input = sys.stdin.readline

bracket = input()

stack = []
result = 0
temp = 1

for i, b in enumerate(bracket):
    if b == "(":
        temp *= 2
        stack.append(b)
    elif b == "[":
        temp *= 3
        stack.append(b)
    elif b == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break
        if bracket[i-1] == "(":
            result += temp
        temp //= 2
        stack.pop()
    elif b == "]":
        if not stack or stack[-1] != "[":
            result = 0
            break
        if bracket[i-1] == "[":
            result += temp
        temp //= 3
        stack.pop()

# 스택에 값이 남이있다면 유효한 괄호가 아니다
if stack:
    result = 0
print(result)