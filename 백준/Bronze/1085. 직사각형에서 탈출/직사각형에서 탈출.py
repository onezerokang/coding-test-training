x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

result = x
values = [y, h - y, w - x]
for value in values:
    if result > value:
        result = value

print(result)