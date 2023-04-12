bracket = input()
a = []

ret = 0
for x in bracket:
    if x == "(":
        a.append("(")
    elif x == ")" and a[-1] == "(":
        a.pop()
        ret += len(a)
    else:
        ret += 1
        a.pop()
        
print(ret)

