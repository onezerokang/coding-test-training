import sys
input = sys.stdin.readline
a = input().rstrip()

operator = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
}
stack = []
ans = ""

for x in a:
    if x.isalpha():
        ans += x
    else:
        # 닫는 괄호가 나오면 여는 괄호가 나올 때까지 ans에 더한다.
        if x == ")":
            while True:
                tmp = stack.pop()
                if tmp == "(":
                    break
                ans += tmp
            continue

        if x == "(":
            stack.append(x)
            continue

        # 마지막 요소보다 우선순위가 낮으면 마지막 요소를 pop하여 ans에 더한다.
        while stack and stack[-1] != "(" and operator[stack[-1]] >= operator[x]:
            ans += stack.pop()
        
        stack.append(x)


while stack:
    ans += stack.pop()

print(ans)