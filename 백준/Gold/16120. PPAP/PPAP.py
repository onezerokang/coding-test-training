import sys

string = sys.stdin.readline().strip()
stack = []
ppap =['P','P','A','P']

for i in range(0,len(string)) :

    stack.append(string[i])
    if len(stack) >= 4 :
        if stack[-4:] == ppap : 
            for j in range(0,4) :
                stack.pop()
            if i == len(string) -1 :
                break
            else :
                stack.append("P")

if stack == ppap or len(stack) == 0:
    print("PPAP")
elif len(stack) == 1 and stack[0] == "P" :
    print("PPAP")
else :
    print("NP")