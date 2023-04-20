import sys
string = sys.stdin.readline().rstrip()

ppap = ["P", "P", "A", "P"]
stack = []

for i in range(len(string)):
    stack.append(string[i])

    if len(stack) >= 4:
        if ppap == stack[-4:]:
            for _ in range(4):
                stack.pop()
            stack.append('P')

if len(stack) == 1 and stack[0] == 'P':
    print("PPAP")
else:
    print("NP")